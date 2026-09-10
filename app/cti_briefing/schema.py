"""Data model for the daily CTI briefing engine.

Every fixture in this package (actors, CVEs, organizations, IPs, domains, and
telemetry) is synthetic. See SYNTHETIC_BANNER for the text embedded in every
generated report.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Any

SYNTHETIC_BANNER = (
    "SYNTHETIC DATA ONLY: every actor, CVE, organization, IP address, domain, "
    "and telemetry event in this report is fabricated for demonstration. None "
    "of it corresponds to a real vulnerability, incident, or indicator. Do not "
    "action any value in this report against real infrastructure."
)

LIVE_BANNER = (
    "LIVE DATA: vulnerability existence, exploitation status, and severity are "
    "sourced from the public CISA KEV catalog and the NVD API. Sector "
    "relevance and environment reachability are self-declared by the analyst "
    "in config/watchlist.json and are not independently verified -- edit that "
    "file to match your real environment before relying on this report. "
    "Actor-campaign, dark-web, and corroborated-indicator findings do not "
    "appear here unless supplied via data/manual_signals.json; this project "
    "has no live source for those signal types."
)

# Reserved, non-routable ranges (RFC 5737 / RFC 2606) so no fixture can be
# mistaken for a real indicator worth blocking.
SAFE_IP_PREFIXES = ("192.0.2.", "198.51.100.", "203.0.113.")
SAFE_DOMAIN_SUFFIXES = (".example", ".test", ".invalid", ".localhost")

STATES = (
    "NEW", "ACTIVE", "UNCHANGED", "PENDING_VERIFICATION", "STALE",
    "MITIGATED", "RESOLVED", "REOPENED",
)

# States in which an item is considered closed enough that reappearing
# evidence must be flagged as a reopening rather than routine persistence.
CLOSED_OR_AGED_STATES = {"STALE", "MITIGATED", "RESOLVED"}

SEVERITY_BANDS = ((70.0, "critical"), (50.0, "high"), (30.0, "medium"), (0.0, "low"))
SLA_DAYS = {"critical": 2, "high": 7, "medium": 14, "low": 30}

# Time-to-live per signal type: how many days a signal keeps corroborating a
# finding after its own observation date before it stops counting as current
# evidence. IP-type indicators decay fastest; vulnerability facts persist
# until remediation evidence says otherwise (a very long TTL, not "forever",
# so the schema never has to special-case "no expiry").
SIGNAL_TTL_DAYS = {
    "multi_source_corroboration": 2,
    "internal_ioc_sighting": 3,
    "actor_campaign_activity": 21,
    "known_exploited_vulnerability": 3650,
    "high_severity_vulnerability": 3650,
    "sector_targeting": 30,
    "environment_reachable": 3650,
    "dark_web_mention": 1,
}
DEFAULT_SIGNAL_TTL_DAYS = 7

REMEDIATION_KINDS = {"patch_deployed", "credential_revoked", "exposure_removed", "incident_closed"}

FEEDBACK_LABELS = {
    "useful", "duplicate", "false_positive", "insufficient_evidence",
    "accepted_risk", "confirmed_incident",
}


def parse_date(value: str) -> date:
    return date.fromisoformat(value)


@dataclass(frozen=True)
class Signal:
    """One atomic piece of intelligence, with its own provenance and TTL."""

    signal_type: str
    subject: str
    source: str
    source_reliability: str  # Admiralty-style A (fully reliable) .. F (cannot be judged)
    confidence: float        # 0-1: collector's confidence in this specific signal
    detail: str
    observed_at: str         # ISO date the underlying activity/fact occurred
    collected_at: str        # ISO date this system ingested it
    upstream_id: str | None = None  # shared id => signals are not independent sources
    remediation_kind: str | None = None
    remediation_verified: bool = False
    source_url: str | None = None

    def ttl_days(self) -> int:
        return SIGNAL_TTL_DAYS.get(self.signal_type, DEFAULT_SIGNAL_TTL_DAYS)

    def expired_on(self, as_of: date) -> bool:
        return (as_of - parse_date(self.observed_at)).days > self.ttl_days()


@dataclass
class EvidenceRecord:
    source: str
    source_reliability: str
    confidence: float
    statement: str
    first_observed: str
    last_observed: str
    supports: bool = True
    collected_at: str | None = None
    source_url: str | None = None

    def line(self) -> str:
        stance = "supports" if self.supports else "contradicts"
        provenance = [
            f"source date {self.first_observed}",
            f"collected {self.collected_at}" if self.collected_at else "",
            f"[original source]({self.source_url})" if self.source_url else "",
        ]
        return (
            f"[{self.source}, reliability {self.source_reliability}, "
            f"confidence {self.confidence:.2f}, {stance}] {self.statement} "
            f"(first seen {self.first_observed}, last seen {self.last_observed}; "
            f"{'; '.join(part for part in provenance if part)})"
        )


@dataclass
class AssetContext:
    owner: str
    internet_exposure: bool
    production: bool
    data_sensitivity: str  # low | medium | high | crown_jewel
    existing_controls: list[str]
    exploitability: float  # 0-1, independent of any single CVE's CVSS
    operational_importance: float  # multiplier, typically 0.85-1.3


DEFAULT_ASSET_CONTEXT = AssetContext(
    owner="Unassigned (synthetic)", internet_exposure=False, production=False,
    data_sensitivity="medium", existing_controls=[], exploitability=0.5,
    operational_importance=1.0,
)

_CRITICALITY_WEIGHT = {"low": 0.9, "medium": 1.0, "high": 1.15, "crown_jewel": 1.3}


def asset_multiplier(context: AssetContext) -> float:
    weight = _CRITICALITY_WEIGHT.get(context.data_sensitivity, 1.0)
    weight *= context.operational_importance
    if context.internet_exposure:
        weight *= 1.1
    if context.production:
        weight *= 1.05
    return round(weight, 3)


@dataclass
class Item:
    item_id: str
    rule_id: str
    title: str
    subject: str
    score: float
    components: dict[str, float]
    severity: str
    state: str
    change: str
    evidence: list[EvidenceRecord]
    owner: str
    action: str
    verification_method: str
    deadline: str
    first_seen: str
    last_seen: str
    last_evidence_at: str
    remediation: list[str] = field(default_factory=list)
    independent_sources: int = 1
    circular_reporting: bool = False
    suppressed: bool = False
    reportable_reason: str = ""
    history: list[dict[str, Any]] = field(default_factory=list)


def severity_for(score: float) -> str:
    for floor, label in SEVERITY_BANDS:
        if score >= floor:
            return label
    return "low"


def deadline_from(first_seen: str, severity: str) -> str:
    return (parse_date(first_seen) + timedelta(days=SLA_DAYS.get(severity, 14))).isoformat()


def looks_unsafe(text: str) -> str | None:
    """Return a reason string if text contains an indicator outside reserved,
    non-routable ranges -- the thing a quality gate must never let through."""
    import re

    for match in re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", text):
        if not match.startswith(SAFE_IP_PREFIXES):
            return f"IP address {match} is not in a reserved TEST-NET range"
    for match in re.findall(r"\b[a-z0-9.-]+\.[a-z]{2,}\b", text.lower()):
        if match.endswith(SAFE_DOMAIN_SUFFIXES):
            continue
        if match in {"cve.mitre.org", "nvd.nist.gov"}:  # documentation references, not indicators
            continue
        # Only flag tokens that read like a hostname/indicator context word nearby;
        # kept intentionally strict for this synthetic-only demo.
        if any(hint in text.lower() for hint in ("domain", "hostname", "c2", "indicator")):
            return f"possible non-reserved domain '{match}' referenced as an indicator"
    return None
