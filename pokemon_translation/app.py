"""
ポケモンの外国語名辞書（CSV形式）を作成します
"""

import sys
from requests.exceptions import Timeout, RequestException
from pokemon_csv import pokemon_wiki_to_csv


def main():
    """wiki/ポケモンの外国語名一覧を解析し、CSV出力します"""
    try:
        pokemon_wiki_to_csv()
    except Timeout:
        print("request timeout")
        sys.exit(1)
    except RequestException as error:
        print(f"requests failed: {error}")
        sys.exit(1)


# エントリーポイント
if __name__ == "__main__":
    main()
