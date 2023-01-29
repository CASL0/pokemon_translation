from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class PokemonTranslation:
    """ポケモン翻訳エンティティ"""

    id: str
    jpn: str
    eng: str
    deu: str
    fra: str
    kor: str
    chs: str
    cht: str
