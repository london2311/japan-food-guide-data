# 使い方

## 1. インストール

```bash
pip install -r requirements.txt
```

## 2. サンプル実行

```bash
python run_sample.py
```

## 3. 出力確認

```txt
data/hiroshima/restaurants.csv
data/hiroshima/restaurants.json
data/hiroshima/diff_report.json
```

## 4. 実サイト対応の考え方

まずは対象サイトの利用規約とrobots.txtを確認してください。
そのうえで、店舗公式サイト、観光協会、自治体ページなど、公開情報として整理しやすいページを対象にします。

新しいページに対応する場合は、`collectors/sample_html_collector.py` を参考にして、専用collectorを作成します。

## 5. GitHub Actionsで定期実行

`.github/workflows/daily_collect.yml` にサンプルを入れています。
毎日自動で `python run_sample.py` を実行する構成です。
