"""Synthetic five-day CTI feed.

Every actor id, CVE id, organization name, IP address, and domain here is
fabricated for this demo. CVE ids use the year 2099 and a "-SYNTH" suffix so
they cannot be mistaken for a real, assignable identifier. IP addresses are
drawn only from the IETF reserved TEST-NET ranges (RFC 5737): 192.0.2.0/24,
198.51.100.0/24, 203.0.113.0/24.
"""

from __future__ import annotations

from .schema import AssetContext, Signal

RUN_DATES = ["2026-09-01", "2026-09-02", "2026-09-03", "2026-09-04", "2026-09-05"]

ASSET_CONTEXT: dict[str, AssetContext] = {
    "CVE-2099-00001-SYNTH": AssetContext(
        owner="Platform Engineering (synthetic)", internet_exposure=True, production=True,
        data_sensitivity="crown_jewel", existing_controls=["WAF"], exploitability=0.9,
        operational_importance=1.2,
    ),
    "CVE-2099-00002-SYNTH": AssetContext(
        owner="API Platform Team (synthetic)", internet_exposure=True, production=True,
        data_sensitivity="high", existing_controls=["rate limiting"], exploitability=0.6,
        operational_importance=1.05,
    ),
    "FICTUS-ACTOR-07": AssetContext(
        owner="Detection and Response (synthetic)", internet_exposure=False, production=True,
        data_sensitivity="high", existing_controls=["EDR"], exploitability=0.7,
        operational_importance=1.1,
    ),
    "example-financial-co (synthetic org)": AssetContext(
        owner="CISO Office (synthetic)", internet_exposure=False, production=False,
        data_sensitivity="medium", existing_controls=[], exploitability=0.4,
        operational_importance=1.0,
    ),
    "TESTNET-IOC-01 (203.0.113.77)": AssetContext(
        owner="Network Security (synthetic)", internet_exposure=True, production=True,
        data_sensitivity="medium", existing_controls=["egress proxy"], exploitability=0.5,
        operational_importance=1.0,
    ),
    "TESTNET-IOC-02 (198.51.100.23)": AssetContext(
        owner="Network Security (synthetic)", internet_exposure=True, production=True,
        data_sensitivity="medium", existing_controls=["egress proxy"], exploitability=0.5,
        operational_importance=1.0,
    ),
}


def _s(signal_type, subject, source, reliability, confidence, detail, day, **kw) -> Signal:
    return Signal(signal_type, subject, source, reliability, confidence, detail, day, day, **kw)


def _day1(d: str) -> list[Signal]:
    return [
        _s("known_exploited_vulnerability", "CVE-2099-00001-SYNTH", "sca_scanner_synth", "B", 0.98,
           "Fictitious CVE flagged as KEV-listed in the synthetic feed, CVSS 9.6 (fixture).", d),
        _s("sector_targeting", "CVE-2099-00001-SYNTH", "vendor_advisory_synth", "B", 0.85,
           "Synthetic vendor advisory claims targeting of the financial sector (fixture).", d),
        _s("environment_reachable", "CVE-2099-00001-SYNTH", "asset_inventory_synth", "A", 0.95,
           "Synthetic asset inventory marks the affected service as internet-facing (fixture).", d),
        _s("actor_campaign_activity", "FICTUS-ACTOR-07", "commercial_feed_synth", "B", 0.80,
           "Synthetic feed reports campaign activity against peer organizations (fixture).", d),
        _s("dark_web_mention", "example-financial-co (synthetic org)", "darkweb_monitor_synth", "D", 0.55,
           "Synthetic forum post claims access to 'a mid-size bank'; unconfirmed (fixture).", d),
        _s("high_severity_vulnerability", "CVE-2099-00002-SYNTH", "sca_scanner_synth", "B", 0.90,
           "Synthetic CVE, CVSS 8.7, disclosed yesterday, no known exploitation (fixture).", d),
        _s("environment_reachable", "CVE-2099-00002-SYNTH", "asset_inventory_synth", "A", 0.90,
           "Synthetic asset inventory: affected library used by the public API gateway (fixture).", d),
    ]


def _day2(d: str) -> list[Signal]:
    return [
        _s("known_exploited_vulnerability", "CVE-2099-00001-SYNTH", "sca_scanner_synth", "B", 0.98,
           "Still KEV-listed in the synthetic feed; patch not yet deployed (fixture).", d),
        _s("sector_targeting", "CVE-2099-00001-SYNTH", "vendor_advisory_synth", "B", 0.85,
           "Synthetic vendor advisory: targeting confirmed continues (fixture).", d),
        _s("environment_reachable", "CVE-2099-00001-SYNTH", "asset_inventory_synth", "A", 0.95,
           "Synthetic asset inventory: affected service is still internet-facing (fixture).", d),
        _s("actor_campaign_activity", "FICTUS-ACTOR-07", "commercial_feed_synth", "B", 0.82,
           "Synthetic feed: campaign infrastructure expanded (fixture).", d),
        _s("internal_ioc_sighting", "FICTUS-ACTOR-07", "edr_telemetry_synth", "A", 0.90,
           "Synthetic EDR shows the actor's known C2 domain in outbound proxy logs (fixture).", d),
        _s("multi_source_corroboration", "TESTNET-IOC-01 (203.0.113.77)", "commercial_feed_synth", "B", 0.70,
           "Synthetic feed reports 203.0.113.77 (TEST-NET-3, reserved) as malicious hosting (fixture).", d),
        _s("multi_source_corroboration", "TESTNET-IOC-01 (203.0.113.77)", "isac_share_synth", "B", 0.75,
           "Synthetic ISAC share independently reports the same reserved address (fixture).", d),
        _s("multi_source_corroboration", "TESTNET-IOC-02 (198.51.100.23)", "feed_alpha_synth", "B", 0.70,
           "Synthetic feed Alpha reports 198.51.100.23 (TEST-NET-2, reserved) as malicious (fixture).", d,
           upstream_id="RPT-778-SYNTH"),
        _s("multi_source_corroboration", "TESTNET-IOC-02 (198.51.100.23)", "feed_beta_synth", "B", 0.65,
           "Synthetic feed Beta republishes upstream report RPT-778-SYNTH for the same reserved address (fixture).", d,
           upstream_id="RPT-778-SYNTH"),
    ]


def _day3(d: str) -> list[Signal]:
    return [
        _s("remediation_evidence", "CVE-2099-00001-SYNTH", "patch_mgmt_synth", "B", 0.80,
           "Synthetic change record: patch deployed to production (fixture, not yet independently verified).", d,
           remediation_kind="patch_deployed", remediation_verified=False),
        _s("actor_campaign_activity", "FICTUS-ACTOR-07", "commercial_feed_synth", "B", 0.82,
           "Synthetic feed: campaign infrastructure unchanged (fixture).", d),
        _s("internal_ioc_sighting", "FICTUS-ACTOR-07", "edr_telemetry_synth", "A", 0.97,
           "Synthetic EDR: stronger telemetry match against the actor's C2 fingerprint (fixture).", d),
    ]


def _day4(d: str) -> list[Signal]:
    return [
        _s("remediation_evidence", "CVE-2099-00001-SYNTH", "rescan_synth", "A", 0.95,
           "Synthetic re-scan confirms the vulnerability signature is no longer present (fixture).", d,
           remediation_kind="patch_deployed", remediation_verified=True),
        _s("actor_campaign_activity", "FICTUS-ACTOR-07", "commercial_feed_synth", "B", 0.82,
           "Synthetic feed: campaign infrastructure unchanged (fixture).", d),
        _s("internal_ioc_sighting", "FICTUS-ACTOR-07", "edr_telemetry_synth", "A", 0.97,
           "Synthetic EDR: same strong telemetry match continues (fixture).", d),
    ]


def _day5(d: str) -> list[Signal]:
    return [
        # A synthetic configuration rollback reintroduces the vulnerability.
        _s("known_exploited_vulnerability", "CVE-2099-00001-SYNTH", "sca_scanner_synth", "B", 0.98,
           "Synthetic re-scan: a configuration rollback reintroduced the vulnerable setting (fixture).", d),
        _s("sector_targeting", "CVE-2099-00001-SYNTH", "vendor_advisory_synth", "B", 0.85,
           "Synthetic vendor advisory: targeting still active (fixture).", d),
        _s("environment_reachable", "CVE-2099-00001-SYNTH", "asset_inventory_synth", "A", 0.95,
           "Synthetic asset inventory: affected service is internet-facing again (fixture).", d),
        _s("actor_campaign_activity", "FICTUS-ACTOR-07", "commercial_feed_synth", "B", 0.82,
           "Synthetic feed: campaign infrastructure unchanged (fixture).", d),
        _s("internal_ioc_sighting", "FICTUS-ACTOR-07", "edr_telemetry_synth", "A", 0.97,
           "Synthetic EDR: same strong telemetry match continues (fixture).", d),
    ]


def demo_days() -> list[list[Signal]]:
    builders = [_day1, _day2, _day3, _day4, _day5]
    return [builder(day) for builder, day in zip(builders, RUN_DATES)]


def demo_feedback() -> list[tuple[str, str, str, str, str]]:
    """(item_id, day, label, analyst, note) -- recorded for evaluation, not retraining."""
    return [
        ("CTI-003:example-financial-co (synthetic org)", RUN_DATES[0], "insufficient_evidence", "analyst.synthetic",
         "Single unconfirmed forum post; no internal corroboration."),
        ("CTI-002:FICTUS-ACTOR-07", RUN_DATES[1], "confirmed_incident", "analyst.synthetic",
         "EDR telemetry independently confirms the campaign."),
    ]
