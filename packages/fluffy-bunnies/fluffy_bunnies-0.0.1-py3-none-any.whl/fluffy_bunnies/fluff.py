class Bunny:
    def __init__(self, name: str) -> None:
        self.name = name

    def hop(self) -> None:
        print(f"{self.name} is hopping!")


def make_bunnies(names: list[str]) -> list[Bunny]:
    return [Bunny(name) for name in names]


def main() -> None:
    bunnies = make_bunnies(["flopsy"])
    for bunny in bunnies:
        bunny.hop()
