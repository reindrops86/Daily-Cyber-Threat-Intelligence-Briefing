"""Correlate signals into findings and advance each finding's lifecycle.

The one rule this module exists to enforce: the absence of a signal is not
evidence of remediation. A finding can only become MITIGATED or RESOLVED when
a remediation_evidence signal says so. Everything else that stops being
observed ages through PENDING_VERIFICATION and, past its freshness window,
STALE -- never RESOLVED.
"""

from __future__ import annotations

from datetime import date
from typing import Any

from .schema import (
    CLOSED_OR_AGED_STATES, DEFAULT_ASSET_CONTEXT, AssetContext, EvidenceRecord,
    Item, Signal, asset_multiplier, deadline_from, parse_date, severity_for,
)

RULES: dict[str, dict[str, Any]] = {
    "CTI-001": {
        "title": "Exploited vulnerability reachable in the environment and targeting our sector",
        "required": {"known_exploited_vulnerability", "sector_targeting", "environment_reachable"},
        "base": 70.0,
        "action": "Patch or virtually patch within the SLA window; confirm compensating controls until then.",
        "verification_method": "Re-scan the asset and confirm the vulnerability signature is no longer detected.",
    },
    "CTI-002": {
        "title": "Tracked threat actor campaign confirmed active in internal telemetry",
        "required": {"actor_campaign_activity", "internal_ioc_sighting"},
        "base": 62.0,
        "action": "Escalate to incident response; hunt for the actor's known TTPs across the estate.",
        "verification_method": "Confirm no further C2 communication in EDR telemetry for the SLA window.",
    },
    "CTI-003": {
        "title": "Dark-web mention referencing the organization or sector",
        "required": {"dark_web_mention"},
        "amplifiers": {"sector_targeting"},
        "base": 30.0,
        "action": "Validate against internal telemetry before escalating; monitor for corroboration.",
        "verification_method": (
            "None. A dark-web mention has no remediation artifact; it is only "
            "ever confirmed by corroborating telemetry (a different finding) "
            "or allowed to expire."
        ),
    },
    "CTI-004": {
        "title": "Indicator corroborated by multiple independent sources",
        "required": {"multi_source_corroboration"},
        "base": 35.0,
        "action": "Add to the active watchlist and block at available control points.",
        "verification_method": "Confirm the indicator no longer appears in egress or DNS telemetry after blocking.",
    },
    "CTI-005": {
        "title": "Newly disclosed high-severity vulnerability reachable but not yet exploited",
        "required": {"high_severity_vulnerability", "environment_reachable"},
        "base": 40.0,
        "action": "Prioritize patching ahead of public exploitation; track KEV status daily.",
        "verification_method": "Re-scan the asset and confirm the vulnerability signature is no longer detected.",
    },
}

MATERIAL_SCORE_DELTA = 3.0


def _rule_ttl_days(rule: dict[str, Any]) -> int:
    """TTL is governed only by the required signal types.

    Amplifiers are optional boosters, not the evidence the finding depends on;
    letting a long-lived amplifier (e.g. sector_targeting) stretch out a
    short-lived required signal's freshness window (e.g. dark_web_mention)
    would let a stale claim look current far longer than its own evidence
    supports.
    """
    return max(
        (Signal(t, "", "", "F", 0, "", date.today().isoformat(), date.today().isoformat()).ttl_days() for t in rule["required"]),
        default=7,
    )


def _corroboration(signals: list[Signal]) -> tuple[int, bool]:
    """Collapse signals that share an upstream_id into one independent source."""
    groups: dict[str, list[Signal]] = {}
    standalone = 0
    for signal in signals:
        if signal.upstream_id:
            groups.setdefault(signal.upstream_id, []).append(signal)
        else:
            standalone += 1
    circular = any(len({s.source for s in group}) > 1 for group in groups.values())
    independent = standalone + len(groups)
    return max(1, independent), circular


def _merge_evidence(prior: list[EvidenceRecord], fresh: list[Signal], today: str) -> list[EvidenceRecord]:
    by_key = {(record.source, record.statement): record for record in prior}
    for signal in fresh:
        key = (signal.source, signal.detail)
        existing = by_key.get(key)
        if existing:
            existing.last_observed = today
        else:
            by_key[key] = EvidenceRecord(
                source=signal.source, source_reliability=signal.source_reliability,
                confidence=signal.confidence, statement=signal.detail,
                first_observed=signal.observed_at, last_observed=today,
            )
    return list(by_key.values())


def advance(
    rule_id: str, subject: str, today: date, signals_today: list[Signal],
    prior: Item | None, context: AssetContext | None = None,
) -> Item | None:
    rule = RULES[rule_id]
    context = context or DEFAULT_ASSET_CONTEXT
    required, amplifiers = rule["required"], rule.get("amplifiers", set())

    relevant_today = [
        s for s in signals_today
        if s.signal_type in required | amplifiers and not s.expired_on(today)
    ]
    satisfied = required <= {s.signal_type for s in relevant_today}
    remediation_today = [s for s in signals_today if s.signal_type == "remediation_evidence"]

    if not satisfied and not remediation_today and prior is None:
        return None  # never existed; nothing to report

    item_id = f"{rule_id}:{subject}"
    today_iso = today.isoformat()

    if satisfied:
        used_amplifiers = amplifiers & {s.signal_type for s in relevant_today}
        independent_sources, circular = _corroboration(relevant_today)
        source_confidence = min(1.15, 1.0 + 0.05 * (independent_sources - 1))
        signal_confidence = sum(s.confidence for s in relevant_today) / len(relevant_today)
        amplifier_factor = 1.0 + 0.15 * len(used_amplifiers)
        multiplier = asset_multiplier(context)
        score = round(min(100.0, rule["base"] * amplifier_factor * source_confidence * signal_confidence * multiplier), 2)
        components = {
            "base": rule["base"], "amplifier_factor": round(amplifier_factor, 2),
            "source_confidence": round(source_confidence, 2), "signal_confidence": round(signal_confidence, 3),
            "asset_multiplier": multiplier,
        }
        evidence = _merge_evidence(prior.evidence if prior else [], relevant_today, today_iso)

        if prior is None:
            state, change = "NEW", "First observed."
        elif prior.state in CLOSED_OR_AGED_STATES:
            state = "REOPENED"
            change = f"Supporting evidence reappeared after the finding was {prior.state.lower()}."
        elif abs(score - prior.score) > MATERIAL_SCORE_DELTA:
            state, change = "ACTIVE", f"Priority moved from {prior.score} to {score}."
        else:
            state, change = "UNCHANGED", "No material change since the previous briefing."

        severity = severity_for(score)
        first_seen = today_iso if prior is None else prior.first_seen
        deadline = deadline_from(today_iso, severity) if state in {"NEW", "REOPENED"} else (prior.deadline if prior else deadline_from(today_iso, severity))
        remediation = [] if state in {"NEW", "REOPENED"} else (prior.remediation if prior else [])
    else:
        if not prior:
            return None
        evidence = prior.evidence
        score, severity = prior.score, prior.severity
        components = prior.components
        independent_sources, circular = prior.independent_sources, prior.circular_reporting
        first_seen, deadline = prior.first_seen, prior.deadline

        if remediation_today:
            verified = any(s.remediation_verified for s in remediation_today)
            state = "RESOLVED" if verified else "MITIGATED"
            kinds = ", ".join(sorted({s.remediation_kind or "remediation" for s in remediation_today}))
            change = (
                f"Remediation verified ({kinds})." if verified
                else f"Remediation reported ({kinds}); pending independent verification."
            )
            evidence = _merge_evidence(evidence, remediation_today, today_iso)
            remediation = list(prior.remediation) + [f"{today_iso}: {s.detail}" for s in remediation_today]
            last_evidence_at = today_iso
        elif prior.state in {"MITIGATED", "RESOLVED"}:
            state, change = prior.state, f"No new evidence; remains {prior.state.lower()}."
            remediation = prior.remediation
            last_evidence_at = prior.last_evidence_at
        else:
            age = (today - parse_date(prior.last_evidence_at)).days
            ttl = _rule_ttl_days(rule)
            remediation = prior.remediation
            last_evidence_at = prior.last_evidence_at
            if age > ttl:
                state = "STALE"
                change = f"No supporting evidence for {age} day(s), past the {ttl}-day freshness window for this finding type."
            else:
                state = "PENDING_VERIFICATION"
                change = f"No supporting evidence today ({age} day(s) since last observed); not yet treated as reduced risk."

    state_changed = prior is None or state != prior.state
    is_overdue = today_iso > deadline and state not in {"RESOLVED"}
    suppressed = (not state_changed) and severity in {"low", "medium"} and not is_overdue
    if state_changed:
        reason = f"state changed to {state}"
    elif is_overdue:
        reason = "deadline passed"
    else:
        reason = "severity requires continued visibility" if not suppressed else "no material change"

    return Item(
        item_id=item_id, rule_id=rule_id, title=f"{rule['title']}: {subject}", subject=subject,
        score=score, components=components, severity=severity, state=state, change=change,
        evidence=evidence, owner=context.owner, action=rule["action"],
        verification_method=rule["verification_method"], deadline=deadline,
        first_seen=first_seen, last_seen=today_iso,
        last_evidence_at=today_iso if satisfied or remediation_today else (prior.last_evidence_at if prior else today_iso),
        remediation=remediation, independent_sources=independent_sources, circular_reporting=circular,
        suppressed=suppressed, reportable_reason=reason,
        history=(prior.history if prior else []) + [{"day": today_iso, "state": state, "score": score, "severity": severity}],
    )


def correlate(signals_today: list[Signal], prior_items: dict[str, Item], today: date, asset_lookup: dict[str, AssetContext] | None = None) -> list[Item]:
    asset_lookup = asset_lookup or {}
    by_subject: dict[str, list[Signal]] = {}
    for signal in signals_today:
        by_subject.setdefault(signal.subject, []).append(signal)

    candidates: set[tuple[str, str]] = set()
    for subject in by_subject:
        for rule_id in RULES:
            candidates.add((rule_id, subject))
    for item_id in prior_items:
        rule_id, _, subject = item_id.partition(":")
        candidates.add((rule_id, subject))

    items: list[Item] = []
    for rule_id, subject in sorted(candidates):
        item = advance(
            rule_id, subject, today, by_subject.get(subject, []),
            prior_items.get(f"{rule_id}:{subject}"), asset_lookup.get(subject),
        )
        if item is not None:
            items.append(item)
    return sorted(items, key=lambda item: -item.score)
