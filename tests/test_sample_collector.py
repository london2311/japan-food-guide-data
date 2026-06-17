from pathlib import Path

from collectors.sample_html_collector import collect_from_sample_html


def test_collect_from_sample_html():
    sample_path = Path("examples/hiroshima/sample_restaurants.html")
    restaurants = collect_from_sample_html(sample_path)

    assert len(restaurants) == 2

    first = restaurants[0]
    assert first.name_ja == "広島お好み焼き ひろしま亭"
    assert first.genre == "Okonomiyaki"
    assert first.city == "Hiroshima"
    assert first.local_specialty == "Hiroshima-style okonomiyaki"

    second = restaurants[1]
    assert second.name_ja == "宮島あなごめし サンプル店"
    assert second.city == "Hatsukaichi"
    assert second.local_specialty == "Anago meshi"
