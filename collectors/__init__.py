from __future__ import annotations

import json
from pathlib import Path

from collectors.base import write_csv, write_json, read_json
from collectors.diff import diff_rows
from collectors.sample_html_collector import collect_from_sample_html

ROOT = Path(__file__).resolve().parent
SAMPLE_HTML = ROOT / "examples" / "hiroshima" / "sample_restaurants.html"
OUTPUT_JSON = ROOT / "data" / "hiroshima" / "restaurants.json"
OUTPUT_CSV = ROOT / "data" / "hiroshima" / "restaurants.csv"
DIFF_REPORT = ROOT / "data" / "hiroshima" / "diff_report.json"


def main() -> None:
    previous_rows = read_json(OUTPUT_JSON)
    restaurants = collect_from_sample_html(SAMPLE_HTML, source_url="examples/hiroshima/sample_restaurants.html")
    current_rows = [r.normalized() for r in restaurants]

    write_csv(restaurants, OUTPUT_CSV)
    write_json(restaurants, OUTPUT_JSON)

    report = diff_rows(previous_rows, current_rows)
    DIFF_REPORT.parent.mkdir(parents=True, exist_ok=True)
    DIFF_REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Collected {len(restaurants)} restaurants")
    print(f"CSV: {OUTPUT_CSV}")
    print(f"JSON: {OUTPUT_JSON}")
    print(f"Diff: {DIFF_REPORT}")


if __name__ == "__main__":
    main()
