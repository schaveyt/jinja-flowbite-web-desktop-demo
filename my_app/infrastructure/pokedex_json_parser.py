from my_app.domain.pokedex_types import Pokemon
import json


class PokedexJsonReader:

    def parse (self, json_file_location: str) -> list[Pokemon]:
        
        with open(json_file_location, mode="r", encoding="utf-8") as read_file:
            json_data = json.load(read_file)

            result: list[Pokemon] = []

            for i, pokemon_json in enumerate(json_data):
                pokemon = Pokemon(
                    id=pokemon_json["id"],
                    name=pokemon_json["name"]["english"],
                    typing=pokemon_json["type"],
                    species=pokemon_json["species"],
                    description=pokemon_json["description"])
                
                result.append(pokemon)
                

        return result