"""Tests for KEV + EPSS + CVSS patch priority, evidence labels, and PIRs.
All network access is replaced with injected fakes."""

from __future__ import annotations

from datetime import date

from app.cti_briefing.collectors import EPSS_URL, fetch_cvss_scores, fetch_epss_scores
from app.cti_briefing.engine import advance
from app.cti_briefing.live import collect_vuln_intel
from app.cti_briefing.reports import patch_priority, render
from app.cti_briefing.schema import Signal, evidence_class

TODAY = date(2026, 1, 5)


def _sig(signal_type, subject, source, detail="detail", reliability="A", confidence=0.9):
    return Signal(signal_type, subject, source, reliability, confidence, detail, "2026-01-05", "2026-01-05")


def _kev_item(cve="CVE-2026-0001"):
    signals = [
        _sig("known_exploited_vulnerability", cve, "cisa_kev", "CISA KEV catalog: Vendor Product."),
        _sig("sector_targeting", cve, "user_watchlist_config", "Sector declared.", "C", 0.6),
        _sig("environment_reachable", cve, "user_watchlist_config", "Declared reachable.", "B", 0.6),
    ]
    return advance("CTI-001", cve, TODAY, signals, None)


def _nvd_item(cve="CVE-2026-0002", cvss=9.8):
    signals = [
        _sig("high_severity_vulnerability", cve, "nvd", f"NVD: {cve}, CVSS {cvss}. Issue."),
        _sig("environment_reachable", cve, "user_watchlist_config", "Declared reachable.", "B", 0.6),
    ]
    return advance("CTI-005", cve, TODAY, signals, None)


def test_fetch_epss_scores_batches_and_rejects_malformed_ids():
    requested: list[str] = []

    def fake(url: str) -> dict:
        requested.append(url)
        return {"data": [
            {"cve": "CVE-2026-0001", "epss": "0.91234", "percentile": "0.998", "date": "2026-01-05"},
            {"cve": "CVE-2026-0002", "epss": "not-a-number", "percentile": "0.1"},
        ]}

    scores = fetch_epss_scores(["CVE-2026-0001", "CVE-2026-0002", "bad&id=1"], fetch=fake)
    assert requested == [f"{EPSS_URL}?cve=CVE-2026-0001,CVE-2026-0002"]
    assert scores == {"CVE-2026-0001": {"epss": 0.91234, "percentile": 0.998, "date": "2026-01-05"}}


def test_fetch_cvss_scores_paces_requests_and_skips_missing_metrics():
    pauses: list[float] = []

    def fake(url: str) -> dict:
        if url.endswith("CVE-2026-0001"):
            return {"vulnerabilities": [{"cve": {"metrics": {"cvssMetricV31": [{"cvssData": {"baseScore": 9.8}}]}}}]}
        return {"vulnerabilities": [{"cve": {"metrics": {}}}]}

    scores = fetch_cvss_scores(["CVE-2026-0002", "CVE-2026-0001"], fetch=fake, sleep=pauses.append)
    assert scores == {"CVE-2026-0001": 9.8}
    assert len(pauses) == 1


def test_patch_priority_tiers():
    assert patch_priority(True, 0.01, 5.0)[0].startswith("P1")
    assert patch_priority(False, 0.5, None)[0].startswith("P2")
    assert patch_priority(False, None, 9.8)[0].startswith("P2")
    assert patch_priority(False, 0.01, 7.5)[0].startswith("P3")
    assert patch_priority(False, None, None)[0].startswith("P3")


def test_collect_vuln_intel_only_looks_up_cvss_when_evidence_lacks_it():
    items = [_kev_item(), _nvd_item()]
    cvss_requested: list[str] = []

    def fake_cvss(cves):
        cvss_requested.extend(cves)
        return {cve: 7.5 for cve in cves}

    intel = collect_vuln_intel(
        items, [], epss_fetcher=lambda cves: {"CVE-2026-0001": {"epss": 0.4, "percentile": 0.97}},
        cvss_fetcher=fake_cvss,
    )
    assert cvss_requested == ["CVE-2026-0001"]
    assert intel["CVE-2026-0001"] == {"epss": 0.4, "percentile": 0.97, "cvss": 7.5}
    assert intel["CVE-2026-0002"] == {}


def test_render_shows_priority_table_evidence_labels_and_pir_coverage():
    items = [_kev_item(), _nvd_item()]
    intel = {"CVE-2026-0001": {"epss": 0.4, "percentile": 0.97, "cvss": 7.5}, "CVE-2026-0002": {}}
    pirs = [
        {"id": "PIR-001", "question": "Exploited and watched?", "rule_ids": ["CTI-001"]},
        {"id": "PIR-003", "question": "Actor active?", "rule_ids": ["CTI-002"]},
    ]
    rendered = render(items, "2026-01-05", "now", ["- x"], live=True, vuln_intel=intel, pirs=pirs)
    analyst, executive = rendered["analyst"], rendered["executive"]

    assert "| CVE-2026-0001 | P1 - patch now | yes | 0.400 (97%) | 7.5 |" in analyst
    assert "| CVE-2026-0002 | P2 - patch this cycle | no | n/a | 9.8 |" in analyst
    assert analyst.index("CVE-2026-0001 | P1") < analyst.index("CVE-2026-0002 | P2")
    assert "- **Reported fact:** [cisa_kev" in analyst
    assert "- **Analyst assessment:** [user_watchlist_config" in analyst
    assert "**Addresses:** PIR-001" in analyst
    assert "**PIR-003** Actor active? -- no new intelligence this cycle" in executive
    assert "**PIR-001** Exploited and watched? -- 1 reportable finding(s)" in executive


def test_render_without_vuln_intel_omits_priority_section():
    rendered = render([_kev_item()], "2026-01-05", "now", ["- x"])
    assert "Vulnerability Patch Priority" not in rendered["analyst"]
    assert "Priority Intelligence Requirements" not in rendered["executive"]


def test_evidence_class_labels():
    assert evidence_class("cisa_kev") == "Reported fact"
    assert evidence_class("threat-ingest-censys") == "Automated inference"
    assert evidence_class("user_watchlist_config") == "Analyst assessment"
    assert evidence_class("edr_telemetry_synth") == "Observed telemetry"
    assert evidence_class("commercial_feed_synth") == "Third-party report"
    assert evidence_class("something_else") == "Unclassified source"
