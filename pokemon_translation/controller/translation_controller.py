"""
翻訳APIのコントローラー
"""
from flask import Blueprint, jsonify
from repository import TranslationRepository
from consts import CSV_FILE_NAME

translation_repository = TranslationRepository(CSV_FILE_NAME)
translation_bp = Blueprint("translation_bp", __name__)


@translation_bp.route("/translation/<name>")
def find_by_name(name: str):
    """
    ポケモン名から翻訳情報を取得するエンドポイント

    Args:
        name (str): ポケモンの名前
    """
    translation = translation_repository.find_by_name(name=name)
    if translation is None:
        raise Exception
    return jsonify(translation)
