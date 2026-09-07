"""Analyst feedback and executive trend metrics.

Feedback labels are recorded for evaluation -- to measure how well the engine
is scoring and prioritizing -- not fed back automatically into future scoring.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date

from .schema import FEEDBACK_LABELS, Item, parse_date


@dataclass
class Feedback:
    item_id: str
    day: str
    label: str
    analyst: str
    note: str = ""

    def __post_init__(self) -> None:
        if self.label not in FEEDBACK_LABELS:
            raise ValueError(f"unknown feedback label: {self.label}")


@dataclass
class FeedbackLog:
    entries: list[Feedback] = field(default_factory=list)

    def record(self, item_id: str, day: str, label: str, analyst: str, note: str = "") -> Feedback:
        entry = Feedback(item_id, day, label, analyst, note)
        self.entries.append(entry)
        return entry

    def first_feedback_day(self, item_id: str) -> str | None:
        matches = [entry.day for entry in self.entries if entry.item_id == item_id]
        return min(matches) if matches else None

    def false_positive_rate(self) -> float:
        if not self.entries:
            return 0.0
        false_positives = sum(1 for entry in self.entries if entry.label == "false_positive")
        return round(false_positives / len(self.entries), 3)


def compute_trend(daily_items: list[list[Item]], daily_labels: list[str], feedback: FeedbackLog) -> dict:
    """Executive metrics computed across a run of daily item snapshots."""
    if not daily_items:
        return {}

    all_ids = {item.item_id for day in daily_items for item in day}
    first_seen_by_id = {}
    for day in daily_items:
        for item in day:
            first_seen_by_id.setdefault(item.item_id, item.first_seen)

    new_counts, recurring_counts, suppressed_counts, total_scores = [], [], [], []
    for day in daily_items:
        new_counts.append(sum(1 for item in day if item.state == "NEW"))
        recurring_counts.append(sum(1 for item in day if item.state in {"ACTIVE", "UNCHANGED"}))
        suppressed_counts.append(sum(1 for item in day if item.suppressed))
        total_scores.append(round(sum(item.score for item in day if not item.suppressed), 2))

    reopened_total = sum(1 for day in daily_items for item in day if item.state == "REOPENED")

    triage_deltas, mitigate_deltas = [], []
    mitigated_or_resolved_seen: set[str] = set()
    for day in daily_items:
        for item in day:
            first_feedback = feedback.first_feedback_day(item.item_id)
            if first_feedback:
                triage_deltas.append((parse_date(first_feedback) - parse_date(item.first_seen)).days)
            if item.state in {"MITIGATED", "RESOLVED"} and item.item_id not in mitigated_or_resolved_seen:
                mitigated_or_resolved_seen.add(item.item_id)
                mitigate_deltas.append((parse_date(item.last_seen) - parse_date(item.first_seen)).days)

    latest = daily_items[-1]
    latest_day = parse_date(daily_labels[-1])
    overdue_critical = sum(
        1 for item in latest
        if item.severity == "critical" and item.state not in {"RESOLVED"} and latest_day.isoformat() > item.deadline
    )

    return {
        "days": daily_labels,
        "new_per_day": new_counts,
        "recurring_per_day": recurring_counts,
        "suppressed_per_day": suppressed_counts,
        "total_exposure_per_day": total_scores,
        "reopened_total": reopened_total,
        "mean_time_to_triage_days": round(sum(triage_deltas) / len(triage_deltas), 2) if triage_deltas else None,
        "mean_time_to_mitigate_days": round(sum(mitigate_deltas) / len(mitigate_deltas), 2) if mitigate_deltas else None,
        "overdue_critical_findings": overdue_critical,
        "suppression_rate_latest": round(suppressed_counts[-1] / len(latest), 3) if latest else 0.0,
        "false_positive_rate": feedback.false_positive_rate(),
        "tracked_findings_total": len(all_ids),
    }
