from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from app.cti_briefing.engine import correlate
from app.cti_briefing.feedback import FeedbackLog, compute_trend
from app.cti_briefing.quality_gate import gate_passed, render_gate_summary, run_quality_gate
from app.cti_briefing.reports import render
from app.cti_briefing.schema import parse_date
from app.cti_briefing.simulate import ASSET_CONTEXT, RUN_DATES, demo_days, demo_feedback


def main() -> int:
    report_dir = Path(__file__).resolve().parent.parent / "reports"
    report_dir.mkdir(exist_ok=True)

    feedback_log = FeedbackLog()
    for item_id, day, label, analyst, note in demo_feedback():
        feedback_log.record(item_id, day, label, analyst, note)

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    state: dict = {}
    daily_items: list = []
    history_lines: list[str] = []
    previous_rendered = None

    for day_str, signals in zip(RUN_DATES, demo_days()):
        today = parse_date(day_str)
        items = correlate(signals, state, today, ASSET_CONTEXT)
        state = {item.item_id: item for item in items}
        daily_items.append(items)

        reportable = [item for item in items if not item.suppressed]
        history_lines.append(
            f"- {day_str}: {len(reportable)} reported, "
            f"{sum(1 for item in reportable if item.severity == 'critical')} critical, "
            f"{sum(1 for item in items if item.suppressed)} suppressed"
        )

        trend = compute_trend(daily_items, RUN_DATES[: len(daily_items)], feedback_log)
        rendered = render(items, day_str, generated_at, list(history_lines), trend)

        gate_results = run_quality_gate(items, rendered, previous_rendered)
        gate_summary = render_gate_summary(gate_results)
        (report_dir / f"{day_str}-quality-gate.md").write_text(gate_summary, encoding="utf-8")

        for audience, content in rendered.items():
            (report_dir / f"{day_str}-{audience}.md").write_text(content, encoding="utf-8")

        if gate_passed(gate_results):
            for audience, content in rendered.items():
                (report_dir / f"latest-{audience}.md").write_text(content, encoding="utf-8")
            (report_dir / "latest-quality-gate.md").write_text(gate_summary, encoding="utf-8")
        else:
            print(f"Quality gate failed on {day_str}; latest-*.md not updated. See {day_str}-quality-gate.md")

        previous_rendered = rendered

    final_trend = compute_trend(daily_items, RUN_DATES, feedback_log)
    final_reportable = [item for item in daily_items[-1] if not item.suppressed]
    print(
        f"Generated reports for {len(RUN_DATES)} day(s). Latest briefing ({RUN_DATES[-1]}): "
        f"{len(final_reportable)} reported, reopened total {final_trend['reopened_total']}, "
        f"tracked findings total {final_trend['tracked_findings_total']}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

