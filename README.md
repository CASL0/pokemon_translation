# ポケモン翻訳テーブル

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://black.readthedocs.io/en/stable/_static/license.svg)](LICENSE.md)

[ポケモンの外国語名一覧](http://wiki.xn--rckteqa2e.com/wiki/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E3%81%AE%E5%A4%96%E5%9B%BD%E8%AA%9E%E5%90%8D%E4%B8%80%E8%A6%A7)から、外国語名の対応一覧のAPIサーバーです

## 使い方
### 事前準備

CSV配置先のS3バケット及び同S3へアクセス可能なIAMユーザーを作成してください。

IAMユーザーには以下のように`PutObject`、`GetObject`が許可されているポリシーをアタッチしてください。

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject"
            ],
            "Resource": "<バケットのARN>/*"
        }
    ]
}
```

作成したS3のアクセス情報を[.env](.env)に反映してください。

## 開発
### ビルド環境
[Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)の使用を推奨します。
