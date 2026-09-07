"""Live-mode tests. No real network calls: collectors are exercised with
injected fake fetch functions so the suite stays fast, offline, and
deterministic."""

from __future__ import annotations

from pathlib import Path

from app.cti_briefing.collectors import fetch_cisa_kev, fetch_recent_high_severity_cves
from app.cti_briefing.live import build_live_signals
from app.cti_briefing.state_store import load_state, save_state


def _fake_kev(url: str) -> dict:
    return {
        "vulnerabilities": [
            {
                "cveID": "CVE-2024-0001", "vendorProject": "Apache", "product": "HTTP Server",
                "shortDescription": "Remote code execution.", "dateAdded": "2026-01-01",
                "dueDate": "2026-01-15",
            },
            {"cveID": "", "vendorProject": "Broken", "product": "Entry"},  # missing id, must be skipped
        ]
    }


def _fake_nvd(url: str) -> dict:
    return {
        "vulnerabilities": [
            {
                "cve": {
                    "id": "CVE-2024-0002",
                    "published": "2026-01-02T00:00:00.000",
                    "metrics": {"cvssMetricV31": [{"cvssData": {"baseScore": 8.5}}]},
                    "descriptions": [{"lang": "en", "value": "A high severity issue."}],
                }
            },
            {
                "cve": {
                    "id": "CVE-2024-0003",
                    "published": "2026-01-02T00:00:00.000",
                    "metrics": {"cvssMetricV31": [{"cvssData": {"baseScore": 4.0}}]},
                    "descriptions": [{"lang": "en", "value": "Below the CVSS floor, must be dropped."}],
                }
            },
        ]
    }


def test_fetch_cisa_kev_skips_entries_with_no_cve_id():
    signals = fetch_cisa_kev(fetch=_fake_kev)
    assert len(signals) == 1
    assert signals[0].subject == "CVE-2024-0001"
    assert signals[0].signal_type == "known_exploited_vulnerability"
    assert signals[0].source == "cisa_kev"


def test_fetch_recent_high_severity_cves_applies_the_cvss_floor():
    signals = fetch_recent_high_severity_cves(min_cvss=7.0, fetch=_fake_nvd)
    assert [s.subject for s in signals] == ["CVE-2024-0002"]
    assert signals[0].signal_type == "high_severity_vulnerability"


def test_build_live_signals_never_invents_reachability_for_unmatched_products():
    kev_signals = fetch_cisa_kev(fetch=_fake_kev)
    watchlist = {"organization_sector": "", "tracked_products": [{"match": "nginx", "owner": "x"}]}
    signals, asset_lookup = build_live_signals(kev_signals, watchlist)
    assert signals == kev_signals  # nothing matched "Apache HTTP Server" against "nginx"
    assert asset_lookup == {}


def test_build_live_signals_declares_reachability_only_for_matched_products():
    kev_signals = fetch_cisa_kev(fetch=_fake_kev)
    watchlist = {
        "organization_sector": "financial services",
        "tracked_products": [{"match": "apache", "owner": "Platform Engineering", "internet_exposure": True}],
    }
    signals, asset_lookup = build_live_signals(kev_signals, watchlist)
    types_added = {s.signal_type for s in signals} - {s.signal_type for s in kev_signals}
    assert types_added == {"environment_reachable", "sector_targeting"}
    assert all(s.source == "user_watchlist_config" for s in signals if s.signal_type in types_added)
    assert "CVE-2024-0001" in asset_lookup
    assert asset_lookup["CVE-2024-0001"].internet_exposure is True


def test_state_round_trips_through_disk(tmp_path: Path):
    from app.cti_briefing.engine import advance
    from app.cti_briefing.schema import Signal
    from datetime import date

    signal = Signal("multi_source_corroboration", "TEST-STATE", "src", "B", 0.7, "test", "2026-01-01", "2026-01-01")
    item = advance("CTI-004", "TEST-STATE", date(2026, 1, 1), [signal], None)

    state_path = tmp_path / "state.json"
    save_state(state_path, {item.item_id: item})
    reloaded = load_state(state_path)

    assert reloaded[item.item_id].state == "NEW"
    assert reloaded[item.item_id].evidence[0].statement == "test"


def test_load_state_returns_empty_dict_when_file_is_absent(tmp_path: Path):
    assert load_state(tmp_path / "does-not-exist.json") == {}
