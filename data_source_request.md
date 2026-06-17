# Japan Food Guide Data

**Japan Food Guide Data** is an open-source toolkit for collecting, structuring, and continuously updating public restaurant information in Japan for international travelers.

日本を訪れる旅行者向けに、日本語の店舗公式サイト・観光協会・自治体ページ・商店街ページなどに散らばる飲食店情報を、CSV/JSONとして整理・更新するためのオープンソース・ツールキットです。

## Why this project exists

Many local restaurants in Japan publish important information only in Japanese and often across small official websites, tourism association pages, municipal pages, or shopping-street pages. International travelers may struggle to find reliable information about:

- opening hours and closed days
- reservation methods
- cashless payment availability
- English menus
- vegetarian, halal, and allergy-friendly options
- local specialties and regional food culture
- nearest station or area
- official website or booking links

This project helps transform those scattered public pages into machine-readable CSV/JSON datasets that can support travel guides, local tourism maps, multilingual directories, and data education.

## What this project does

- Collects restaurant information from public and official-friendly sources
- Saves structured data as CSV and JSON
- Detects differences between the latest and previous datasets
- Provides a GitHub Actions workflow for scheduled collection
- Provides a travel-friendly restaurant schema
- Provides sample Hiroshima data and sample HTML
- Helps Python beginners learn public web data collection respectfully

## What this project does **not** do

This project is **not** designed to copy or redistribute proprietary review-platform content.

Avoid collecting or redistributing:

- third-party review text
- platform-owned or user-owned photos
- proprietary scores, rankings, or badges
- content prohibited by a target website's terms of service
- private or non-public information

Recommended sources include restaurant official websites, tourism association pages, municipal pages, shopping-street pages, and other sources that permit access and reuse.

## Current status

This repository is currently an early-stage OSS prototype.

- Version: `v0.1.0`
- Initial sample area: Hiroshima
- Main output formats: CSV / JSON
- Automation: GitHub Actions sample workflow
- License: MIT

## Project structure

```txt
japan-food-guide-data/
  collectors/
    base.py
    sample_html_collector.py
    diff.py
  data/
    hiroshima/
      restaurants.csv
      restaurants.json
      diff_report.json
  examples/
    hiroshima/
      sample_restaurants.html
  docs/
    application_note_ja.md
    issue_plan_ja.md
    legal_notes_ja.md
    release_v0.1.0.md
    schema_ja.md
    social_posts_ja.md
    usage_ja.md
  .github/
    ISSUE_TEMPLATE/
      bug_report.md
      feature_request.md
      data_source_request.md
    workflows/
      daily_collect.yml
  tests/
    test_sample_collector.py
  README.md
  CONTRIBUTING.md
  CODE_OF_CONDUCT.md
  requirements.txt
  LICENSE
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python run_sample.py
```

The sample command reads:

```txt
examples/hiroshima/sample_restaurants.html
```

and writes:

```txt
data/hiroshima/restaurants.csv
data/hiroshima/restaurants.json
data/hiroshima/diff_report.json
```

## CSV schema

Main columns:

```csv
id,name_ja,name_en,area,city,address,genre,tags,official_url,reservation_url,opening_hours,closed_days,price_lunch,price_dinner,cashless,english_menu,vegetarian_friendly,halal_friendly,solo_friendly,family_friendly,nearest_station,local_specialty,source_url,last_checked,notes
```

See [`docs/schema_ja.md`](docs/schema_ja.md) for details.

## Example use cases

- Hiroshima local food guide for international travelers
- Municipal food tourism datasets
- Restaurant opening-hours monitoring
- Travel-friendly restaurant directory generation
- Multilingual guide preparation
- Public web data collection education for Python beginners
- Local tourism support for small restaurants and shopping streets

## Roadmap

- [ ] Add a tourism association page collector
- [ ] Add an official restaurant website parser template
- [ ] Add Google Colab tutorial
- [ ] Add multilingual export helper
- [ ] Add schema validation
- [ ] Add more sample datasets for Hiroshima, Osaka, Kyoto, and Tokyo
- [ ] Add accessibility and dietary-option fields
- [ ] Add link-checking and source freshness checks
- [ ] Add GitHub Pages sample viewer

## Responsible use

Before collecting data, check:

- target website terms of service
- robots.txt
- copyright and database rights
- access frequency and server load
- whether redistribution is permitted
- whether API access is preferred over scraping

This toolkit is designed for respectful collection of public information and educational use.

## Maintainer workflow

This repository is maintained through:

- GitHub Issues for feature planning and bug tracking
- Pull requests for code and documentation changes
- Releases for versioned changes
- GitHub Actions for scheduled runs and tests

## Contributing

Contributions are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

MIT License.
