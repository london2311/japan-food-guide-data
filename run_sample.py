from pathlib import Path

from collectors.base import read_json, write_csv, write_json
from collectors.diff import diff_rows
from collectors.sample_html_collector import collect_from_sample_html


def main() -> None:
    sample_html = Path("examples/hiroshima/sample_restaurants.html")
    output_dir = Path("data/hiroshima")
    output_json = output_dir / "restaurants.json"
    output_csv = output_dir / "restaurants.csv"
    diff_report = output_dir / "diff_report.json"

    previous_rows = read_json(output_json)
    restaurants = collect_from_sample_html(sample_html, source_url="sample")

    write_json(restaurants, output_json)
    write_csv(restaurants, output_csv)

    current_rows = [restaurant.normalized() for restaurant in restaurants]
    diff = diff_rows(previous_rows, current_rows)

    output_dir.mkdir(parents=True, exist_ok=True)
    diff_report.write_text(
        __import__("json").dumps(diff, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Collected {len(restaurants)} restaurants")
    print(f"Wrote {output_json}")
    print(f"Wrote {output_csv}")
    print(f"Wrote {diff_report}")


if __name__ == "__main__":
    main()
