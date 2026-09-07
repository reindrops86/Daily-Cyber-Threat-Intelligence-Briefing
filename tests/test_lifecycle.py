"""Unit tests for the finding lifecycle state machine.

These call engine.advance() directly with hand-built signals so every
transition is exercised in isolation from the demo narrative.
"""

from __future__ import annotations

from datetime import date, timedelta

from app.cti_briefing.engine import advance
from app.cti_briefing.schema import Signal


def _sig(signal_type, subject, day, confidence=0.8, source="test_source", **kw):
    return Signal(signal_type, subject, source, "B", confidence, "Synthetic test evidence (fixture).", day, day, **kw)


def test_missing_evidence_alone_never_produces_resolved():
    """The central bug this engine exists to prevent."""
    subject = "TEST-SUBJECT-A"
    day1 = date(2026, 1, 1)
    item = advance("CTI-004", subject, day1, [_sig("multi_source_corroboration", subject, "2026-01-01")], None)
    assert item.state == "NEW"

    # Signal never reappears, for a very long time. It must age to STALE, never RESOLVED.
    for offset in range(2, 40):
        day = day1 + timedelta(days=offset)
        item = advance("CTI-004", subject, day, [], item)
        assert item.state != "RESOLVED"
    assert item.state == "STALE"


def test_full_lifecycle_active_stale_mitigated_resolved_reopened():
    subject = "TEST-SUBJECT-B"

    new_item = advance("CTI-004", subject, date(2026, 1, 1),
                        [_sig("multi_source_corroboration", subject, "2026-01-01", confidence=0.7)], None)
    assert new_item.state == "NEW"

    active_item = advance("CTI-004", subject, date(2026, 1, 2),
                           [_sig("multi_source_corroboration", subject, "2026-01-02", confidence=0.99)], new_item)
    assert active_item.state == "ACTIVE"

    # Gap far beyond CTI-004's 2-day TTL, with no remediation evidence at all.
    stale_item = advance("CTI-004", subject, date(2026, 1, 8), [], active_item)
    assert stale_item.state == "STALE"

    mitigated_item = advance(
        "CTI-004", subject, date(2026, 1, 9),
        [_sig("remediation_evidence", subject, "2026-01-09", remediation_kind="exposure_removed", remediation_verified=False)],
        stale_item,
    )
    assert mitigated_item.state == "MITIGATED"
    assert mitigated_item.remediation

    resolved_item = advance(
        "CTI-004", subject, date(2026, 1, 10),
        [_sig("remediation_evidence", subject, "2026-01-10", remediation_kind="exposure_removed", remediation_verified=True)],
        mitigated_item,
    )
    assert resolved_item.state == "RESOLVED"

    reopened_item = advance(
        "CTI-004", subject, date(2026, 1, 11),
        [_sig("multi_source_corroboration", subject, "2026-01-11", confidence=0.8)],
        resolved_item,
    )
    assert reopened_item.state == "REOPENED"
    assert "resolved" in reopened_item.change.lower()


def test_unverified_remediation_does_not_jump_straight_to_resolved():
    subject = "TEST-SUBJECT-C"
    item = advance("CTI-004", subject, date(2026, 1, 1),
                    [_sig("multi_source_corroboration", subject, "2026-01-01")], None)
    mitigated = advance(
        "CTI-004", subject, date(2026, 1, 2),
        [_sig("remediation_evidence", subject, "2026-01-02", remediation_kind="patch_deployed", remediation_verified=False)],
        item,
    )
    assert mitigated.state == "MITIGATED"
    assert mitigated.state != "RESOLVED"


def test_pending_verification_stays_within_ttl_and_expires_past_it():
    subject = "TEST-SUBJECT-D"
    item = advance("CTI-004", subject, date(2026, 1, 1),
                    [_sig("multi_source_corroboration", subject, "2026-01-01")], None)
    # CTI-004's required-signal TTL is 2 days: day+2 is still within the window.
    still_pending = advance("CTI-004", subject, date(2026, 1, 3), [], item)
    assert still_pending.state == "PENDING_VERIFICATION"
    now_stale = advance("CTI-004", subject, date(2026, 1, 4), [], still_pending)
    assert now_stale.state == "STALE"


def test_circular_reporting_collapses_shared_upstream_sources():
    subject = "TEST-SUBJECT-E"
    shared = [
        _sig("multi_source_corroboration", subject, "2026-01-01", confidence=0.7, source="feed_alpha_synth", upstream_id="RPT-1"),
        _sig("multi_source_corroboration", subject, "2026-01-01", confidence=0.6, source="feed_beta_synth", upstream_id="RPT-1"),
    ]
    item = advance("CTI-004", subject, date(2026, 1, 1), shared, None)
    assert item.circular_reporting is True
    assert item.independent_sources == 1


def test_independent_sources_are_not_collapsed():
    subject = "TEST-SUBJECT-F"
    independent = [
        _sig("multi_source_corroboration", subject, "2026-01-01", confidence=0.7),
        _sig("multi_source_corroboration", subject, "2026-01-01", confidence=0.75),
    ]
    item = advance("CTI-004", subject, date(2026, 1, 1), independent, None)
    assert item.circular_reporting is False
    assert item.independent_sources == 2
