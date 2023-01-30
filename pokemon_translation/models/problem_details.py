"""
エラーレスポンスのモデル
"""
from typing import Optional
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ProblemDetail:
    """
    RFC7807

    typeとinstanceはオプショナルにしています
    """

    type: Optional[str]
    title: str
    status: str
    detail: str
    instance: Optional[str]
