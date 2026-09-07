"""Correlate multi-source CTI signals into a prioritized daily briefing.

A raw indicator, CVE, or dark-web mention is not a briefing item. It becomes
one when it combines with sector targeting, internal telemetry, or multiple
independent sources -- the same discipline used across this portfolio's other
evidence-first reporting systems.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Signal:
    signal_type: str
    subject: str
    source: str
    confidence: float
    detail: str


@dataclass
class Item:
    item_id: str
    rule_id: str
    title: str
    subject: str
    score: float
    components: dict[str, float]
    severity: str
    evidence: list[str]
    action: str
    state: str = "new"
    change: str = "First observed."
    suppressed: bool = False


RULES: dict[str, dict[str, Any]] = {
    "CTI-001": {
        "title": "Exploited vulnerability reachable in the environment and targeting our sector",
        "required": {"known_exploited_vulnerability", "sector_targeting", "environment_reachable"},
        "base": 70.0,
        "action": "Patch or virtually patch within 48 hours; confirm compensating controls until then.",
    },
    "CTI-002": {
        "title": "Tracked threat actor campaign confirmed active in internal telemetry",
        "required": {"actor_campaign_activity", "internal_ioc_sighting"},
        "base": 62.0,
        "action": "Escalate to incident response; hunt for the actor's known TTPs across the estate.",
    },
    "CTI-003": {
        "title": "Dark-web mention referencing the organization or sector",
        "required": {"dark_web_mention"},
        "amplifiers": {"sector_targeting"},
        "base": 30.0,
        "action": "Validate against internal telemetry before escalating; monitor for corroboration.",
    },
    "CTI-004": {
        "title": "Indicator corroborated by multiple independent sources",
        "required": {"multi_source_corroboration"},
        "base": 35.0,
        "action": "Add to the active watchlist and block at available control points.",
    },
    "CTI-005": {
        "title": "Newly disclosed high-severity vulnerability reachable but not yet exploited",
        "required": {"high_severity_vulnerability", "environment_reachable"},
        "base": 40.0,
        "action": "Prioritize patching ahead of public exploitation; track KEV status daily.",
    },
}

SEVERITY_BANDS = ((70.0, "critical"), (50.0, "high"), (30.0, "medium"), (0.0, "low"))


def _severity(score: float) -> str:
    for floor, label in SEVERITY_BANDS:
        if score >= floor:
            return label
    return "low"


def correlate(signals: list[Signal], prior: dict[str, Item] | None = None) -> list[Item]:
    prior = prior or {}
    by_subject: dict[str, list[Signal]] = {}
    for signal in signals:
        by_subject.setdefault(signal.subject, []).append(signal)

    items: list[Item] = []
    for subject, subject_signals in by_subject.items():
        types = {s.signal_type for s in subject_signals}
        for rule_id, rule in RULES.items():
            if not rule["required"] <= types:
                continue
            amplifiers = rule.get("amplifiers", set()) & types
            used_types = rule["required"] | amplifiers
            used = [s for s in subject_signals if s.signal_type in used_types]

            confidence = sum(s.confidence for s in used) / len(used)
            source_count = len({s.source for s in used})
            source_confidence = min(1.15, 1.0 + 0.05 * (source_count - 1))
            amplifier_factor = 1.0 + 0.15 * len(amplifiers)

            score = round(min(100.0, rule["base"] * amplifier_factor * source_confidence * confidence), 2)
            components = {
                "base": rule["base"],
                "amplifier_factor": round(amplifier_factor, 2),
                "source_confidence": round(source_confidence, 2),
                "signal_confidence": round(confidence, 3),
            }

            item_id = f"{rule_id}:{subject}"
            evidence = [f"[{s.source}] {s.detail}" for s in sorted(used, key=lambda s: s.signal_type)]

            previous = prior.get(item_id)
            if previous is None:
                state, change = "new", "First observed exposure or activity."
            elif previous.state == "resolved":
                state, change = "escalated", "Previously resolved item is active again."
            elif score > previous.score + 3:
                state, change = "escalated", f"Priority rose from {previous.score} to {score}."
            elif score < previous.score - 3:
                state, change = "de-escalated", f"Priority fell from {previous.score} to {score}."
            else:
                state, change = "unchanged", "No material change since the previous briefing."

            severity = _severity(score)
            item = Item(
                item_id, rule_id, f"{rule['title']}: {subject}", subject, score, components,
                severity, evidence, rule["action"], state, change,
                suppressed=(state == "unchanged" and severity in {"low", "medium"}),
            )
            items.append(item)
    return sorted(items, key=lambda item: -item.score)


def reconcile_resolved(items: list[Item], prior: dict[str, Item]) -> list[Item]:
    """Anything previously tracked and now absent is resolved for this briefing."""
    seen = {item.item_id for item in items}
    resolved: list[Item] = []
    for item_id, previous in prior.items():
        if item_id in seen or previous.state == "resolved":
            continue
        previous.state = "resolved"
        previous.change = "No longer observed; treat as resolved pending confirmation."
        previous.suppressed = False
        resolved.append(previous)
    return items + resolved


def render(items: list[Item], day_label: str, history: list[dict[str, Any]]) -> dict[str, str]:
    reportable = [item for item in items if not item.suppressed]

    analyst = [f"# Analyst Briefing - {day_label}", ""]
    executive = [f"# Executive Summary - {day_label}", "", "## Material Risks", ""]
    watchlist = [f"# Watchlist - {day_label}", ""]
    resolved_lines: list[str] = []

    for item in reportable:
        analyst += [
            f"## {item.item_id} - {item.title}",
            f"**Severity:** {item.severity} | **Score:** {item.score} | **State:** {item.state}",
            f"**What changed:** {item.change}",
            "**Evidence:**",
        ]
        analyst += [f"- {line}" for line in item.evidence]
        analyst += [f"**Score components:** {item.components}", f"**Recommended action:** {item.action}", ""]

        if item.state == "resolved":
            resolved_lines.append(f"- {item.title} (last score {item.score}).")
        elif item.severity in {"critical", "high"}:
            executive.append(f"- **{item.severity.upper()}** {item.title} (score {item.score}, {item.state}). Action: {item.action}")

        watchlist.append(f"- {item.item_id}: {item.severity}, state {item.state}, score {item.score}")

    if not any(line.startswith("- **") for line in executive):
        executive.append("_No active critical or high risks in this briefing._")

    executive += ["", "## Resolved Since Last Briefing", ""]
    executive += resolved_lines if resolved_lines else ["_Nothing resolved in this briefing._"]

    executive += ["", "## Trend", ""]
    for entry in history:
        executive.append(f"- {entry['day']}: {entry['reportable']} reported, {entry['critical']} critical, {entry['suppressed']} suppressed")

    return {"analyst": "\n".join(analyst), "executive": "\n".join(executive), "watchlist": "\n".join(watchlist)}


def summarize(items: list[Item]) -> dict[str, int]:
    reportable = [item for item in items if not item.suppressed]
    return {
        "reportable": len(reportable),
        "critical": sum(item.severity == "critical" for item in reportable),
        "suppressed": sum(item.suppressed for item in items),
    }


# -- Synthetic three-day CTI feed -------------------------------------------

def _day(n: int) -> list[Signal]:
    if n == 1:
        return [
            Signal("known_exploited_vulnerability", "CVE-2026-41821", "sca_scanner", 0.98, "KEV-listed, CVSS 9.6."),
            Signal("sector_targeting", "CVE-2026-41821", "vendor_advisory", 0.85, "Vendor confirms active targeting of financial services."),
            Signal("environment_reachable", "CVE-2026-41821", "asset_inventory", 0.95, "Affected service is internet-facing."),
            Signal("actor_campaign_activity", "UNC-4471", "commercial_feed", 0.8, "Campaign observed against peer organizations this week."),
            Signal("dark_web_mention", "acme-corp", "darkweb_monitor", 0.55, "Forum post references acquiring access to 'a mid-size bank'."),
            Signal("high_severity_vulnerability", "CVE-2026-50210", "sca_scanner", 0.9, "CVSS 8.7, disclosed yesterday, no known exploitation yet."),
            Signal("environment_reachable", "CVE-2026-50210", "asset_inventory", 0.9, "Affected library is used by the public API gateway."),
        ]
    if n == 2:
        return [
            Signal("known_exploited_vulnerability", "CVE-2026-41821", "sca_scanner", 0.98, "Still KEV-listed; patch not yet deployed."),
            Signal("sector_targeting", "CVE-2026-41821", "vendor_advisory", 0.85, "Targeting confirmed continues."),
            Signal("environment_reachable", "CVE-2026-41821", "asset_inventory", 0.95, "Affected service is internet-facing."),
            Signal("actor_campaign_activity", "UNC-4471", "commercial_feed", 0.82, "Campaign infrastructure expanded."),
            Signal("internal_ioc_sighting", "UNC-4471", "edr_telemetry", 0.9, "Actor's known C2 domain observed in outbound proxy logs."),
            Signal("multi_source_corroboration", "185.220.101.44", "commercial_feed", 0.7, "Malicious hosting IP reported by feed vendor."),
            Signal("multi_source_corroboration", "185.220.101.44", "isac_share", 0.75, "Same IP shared independently by sector ISAC."),
        ]
    return [
        Signal("actor_campaign_activity", "UNC-4471", "commercial_feed", 0.82, "Campaign infrastructure expanded."),
        Signal("internal_ioc_sighting", "UNC-4471", "edr_telemetry", 0.9, "Actor's known C2 domain observed in outbound proxy logs."),
        Signal("multi_source_corroboration", "185.220.101.44", "commercial_feed", 0.7, "Malicious hosting IP reported by feed vendor."),
        Signal("multi_source_corroboration", "185.220.101.44", "isac_share", 0.75, "Same IP shared independently by sector ISAC."),
    ]


def demo_days() -> list[list[Signal]]:
    return [_day(1), _day(2), _day(3)]
