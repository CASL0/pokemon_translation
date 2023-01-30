"""
翻訳テーブルのリポジトリ層
"""
from typing import Optional
from utils import s3_select
from consts import AWS_S3_BUCKET
from models import PokemonTranslation


class TranslationRepository:
    """
    翻訳テーブルのCRUD操作を実行するリポジトリ
    """

    def __init__(self, s3_object_key: str) -> Optional[PokemonTranslation]:
        self.s3_object_key = s3_object_key

    def find_by_name(self, name: str):
        """
        ポケモン名から翻訳情報を取得します

        Args:
            name (str): ポケモンの名前
        """
        query = f"SELECT * FROM s3object WHERE jpn = '{ name }' OR eng = '{ name }' OR deu = '{ name }' OR fra = '{ name }' OR kor = '{ name }' OR chs = '{ name }' OR cht = '{ name }'"
        result = s3_select(AWS_S3_BUCKET, self.s3_object_key, query)

        return PokemonTranslation.from_json(result) if result is not None else None
