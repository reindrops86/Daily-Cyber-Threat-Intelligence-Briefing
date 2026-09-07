"""Persist finding state as JSON between separate process runs.

A demo run replays a whole multi-day scenario in one process, so it can keep
state in memory. A live daily run is a fresh process each day (a new GitHub
Actions job), so lifecycle state -- what was NEW yesterday, what is still
PENDING_VERIFICATION, what deadline is already set -- has to be written to
disk and reloaded, or every day would look like day one again.
"""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from .schema import EvidenceRecord, Item


def save_state(path: Path, items: dict[str, Item]) -> None:
    payload = {item_id: asdict(item) for item_id, item in items.items()}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def load_state(path: Path) -> dict[str, Item]:
    if not path.exists():
        return {}
    raw = json.loads(path.read_text(encoding="utf-8"))
    items: dict[str, Item] = {}
    for item_id, data in raw.items():
        data = dict(data)
        evidence = [EvidenceRecord(**record) for record in data.pop("evidence", [])]
        items[item_id] = Item(evidence=evidence, **data)
    return items
