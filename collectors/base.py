from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import date
from typing import Iterable, List
import csv
import json
from pathlib import Path


@dataclass
class Restaurant:
    id: str
    name_ja: str
    name_en: str = ""
    area: str = ""
    city: str = ""
    address: str = ""
    genre: str = ""
    tags: str = ""
    official_url: str = ""
    reservation_url: str = ""
    opening_hours: str = ""
    closed_days: str = ""
    price_lunch: str = ""
    price_dinner: str = ""
    cashless: str = ""
    english_menu: str = ""
    vegetarian_friendly: str = ""
    halal_friendly: str = ""
    solo_friendly: str = ""
    family_friendly: str = ""
    nearest_station: str = ""
    local_specialty: str = ""
    source_url: str = ""
    last_checked: str = ""
    notes: str = ""

    def normalized(self) -> dict:
        data = asdict(self)
        if not data["last_checked"]:
            data["last_checked"] = date.today().isoformat()
        return data


FIELDNAMES = list(Restaurant(id="", name_ja="").normalized().keys())


def write_csv(restaurants: Iterable[Restaurant], output_path: str | Path) -> None:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    rows = [r.normalized() for r in restaurants]
    with output_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def write_json(restaurants: Iterable[Restaurant], output_path: str | Path) -> None:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    rows = [r.normalized() for r in restaurants]
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)


def read_json(path: str | Path) -> List[dict]:
    path = Path(path)
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)
