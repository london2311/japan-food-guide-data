# データスキーマ

このプロジェクトでは、訪日旅行者が使いやすい飲食店情報をCSV/JSONで保存します。

## 主な項目

| Field | 説明 |
|---|---|
| id | 店名と住所から生成する安定ID |
| name_ja | 日本語店名 |
| name_en | 英語店名 |
| area | エリア名 |
| city | 市区町村 |
| address | 住所 |
| genre | 料理ジャンル |
| tags | 補助タグ。カンマ区切り推奨 |
| official_url | 店舗公式URL |
| reservation_url | 予約URL |
| opening_hours | 営業時間 |
| closed_days | 定休日 |
| price_lunch | 昼の価格帯 |
| price_dinner | 夜の価格帯 |
| cashless | キャッシュレス対応 |
| english_menu | 英語メニュー有無 |
| vegetarian_friendly | ベジタリアン対応 |
| halal_friendly | ハラール対応 |
| solo_friendly | 一人利用しやすいか |
| family_friendly | 家族利用しやすいか |
| nearest_station | 最寄駅 |
| local_specialty | 地域名物 |
| source_url | 情報源URL |
| last_checked | 最終確認日 |
| notes | 備考 |

## 方針

- 不明な項目は空欄または `unknown` とする
- 断定できない情報は `ask staff` など控えめに記載する
- 口コミ本文や第三者写真は保存しない
- 店舗公式・自治体・観光協会などの公開情報を優先する
