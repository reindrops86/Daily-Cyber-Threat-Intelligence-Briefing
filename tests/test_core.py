from app.cti_briefing.core import correlate, demo_days, reconcile_resolved, render, summarize


def _run_all_days():
    state = {}
    history = []
    all_days = []
    for index, signals in enumerate(demo_days(), start=1):
        current = correlate(signals, state)
        current = reconcile_resolved(current, state)
        state = {item.item_id: item for item in current}
        history.append({"day": f"day-{index:02d}", **summarize(current)})
        all_days.append(current)
    return all_days, history, state


def test_all_five_cti_detections_fire_across_the_three_day_feed():
    all_days, _, _ = _run_all_days()
    rule_ids = {item.rule_id for day in all_days for item in day}
    assert rule_ids == {"CTI-001", "CTI-002", "CTI-003", "CTI-004", "CTI-005"}


def test_exploited_vulnerability_targeting_sector_is_critical():
    all_days, _, _ = _run_all_days()
    day1 = {item.item_id: item for item in all_days[0]}
    assert day1["CTI-001:CVE-2026-41821"].severity == "critical"
    assert day1["CTI-001:CVE-2026-41821"].state == "new"


def test_actor_campaign_confirmed_by_telemetry_is_never_suppressed_while_active():
    all_days, _, _ = _run_all_days()
    day2 = {item.item_id: item for item in all_days[1]}
    day3 = {item.item_id: item for item in all_days[2]}
    assert day2["CTI-002:UNC-4471"].severity in {"high", "critical"}
    assert day3["CTI-002:UNC-4471"].state == "unchanged"
    assert day3["CTI-002:UNC-4471"].suppressed is False


def test_patched_vulnerability_resolves_and_is_never_silently_dropped():
    all_days, _, _ = _run_all_days()
    day3 = {item.item_id: item for item in all_days[2]}
    resolved = day3["CTI-001:CVE-2026-41821"]
    assert resolved.state == "resolved"
    assert resolved.suppressed is False


def test_low_confidence_dark_web_mention_resolves_when_not_corroborated():
    all_days, _, _ = _run_all_days()
    day1 = {item.item_id: item for item in all_days[0]}
    day2 = {item.item_id: item for item in all_days[1]}
    assert day1["CTI-003:acme-corp"].severity == "low"
    assert day2["CTI-003:acme-corp"].state == "resolved"


def test_reports_share_the_same_evidence_and_state():
    all_days, history, _ = _run_all_days()
    rendered = render(all_days[-1], "day-03", history)
    assert set(rendered) == {"analyst", "executive", "watchlist"}
    assert "CTI-002:UNC-4471" in rendered["analyst"]
    assert "Resolved Since Last Briefing" in rendered["executive"]
    assert "CTI-001:CVE-2026-41821" in rendered["watchlist"]


def test_unchanged_low_or_medium_items_are_suppressed_but_counted():
    all_days, _, _ = _run_all_days()
    day3 = all_days[2]
    suppressed = [item for item in day3 if item.suppressed]
    reportable = [item for item in day3 if not item.suppressed]
    assert suppressed
    assert len(suppressed) + len(reportable) == len(day3)
