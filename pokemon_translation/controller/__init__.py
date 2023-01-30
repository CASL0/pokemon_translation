from flask import jsonify
from models import ProblemDetail
from .translation_controller import *


def handle_bad_request(error):
    """
    400エラーのハンドリングをします
    """
    return (
        jsonify(ProblemDetail(None, error.name, error.code, error.description, None)),
        error.code,
    )
