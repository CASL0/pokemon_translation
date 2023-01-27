from dataclasses import dataclass


@dataclass
class PokemonTranslation:
    id: str
    jpn: str
    eng: str
    deu: str
    fra: str
    kor: str
    chs: str
    cht: str
