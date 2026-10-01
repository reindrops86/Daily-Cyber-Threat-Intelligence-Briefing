"""Render the analyst, executive, and watchlist reports from one item set."""

from __future__ import annotations

import re
from typing import Any

from .schema import EVIDENCE_CLASS_LEGEND, LIVE_BANNER, SYNTHETIC_BANNER, Item, evidence_class

CVE_SUBJECT = re.compile(r"CVE-\d{4}-\d{4,7}")
CVSS_IN_TEXT = re.compile(r"CVSS (\d+(?:\.\d+)?)")
EPSS_PRIORITY_FLOOR = 0.10
CVSS_PRIORITY_FLOOR = 9.0

PATCH_PRIORITY_LEGEND = (
    "Patch priority combines three independent signals and is shown "
    "alongside, not folded into, the finding score: P1 = listed in CISA KEV "
    f"(exploitation confirmed); P2 = not in KEV but EPSS >= {EPSS_PRIORITY_FLOOR:.2f} "
    f"or CVSS >= {CVSS_PRIORITY_FLOOR}; P3 = neither. EPSS is FIRST.org's "
    "modelled probability of exploitation in the next 30 days; CVSS is the "
    "NVD base severity. A missing value is reported as 'n/a', never guessed."
)

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


def _cvss_for(item: Item, vuln_intel: dict[str, dict[str, Any]]) -> float | None:
    known = vuln_intel.get(item.subject, {}).get("cvss")
    if known is not None:
        return float(known)
    for record in item.evidence:
        match = CVSS_IN_TEXT.search(record.statement)
        if match:
            return float(match.group(1))
    return None


def patch_priority(in_kev: bool, epss: float | None, cvss: float | None) -> tuple[str, str]:
    if in_kev:
        return "P1 - patch now", "listed in CISA KEV, exploitation confirmed"
    if epss is not None and epss >= EPSS_PRIORITY_FLOOR:
        return "P2 - patch this cycle", f"EPSS {epss:.3f} >= {EPSS_PRIORITY_FLOOR:.2f}"
    if cvss is not None and cvss >= CVSS_PRIORITY_FLOOR:
        return "P2 - patch this cycle", f"CVSS {cvss} >= {CVSS_PRIORITY_FLOOR}"
    return "P3 - scheduled patching", "not in KEV; EPSS and CVSS below priority floors or unavailable"


def _vuln_row(item: Item, vuln_intel: dict[str, dict[str, Any]]) -> dict[str, Any]:
    intel = vuln_intel.get(item.subject, {})
    in_kev = any(record.source == "cisa_kev" for record in item.evidence)
    epss = intel.get("epss")
    cvss = _cvss_for(item, vuln_intel)
    tier, reason = patch_priority(in_kev, epss, cvss)
    return {
        "in_kev": in_kev, "epss": epss, "percentile": intel.get("percentile"),
        "cvss": cvss, "tier": tier, "reason": reason,
    }


def _fmt(value: float | None, pattern: str) -> str:
    return "n/a" if value is None else pattern.format(value)


def _pirs_for(item: Item, pirs: list[dict[str, Any]]) -> list[str]:
    return [pir["id"] for pir in pirs if item.rule_id in pir.get("rule_ids", [])]


def render(
    items: list[Item], day_label: str, generated_at: str,
    history_lines: list[str], trend: dict[str, Any] | None = None, live: bool = False,
    vuln_intel: dict[str, dict[str, Any]] | None = None, pirs: list[dict[str, Any]] | None = None,
) -> dict[str, str]:
    reportable = [item for item in items if not item.suppressed]
    suppressed = [item for item in items if item.suppressed]
    banner = LIVE_BANNER if live else SYNTHETIC_BANNER
    pirs = pirs or []
    cve_items = (
        [item for item in reportable if CVE_SUBJECT.fullmatch(item.subject)]
        if vuln_intel is not None else []
    )
    vuln_rows = {item.item_id: _vuln_row(item, vuln_intel or {}) for item in cve_items}

    analyst = [
        f"# Analyst Briefing - {day_label}", "",
        f"**Generated:** {generated_at}", "",
        f"> {banner}", "",
        f"_{SCORING_LEGEND}_", "",
        f"_{CONFIDENCE_LEGEND}_", "",
        f"_{EVIDENCE_CLASS_LEGEND}_", "",
    ]
    if vuln_rows:
        analyst += [
            "## Vulnerability Patch Priority (KEV + EPSS + CVSS)", "",
            f"_{PATCH_PRIORITY_LEGEND}_", "",
            "| CVE | Priority | In KEV | EPSS (percentile) | CVSS | Finding |",
            "|---|---|---|---|---|---|",
        ]
        tier_order = {"P1": 0, "P2": 1, "P3": 2}
        for item in sorted(cve_items, key=lambda i: (tier_order[vuln_rows[i.item_id]["tier"][:2]], -i.score)):
            row = vuln_rows[item.item_id]
            epss = "n/a" if row["epss"] is None else f"{row['epss']:.3f} ({_fmt(row['percentile'], '{:.0%}')})"
            analyst.append(
                f"| {item.subject} | {row['tier']} | {'yes' if row['in_kev'] else 'no'} | {epss} | "
                f"{_fmt(row['cvss'], '{}')} | {item.item_id} |"
            )
        analyst.append("")
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
        ]
        addressed = _pirs_for(item, pirs)
        if addressed:
            analyst.append(f"**Addresses:** {', '.join(addressed)}")
        if item.item_id in vuln_rows:
            row = vuln_rows[item.item_id]
            analyst.append(f"**Patch priority:** {row['tier']} ({row['reason']})")
        analyst.append("**Evidence:**")
        analyst += [f"- **{evidence_class(record.source)}:** {record.line()}" for record in item.evidence]
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

    if pirs:
        executive += ["", "## Priority Intelligence Requirements", ""]
        for pir in pirs:
            answering = [item for item in reportable if item.rule_id in pir.get("rule_ids", [])]
            if answering:
                top = max(answering, key=lambda i: i.score)
                status = f"{len(answering)} reportable finding(s); highest: {top.item_id} ({top.severity}, score {top.score})"
            else:
                status = "no new intelligence this cycle (collection gap or nothing observed)"
            executive.append(f"- **{pir['id']}** {pir['question']} -- {status}")

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
