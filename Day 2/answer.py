class Game:
    def __init__(self, line) -> None:
        for character in ":,;":
            line = line.replace(character, "")
        self.id = int(line.split()[1])
        self.data = line.split()[2:]


def is_possible_game(game: Game) -> bool:
    limit = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    for index, value in enumerate(game.data):
        if value in limit.keys():
            if int(game.data[index - 1]) > limit[value]:
                return False
    return True


with open("./Day 2/data.txt") as file:
    print(
        sum(Game(line).id for line in file.readlines() if is_possible_game(Game(line)))
    )
