from __future__ import annotations

from typing import Iterable, Dict, Any


def index_by_id(rows: Iterable[dict]) -> Dict[str, dict]:
    return {row.get("id", ""): row for row in rows if row.get("id")}


def diff_rows(previous: Iterable[dict], current: Iterable[dict]) -> dict:
    prev = index_by_id(previous)
    cur = index_by_id(current)

    added = [cur[k] for k in sorted(cur.keys() - prev.keys())]
    removed = [prev[k] for k in sorted(prev.keys() - cur.keys())]
    changed = []

    for key in sorted(prev.keys() & cur.keys()):
        before = prev[key]
        after = cur[key]
        changes: Dict[str, Any] = {}
        for field, before_value in before.items():
            after_value = after.get(field)
            if before_value != after_value:
                changes[field] = {"before": before_value, "after": after_value}
        if changes:
            changed.append({"id": key, "name_ja": after.get("name_ja", ""), "changes": changes})

    return {"added": added, "removed": removed, "changed": changed}
