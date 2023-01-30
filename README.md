# ポケモン翻訳テーブル

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://black.readthedocs.io/en/stable/_static/license.svg)](LICENSE.md)

[ポケモンの外国語名一覧](http://wiki.xn--rckteqa2e.com/wiki/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E3%81%AE%E5%A4%96%E5%9B%BD%E8%AA%9E%E5%90%8D%E4%B8%80%E8%A6%A7)から、外国語名の対応一覧の API サーバーです

## 使い方

### 事前準備

CSV 配置先の S3 バケット及び同 S3 へアクセス可能な IAM ユーザーを作成してください。

IAM ユーザーには以下のように`PutObject`、`GetObject`が許可されているポリシーをアタッチしてください。

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": ["s3:PutObject", "s3:GetObject"],
      "Resource": "<バケットのARN>/*"
    }
  ]
}
```

作成した S3 のアクセス情報を[.env](.env)に反映してください。

### サーバー起動

`docker-compose up`を実行すると、localhost の 5000 番ポートに Flask をホスティングします。

`http://localhost:5000/v1/translation/{ポケモン名}`を GET することで同ポケモンの翻訳情報を取得できます。

例：メタモンの翻訳情報を取得する

リクエスト：`http://localhost:5000/v1/translation/Ditto`

レスポンス：

```json
{
  "chs": "百变怪",
  "cht": "百變怪",
  "deu": "Ditto",
  "eng": "Ditto",
  "fra": "Metamorph",
  "id": "132",
  "jpn": "メタモン",
  "kor": "메타몽"
}
```

上記のリクエストパラメーターで`Ditto`と指定した個所を`メタモン`としても同じ結果が得られます。

ポケモン名に指定可能な言語は[対応言語](#対応言語)をご確認ください。

## 対応言語

次の言語に対応しています。

- 日本語
- 英語
- ドイツ語
- フランス語
- 韓国語
- 中国語（簡）
- 中国語（繁）

## 開発

### ビルド環境

[Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)の使用を推奨します。

- python 3.11+
