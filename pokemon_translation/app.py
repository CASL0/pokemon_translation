"""
ポケモンの外国語名辞書（CSV形式）を作成します
"""

import sys
import argparse
from requests.exceptions import Timeout, RequestException
from pokemon_csv import pokemon_wiki_to_csv
from consts import CSV_FILE_NAME


def main():
    """wiki/ポケモンの外国語名一覧を解析し、CSV出力します"""
    parser = argparse.ArgumentParser(description="wiki/ポケモンの外国語名一覧から翻訳します")
    parser.add_argument("--csv", help="出力するCSVファイル名", type=str)
    args = parser.parse_args()
    try:
        if args.csv is None:
            pokemon_wiki_to_csv(CSV_FILE_NAME)
        else:
            pokemon_wiki_to_csv(args.csv)
    except Timeout:
        print("request timeout")
        sys.exit(1)
    except RequestException as error:
        print(f"requests failed: {error}")
        sys.exit(1)


# エントリーポイント
if __name__ == "__main__":
    main()
