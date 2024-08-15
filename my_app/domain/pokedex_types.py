

class Pokemon:

    def __init__(self, id: int, name: str, typing: list[str], species: str, description: str) -> None:

        self.id = id
        self.name = name
        self.typing = typing
        self.species = species
        self.description = description
