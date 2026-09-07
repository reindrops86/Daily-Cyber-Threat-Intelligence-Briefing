"""Integration tests over the five-day synthetic demo scenario."""

from __future__ import annotations

from app.cti_briefing.engine import correlate
from app.cti_briefing.feedback import FeedbackLog, compute_trend
from app.cti_briefing.quality_gate import gate_passed, run_quality_gate
from app.cti_briefing.reports import render
from app.cti_briefing.schema import SYNTHETIC_BANNER, EvidenceRecord, Item, looks_unsafe, parse_date
from app.cti_briefing.simulate import ASSET_CONTEXT, RUN_DATES, demo_days, demo_feedback


def _run_all_days():
    state, daily_items = {}, []
    for day_str, signals in zip(RUN_DATES, demo_days()):
        items = correlate(signals, state, parse_date(day_str), ASSET_CONTEXT)
        state = {item.item_id: item for item in items}
        daily_items.append(items)
    return daily_items


def _by_id(items, item_id):
    return next(item for item in items if item.item_id == item_id)


def test_vulnerability_lifecycle_new_unchanged_mitigated_resolved_reopened():
    days = _run_all_days()
    states = [_by_id(day, "CTI-001:CVE-2099-00001-SYNTH").state for day in days]
    assert states == ["NEW", "UNCHANGED", "MITIGATED", "RESOLVED", "REOPENED"]


def test_dark_web_mention_expires_to_stale_and_never_resolves():
    days = _run_all_days()
    item_id = "CTI-003:example-financial-co (synthetic org)"
    states = [_by_id(day, item_id).state for day in days]
    assert "RESOLVED" not in states
    assert "MITIGATED" not in states
    assert states[-1] == "STALE"


def test_unremediated_vulnerability_never_auto_resolves_from_silence():
    days = _run_all_days()
    states = [_by_id(day, "CTI-005:CVE-2099-00002-SYNTH").state for day in days]
    assert "RESOLVED" not in states
    assert "MITIGATED" not in states
    assert states[-1] == "PENDING_VERIFICATION"


def test_suppressed_findings_reactivate_on_material_change():
    days = _run_all_days()
    ioc_id = "CTI-004:TESTNET-IOC-01 (203.0.113.77)"
    day4 = _by_id(days[3], ioc_id)
    day5 = _by_id(days[4], ioc_id)
    assert day4.suppressed is True
    assert day5.suppressed is False
    assert day5.state == "STALE"


def test_every_mitigated_or_resolved_item_carries_remediation_proof():
    for day in _run_all_days():
        for item in day:
            if item.state in {"MITIGATED", "RESOLVED"}:
                assert item.remediation


def test_reports_use_real_calendar_dates_not_placeholder_labels():
    days = _run_all_days()
    rendered = render(days[0], RUN_DATES[0], "2026-09-01 09:00 UTC", ["- placeholder"])
    assert RUN_DATES[0] in rendered["analyst"]
    assert "day-01" not in rendered["analyst"]


def test_every_report_carries_the_synthetic_banner():
    days = _run_all_days()
    rendered = render(days[-1], RUN_DATES[-1], "2026-09-05 09:00 UTC", ["- placeholder"])
    for text in rendered.values():
        assert SYNTHETIC_BANNER in text


def test_suppression_note_explains_reactivation():
    days = _run_all_days()
    rendered = render(days[-1], RUN_DATES[-1], "2026-09-05 09:00 UTC", ["- placeholder"])
    assert "reappears in the very next briefing" in rendered["executive"]


def test_quality_gate_passes_on_the_legitimate_demo_fixture():
    daily_items = _run_all_days()
    feedback_log = FeedbackLog()
    for item_id, day, label, analyst, note in demo_feedback():
        feedback_log.record(item_id, day, label, analyst, note)

    previous = None
    for count, (day_str, items) in enumerate(zip(RUN_DATES, daily_items), start=1):
        trend = compute_trend(daily_items[:count], RUN_DATES[:count], feedback_log)
        rendered = render(items, day_str, "2026-09-01 09:00 UTC", ["- placeholder"], trend)
        results = run_quality_gate(items, rendered, previous)
        assert gate_passed(results)
        previous = rendered


def test_quality_gate_rejects_a_resolved_item_with_no_remediation_proof():
    fabricated = Item(
        item_id="CTI-999:FAKE", rule_id="CTI-999", title="Fabricated resolved finding",
        subject="FAKE", score=10.0, components={"base": 10.0}, severity="low", state="RESOLVED",
        change="test", evidence=[EvidenceRecord("src", "B", 0.5, "stmt", "2026-01-01", "2026-01-01")],
        owner="nobody", action="n/a", verification_method="n/a", deadline="2026-01-01",
        first_seen="2026-01-01", last_seen="2026-01-01", last_evidence_at="2026-01-01",
        remediation=[],  # no proof, despite claiming RESOLVED
    )
    banner_only = {"analyst": SYNTHETIC_BANNER, "executive": SYNTHETIC_BANNER, "watchlist": SYNTHETIC_BANNER}
    results = run_quality_gate([fabricated], banner_only, None)
    assert not gate_passed(results)


def test_looks_unsafe_flags_real_looking_indicators_and_clears_reserved_ones():
    assert looks_unsafe("Malicious hosting at 8.8.8.8 acting as a c2 indicator.") is not None
    assert looks_unsafe("Malicious hosting at 203.0.113.5 acting as a c2 indicator.") is None
    assert looks_unsafe("Command and control domain evil-c2-domain.net observed.") is not None
    assert looks_unsafe("Command and control domain evil-c2-domain.example observed.") is None
