from __future__ import annotations

from pathlib import Path

from app.cti_briefing.core import correlate, demo_days, reconcile_resolved, render, summarize


def main() -> int:
    state: dict = {}
    history: list[dict] = []
    report_dir = Path(__file__).resolve().parent.parent / "reports"
    report_dir.mkdir(exist_ok=True)

    for day_index, signals in enumerate(demo_days(), start=1):
        day_label = f"day-{day_index:02d}"
        current = correlate(signals, state)
        current = reconcile_resolved(current, state)
        state = {item.item_id: item for item in current}

        summary = summarize(current)
        history.append({"day": day_label, **summary})

        for audience, content in render(current, day_label, history).items():
            (report_dir / f"{day_label}-{audience}.md").write_text(content, encoding="utf-8")
            (report_dir / f"latest-{audience}.md").write_text(content, encoding="utf-8")

    print(
        f"Generated {len(history) * 3} report artifacts across {len(history)} days. "
        f"Latest briefing: {history[-1]['reportable']} reported, "
        f"{history[-1]['critical']} critical, {history[-1]['suppressed']} suppressed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
