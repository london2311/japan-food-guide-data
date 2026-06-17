# 初期Issue案

GitHubにアップした後、以下のIssueを作ると「保守されているOSS」に見えやすくなります。

## Issue 1

Title: Add tourism association page collector for Hiroshima

Body:
Create a collector template for public tourism association restaurant list pages. The collector should extract name, area, official URL, genre, and source URL when permitted by the target site.

Labels: enhancement, data-source

## Issue 2

Title: Add schema validation for restaurants.csv

Body:
Add validation for required fields such as id, name_ja, area, city, source_url, and last_checked. Invalid rows should be reported with clear error messages.

Labels: enhancement, good first issue

## Issue 3

Title: Add Google Colab tutorial for beginners

Body:
Create a beginner-friendly Colab guide that runs the sample collector and explains how CSV/JSON outputs are generated.

Labels: documentation, good first issue

## Issue 4

Title: Add multilingual export helper

Body:
Add a helper script that prepares fields for English, Chinese, and Korean guide generation without overwriting the original Japanese source fields.

Labels: enhancement

## Issue 5

Title: Add responsible source checklist to pull request template

Body:
Create a pull request template that asks contributors to confirm source terms, robots.txt, access frequency, and whether redistribution is allowed.

Labels: documentation, governance

## Issue 6

Title: Add GitHub Pages sample viewer

Body:
Create a simple static page that displays the sample Hiroshima restaurant dataset from JSON.

Labels: enhancement, frontend

## Issue 7

Title: Add link freshness checker

Body:
Add a script that checks whether official_url and source_url are reachable and logs stale or broken links.

Labels: enhancement, maintenance

## Issue 8

Title: Add sample dataset for Miyajima area

Body:
Add a small sample dataset for Miyajima using official or tourism-friendly public sources.

Labels: data-source, good first issue
