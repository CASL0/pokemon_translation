"""
ポケモンの外国語名辞書API
"""

import argparse
import logging
from requests.exceptions import Timeout, RequestException
from flask import Flask
from consts import CSV_FILE_NAME, AWS_S3_BUCKET
from utils import s3_upload, pokemon_wiki_to_csv
from controller import translation_bp, handle_bad_request
from werkzeug.exceptions import BadRequest


def main():
    """
    wiki/ポケモンの外国語名一覧から作成したCSVを元に、S3 Selectで翻訳を行うAPIサーバーです
    """
    parser = argparse.ArgumentParser(description="wiki/ポケモンの外国語名一覧から翻訳します")
    parser.add_argument("--csv", help="出力するCSVファイル名", type=str, default=CSV_FILE_NAME)
    parser.add_argument("--port", help="Flaskのポート", type=int, default=5000)
    parser.add_argument("--update", help="CSVを更新します", action="store_true")
    parser.add_argument(
        "--debug", "-d", help="デバッグモードでFlaskを起動します", action="store_true", default=False
    )
    args = parser.parse_args()
    if args.update:
        update_csv(args.csv)

    app = Flask(__name__)
    app.config["JSON_AS_ASCII"] = False
    app.register_error_handler(BadRequest, handle_bad_request)
    app.register_blueprint(translation_bp, url_prefix="/v1")
    app.run(host="0.0.0.0", port=args.port, debug=args.debug)


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
