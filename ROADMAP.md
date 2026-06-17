from pathlib import Path

from collectors.sample_html_collector import collect_from_sample_html


def test_collect_from_sample_html():
    root = Path(__file__).resolve().parents[1]
    restaurants = collect_from_sample_html(root / "examples" / "hiroshima" / "sample_restaurants.html")
    assert len(restaurants) == 2
    assert restaurants[0].name_ja == "お好み焼き ひろしま庵"
    assert restaurants[0].local_specialty == "Hiroshima-style okonomiyaki"
