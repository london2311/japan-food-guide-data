from __future__ import annotations

import hashlib
from pathlib import Path
from typing import List
from bs4 import BeautifulSoup

from .base import Restaurant


def stable_id(name_ja: str, address: str = "") -> str:
    key = f"{name_ja}|{address}".encode("utf-8")
    return hashlib.sha1(key).hexdigest()[:12]


def text_or_empty(element) -> str:
    if element is None:
        return ""
    return " ".join(element.get_text(" ", strip=True).split())


def collect_from_sample_html(path: str | Path, source_url: str = "sample") -> List[Restaurant]:
    """Collect restaurant data from the bundled sample HTML.

    The sample HTML uses simple cards with data-field attributes.
    Real collectors can subclass this idea for specific official/tourism pages.
    """
    html = Path(path).read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "lxml")
    restaurants: List[Restaurant] = []

    for card in soup.select(".restaurant-card"):
        get = lambda field: text_or_empty(card.select_one(f'[data-field="{field}"]'))
        name_ja = get("name_ja")
        address = get("address")
        if not name_ja:
            continue

        restaurants.append(
            Restaurant(
                id=stable_id(name_ja, address),
                name_ja=name_ja,
                name_en=get("name_en"),
                area=get("area"),
                city=get("city"),
                address=address,
                genre=get("genre"),
                tags=get("tags"),
                official_url=get("official_url"),
                reservation_url=get("reservation_url"),
                opening_hours=get("opening_hours"),
                closed_days=get("closed_days"),
                price_lunch=get("price_lunch"),
                price_dinner=get("price_dinner"),
                cashless=get("cashless"),
                english_menu=get("english_menu"),
                vegetarian_friendly=get("vegetarian_friendly"),
                halal_friendly=get("halal_friendly"),
                solo_friendly=get("solo_friendly"),
                family_friendly=get("family_friendly"),
                nearest_station=get("nearest_station"),
                local_specialty=get("local_specialty"),
                source_url=source_url,
                notes=get("notes"),
            )
        )

    return restaurants
