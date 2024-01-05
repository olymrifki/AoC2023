class Game:
    def __init__(self, line) -> None:
        for character in ":,;":
            line = line.replace(character, "")
        self.id = int(line.split()[1])
        self.data = line.split()[2:]

    def power(self):
        fewest_count = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for index, value in enumerate(self.data):
            if value in fewest_count.keys():
                fewest_count[value] = max(
                    fewest_count[value], int(self.data[index - 1])
                )

        result = 1
        for val in fewest_count.values():
            result *= val
        return result


with open("./Day 2/data.txt") as file:
    print(sum(Game(line).power() for line in file.readlines()))
