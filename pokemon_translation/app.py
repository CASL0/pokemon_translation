"""
ポケモンの外国語名辞書（CSV形式）を作成します
"""

import argparse
import logging
from requests.exceptions import Timeout, RequestException
from flask import Flask
from pokemon_csv import pokemon_wiki_to_csv
from consts import CSV_FILE_NAME, AWS_S3_BUCKET
from utils import s3_upload
from controller import translation_bp, handle_bad_request
from werkzeug.exceptions import BadRequest


def main():
    """wiki/ポケモンの外国語名一覧を解析し、CSV出力します"""
    parser = argparse.ArgumentParser(description="wiki/ポケモンの外国語名一覧から翻訳します")
    parser.add_argument("--csv", help="出力するCSVファイル名", type=str, default=CSV_FILE_NAME)
    args = parser.parse_args()
    update_csv(args.csv)

    app = Flask(__name__)
    app.register_error_handler(BadRequest, handle_bad_request)
    app.register_blueprint(translation_bp, url_prefix="/v1")
    app.run(host="0.0.0.0", port=5000)


def update_csv(csv_file_name: str) -> bool:
    """
    S3の翻訳ファイルを更新します

    Args:
        csv_file_name (str): アップロードするCSVファイル名
    Returns
        bool: 成功の場合True、失敗の場合False
    """
    try:
        pokemon_wiki_to_csv(csv_file_name)
        s3_upload(csv_file_name, AWS_S3_BUCKET, csv_file_name)
        return True
    except (Timeout, RequestException) as error:
        logging.error("requests failed: %s", error)
        return False


# エントリーポイント
if __name__ == "__main__":
    main()
