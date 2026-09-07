"""Render the analyst, executive, and watchlist reports from one item set."""

from __future__ import annotations

from typing import Any

from .schema import LIVE_BANNER, SYNTHETIC_BANNER, Item

CONFIDENCE_LEGEND = (
    "Confidence bands: >=0.85 high (multiple reliable sources or direct "
    "telemetry), 0.60-0.84 moderate (single reliable source or partial "
    "corroboration), <0.60 low (single low-reliability source, e.g. an "
    "unconfirmed dark-web post)."
)

SCORING_LEGEND = (
    "Score = base (rule severity) x amplifier_factor (extra corroborating "
    "signal types) x source_confidence (independent sources, capped so "
    "circular reporting cannot inflate it) x signal_confidence (mean "
    "collector confidence) x asset_multiplier (data sensitivity, exposure, "
    "and operational importance of the affected asset), capped at 100. "
    "Severity is a fixed band on that score, never hand-set."
)

NON_ACTIVE_STATES = {"PENDING_VERIFICATION", "STALE", "MITIGATED", "RESOLVED"}

SUPPRESSION_NOTE = (
    "Suppressed findings are not deleted. They remain tracked with full "
    "history so that if a suppressed finding's severity rises, its evidence "
    "changes, its deadline passes, or it is mitigated or reopens, it "
    "reappears in the very next briefing without having lost its record."
)


def _state_caveat(item: Item) -> str:
    if item.state in NON_ACTIVE_STATES:
        return (
            f" _Score and severity reflect the last active measurement on "
            f"{item.last_evidence_at}, not current risk; state is {item.state}._"
        )
    return ""


def render(
    items: list[Item], day_label: str, generated_at: str,
    history_lines: list[str], trend: dict[str, Any] | None = None, live: bool = False,
) -> dict[str, str]:
    reportable = [item for item in items if not item.suppressed]
    suppressed = [item for item in items if item.suppressed]
    banner = LIVE_BANNER if live else SYNTHETIC_BANNER

    analyst = [
        f"# Analyst Briefing - {day_label}", "",
        f"**Generated:** {generated_at}", "",
        f"> {banner}", "",
        f"_{SCORING_LEGEND}_", "",
        f"_{CONFIDENCE_LEGEND}_", "",
    ]
    executive = [
        f"# Executive Summary - {day_label}", "",
        f"> {banner}", "",
        "## Material Risks", "",
    ]
    watchlist = [f"# Watchlist - {day_label}", "", f"> {banner}", ""]
    resolved_lines: list[str] = []

    for item in reportable:
        analyst += [
            f"## {item.item_id} - {item.title}",
            f"**Severity:** {item.severity} | **Score:** {item.score} | **State:** {item.state}"
            + _state_caveat(item),
            f"**What changed:** {item.change}",
            f"**Why reported today:** {item.reportable_reason}",
            f"**Independent sources:** {item.independent_sources}"
            + (" (circular reporting suspected across shared upstream reports)" if item.circular_reporting else ""),
            "**Evidence:**",
        ]
        analyst += [f"- {record.line()}" for record in item.evidence]
        if item.remediation:
            analyst.append("**Remediation evidence:**")
            analyst += [f"- {line}" for line in item.remediation]
        analyst += [
            f"**Score components:** {item.components}",
            f"**Owner:** {item.owner} | **Deadline:** {item.deadline} | **Recommended action:** {item.action}",
            f"**Verification method:** {item.verification_method}",
            "",
        ]

        if item.state == "RESOLVED":
            resolved_lines.append(f"- {item.title} (last active score {item.score}, closed {item.last_seen}).")
        elif item.severity in {"critical", "high"} and item.state != "MITIGATED":
            executive.append(f"- **{item.severity.upper()}** {item.title} (score {item.score}, {item.state}). Owner: {item.owner}. Action: {item.action}")
        elif item.state == "MITIGATED":
            executive.append(f"- **MITIGATION PENDING VERIFICATION** {item.title} (owner {item.owner}).")

    # The watchlist is the full tracking view, not just today's headline items:
    # a suppressed finding is still tracked in full and will resurface here the
    # moment anything material changes about it (see SUPPRESSION_NOTE below).
    for item in items:
        flag = " [suppressed this cycle]" if item.suppressed else ""
        watchlist.append(
            f"- {item.item_id}: {item.severity}, state {item.state}, score {item.score}, "
            f"owner {item.owner}, deadline {item.deadline}{flag}"
        )

    if not any(line.startswith("- **") for line in executive):
        executive.append("_No active critical or high risks in this briefing._")

    executive += ["", "## Resolved Since Last Briefing", ""]
    executive += resolved_lines if resolved_lines else ["_Nothing resolved with verified remediation evidence in this briefing._"]

    executive += ["", "## Suppressed Findings", "", SUPPRESSION_NOTE, ""]
    executive.append(f"{len(suppressed)} unchanged, low/medium-severity finding(s) suppressed this cycle.")

    executive += ["", "## Trend", ""]
    executive += history_lines

    if trend:
        executive += ["", "## Executive Metrics", ""]
        executive += [
            f"- New vs. recurring (per day): {list(zip(trend['days'], trend['new_per_day'], trend['recurring_per_day']))}",
            f"- Mean time to triage: {trend['mean_time_to_triage_days']} day(s)" if trend["mean_time_to_triage_days"] is not None else "- Mean time to triage: no analyst feedback recorded yet",
            f"- Mean time to mitigate: {trend['mean_time_to_mitigate_days']} day(s)" if trend["mean_time_to_mitigate_days"] is not None else "- Mean time to mitigate: none mitigated yet",
            f"- Overdue critical findings: {trend['overdue_critical_findings']}",
            f"- Reopened findings (cumulative): {trend['reopened_total']}",
            f"- Suppression rate (latest day): {trend['suppression_rate_latest']}",
            f"- False-positive rate (from analyst feedback): {trend['false_positive_rate']}",
            f"- Total exposure trend (sum of reportable scores per day): {trend['total_exposure_per_day']}",
        ]

    return {"analyst": "\n".join(analyst), "executive": "\n".join(executive), "watchlist": "\n".join(watchlist)}
