"""
ポケモンの外国語名辞書（CSV形式）を作成します
"""

import csv
from typing import List
import requests
from bs4 import BeautifulSoup, ResultSet
from models import PokemonTranslation
from consts import POKEMON_WIKI_URL, CSV_EOL, CSV_ENCODING, CSV_HEADER


def pokemon_wiki_to_csv(csv_file: str):
    """
    wiki/ポケモンの外国語名一覧を解析し、CSV出力します

    Raises:
        Timeout
        RequestException
    """
    response = requests.get(POKEMON_WIKI_URL, timeout=21)
    soup = BeautifulSoup(response.text, "html.parser")
    pokemon_tables = soup.find_all("table", class_="graytable")
    pokemons: List[PokemonTranslation] = []
    for pokemon_table in pokemon_tables:
        pokemons.extend(analyze_pokemon_elements(pokemon_table.find_all("tr")))
    write_csv(pokemons, csv_file)


def analyze_pokemon_elements(
    elements: ResultSet,
) -> List[PokemonTranslation]:
    """ポケモン外国語名を解析します"""
    pokemons: List[PokemonTranslation] = []
    for element in elements:
        attributes = element.find_all("td")
        if attributes == []:
            continue
        pokemons.append(
            PokemonTranslation(
                attributes[0].text.rstrip("\n"),
                attributes[1].a.text.rstrip("\n"),
                attributes[2].text.rstrip("\n"),
                attributes[3].text.rstrip("\n"),
                attributes[4].text.rstrip("\n"),
                attributes[5].text.rstrip("\n"),
                attributes[6].text.rstrip("\n"),
                attributes[7].text.rstrip("\n"),
            )
        )
    return pokemons


def write_csv(pokemons: List[PokemonTranslation], file_name: str):
    """ポケモン外国語名一覧をCSVとして書き込みます"""
    with open(file_name, "w", encoding=CSV_ENCODING) as f:
        writer = csv.writer(f, lineterminator=CSV_EOL)
        writer.writerow(CSV_HEADER)
        for pokemon in pokemons:
            record: list = [
                pokemon.id,
                pokemon.jpn,
                pokemon.eng,
                pokemon.deu,
                pokemon.fra,
                pokemon.kor,
                pokemon.chs,
                pokemon.cht,
            ]
            writer.writerow(record)
