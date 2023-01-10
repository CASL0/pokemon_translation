"""
ポケモンの外国語名辞書（CSV形式）を作成します

python app.py
"""

import csv
import requests
from bs4 import BeautifulSoup
import PokemonTranslation


def main():
    """wiki/ポケモンの外国語名一覧を解析し、CSV出力します"""
    url: str = "http://wiki.xn--rckteqa2e.com/wiki/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E3%81%AE%E5%A4%96%E5%9B%BD%E8%AA%9E%E5%90%8D%E4%B8%80%E8%A6%A7"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    pokemon_tables = soup.find_all("table", class_="graytable")
    pokemons: list = []
    for pokemon_table in pokemon_tables:
        pokemons.extend(analyze_pokemon_elements(pokemon_table.find_all("tr")))
    write_csv(pokemons)


def analyze_pokemon_elements(elements) -> list:
    """ポケモン外国語名を解析します"""
    pokemons: list = []
    for element in elements:
        attributes = element.find_all("td")
        if attributes == []:
            continue
        pokemons.append(
            PokemonTranslation.PokemonTranslation(
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


def write_csv(pokemons: PokemonTranslation.PokemonTranslation):
    """ポケモン外国語名一覧をCSVとして書き込みます"""
    CSV_HEADER: list = ["id", "jpn", "eng", "deu", "fra", "kor", "chs", "cht"]
    CSV_FILE_NAME: str = "pokemon_translation.csv"
    with open(CSV_FILE_NAME, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
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


# エントリーポイント
if __name__ == "__main__":
    main()
