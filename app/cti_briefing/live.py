"""Orchestrates a live daily run against real, public threat data.

What is genuinely live: vulnerability existence and severity, from the CISA
KEV catalog and the NVD API. What is self-declared: whether a given product
is in your environment and whether your sector is targeted -- only the
analyst editing config/watchlist.json can know that, so it is never invented
here. What is unavailable: actor campaigns, dark-web mentions, and
corroborated indicators, unless supplied via data/manual_signals.json.
"""

from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path
from typing import Any

from .collectors import CollectionError, fetch_cisa_kev, fetch_recent_high_severity_cves
from .engine import correlate
from .quality_gate import gate_passed, render_gate_summary, run_quality_gate
from .reports import render
from .schema import AssetContext, DEFAULT_ASSET_CONTEXT, Signal
from .state_store import load_state, save_state

ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_WATCHLIST = ROOT / "config" / "watchlist.json"
DEFAULT_MANUAL_SIGNALS = ROOT / "data" / "manual_signals.json"
DEFAULT_STATE = ROOT / "data" / "state.json"
DEFAULT_REPORT_DIR = ROOT / "reports"


def _load_watchlist(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"organization_sector": "", "tracked_products": []}
    return json.loads(path.read_text(encoding="utf-8"))


def _load_manual_signals(path: Path) -> list[Signal]:
    if not path.exists():
        return []
    raw = json.loads(path.read_text(encoding="utf-8"))
    return [Signal(**entry) for entry in raw]


def _within_lookback(signal: Signal, today: date, lookback_days: int) -> bool:
    from .schema import parse_date
    return (today - parse_date(signal.observed_at)).days <= lookback_days


def _match_product(detail: str, tracked_products: list[dict[str, Any]]) -> dict[str, Any] | None:
    lowered = detail.lower()
    for product in tracked_products:
        if product.get("match", "").lower() in lowered:
            return product
    return None


def _asset_context_for(product: dict[str, Any]) -> AssetContext:
    return AssetContext(
        owner=product.get("owner", DEFAULT_ASSET_CONTEXT.owner),
        internet_exposure=bool(product.get("internet_exposure", False)),
        production=bool(product.get("production", False)),
        data_sensitivity=product.get("data_sensitivity", "medium"),
        existing_controls=product.get("existing_controls", []),
        exploitability=float(product.get("exploitability", 0.5)),
        operational_importance=float(product.get("operational_importance", 1.0)),
    )


def build_live_signals(
    vuln_signals: list[Signal], watchlist: dict[str, Any],
) -> tuple[list[Signal], dict[str, AssetContext]]:
    """Cross-reference real vulnerability signals against the analyst's
    self-declared environment; never invent reachability or targeting."""
    sector = watchlist.get("organization_sector", "")
    tracked = watchlist.get("tracked_products", [])
    today = date.today().isoformat()

    signals: list[Signal] = list(vuln_signals)
    asset_lookup: dict[str, AssetContext] = {}

    for signal in vuln_signals:
        product = _match_product(signal.detail, tracked)
        if product is None:
            continue
        asset_lookup[signal.subject] = _asset_context_for(product)
        signals.append(Signal(
            signal_type="environment_reachable", subject=signal.subject,
            source="user_watchlist_config", source_reliability="B", confidence=0.6,
            detail=(
                f"Declared reachable per config/watchlist.json (matched '{product.get('match')}'). "
                "Edit that file to reflect your real environment."
            ),
            observed_at=today, collected_at=today,
        ))
        if sector:
            signals.append(Signal(
                signal_type="sector_targeting", subject=signal.subject,
                source="user_watchlist_config", source_reliability="C", confidence=0.6,
                detail=(
                    f"Organization sector declared as '{sector}' in config/watchlist.json; "
                    "this is a self-declared business fact, not independently corroborated."
                ),
                observed_at=today, collected_at=today,
            ))
    return signals, asset_lookup


def run(
    report_dir: Path = DEFAULT_REPORT_DIR, state_path: Path = DEFAULT_STATE,
    watchlist_path: Path = DEFAULT_WATCHLIST, manual_signals_path: Path = DEFAULT_MANUAL_SIGNALS,
) -> int:
    report_dir.mkdir(exist_ok=True)
    today = date.today()
    today_iso = today.isoformat()

    collection_notes: list[str] = []
    vuln_signals: list[Signal] = []
    try:
        vuln_signals += fetch_cisa_kev()
    except CollectionError as exc:
        collection_notes.append(f"CISA KEV unavailable this run: {exc}")
    try:
        vuln_signals += fetch_recent_high_severity_cves()
    except CollectionError as exc:
        collection_notes.append(f"NVD unavailable this run: {exc}")

    watchlist = _load_watchlist(watchlist_path)
    lookback_days = int(watchlist.get("kev_lookback_days", 30))
    vuln_signals = [s for s in vuln_signals if _within_lookback(s, today, lookback_days)]

    live_signals, asset_lookup = build_live_signals(vuln_signals, watchlist)
    live_signals += _load_manual_signals(manual_signals_path)

    prior_state = load_state(state_path)
    items = correlate(live_signals, prior_state, today, asset_lookup)
    save_state(state_path, {item.item_id: item for item in items})

    history_lines = [f"- {today_iso}: {sum(1 for i in items if not i.suppressed)} reported, "
                      f"{sum(1 for i in items if i.severity == 'critical' and not i.suppressed)} critical, "
                      f"{sum(1 for i in items if i.suppressed)} suppressed"]
    if collection_notes:
        history_lines += [f"  (note: {note})" for note in collection_notes]

    generated_at = today.isoformat()
    rendered = render(items, today_iso, generated_at, history_lines, live=True)
    gate_results = run_quality_gate(items, rendered, None, live=True)
    gate_summary = render_gate_summary(gate_results)

    for audience, content in rendered.items():
        (report_dir / f"live-{audience}.md").write_text(content, encoding="utf-8")
    (report_dir / "live-quality-gate.md").write_text(gate_summary, encoding="utf-8")

    print(f"Live briefing generated for {today_iso}: {sum(1 for i in items if not i.suppressed)} reportable finding(s).")
    for note in collection_notes:
        print(f"  WARNING: {note}")
    if not watchlist.get("tracked_products"):
        print("  NOTE: config/watchlist.json has no tracked_products yet; edit it to see correlated findings.")

    return 0 if gate_passed(gate_results) else 1
