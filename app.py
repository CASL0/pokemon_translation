import requests
from bs4 import BeautifulSoup
import PokemonTranslation


def main():
    url: str = "http://wiki.xn--rckteqa2e.com/wiki/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E3%81%AE%E5%A4%96%E5%9B%BD%E8%AA%9E%E5%90%8D%E4%B8%80%E8%A6%A7"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    pokemon_tables = soup.find_all("table", class_="graytable")

    for pokemon_table in pokemon_tables:
        pokemons = pokemon_table.find_all("tr")
        # TODO: CSV出力
        print(analyze_pokemon_elements(pokemons))


def analyze_pokemon_elements(elements) -> list:
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


main()
