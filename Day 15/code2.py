# The instruction here was too long that I code along while reading them instead of explaining inside solution
filename = "./Day 15/data.txt"
strings = []
with open(filename) as file:
    temp = ""
    for line in file.readlines():
        temp += line.strip()
    strings = temp.split(",")


def hashin(string: str, index: int) -> int:
    # this is all powers of 17 mod 256
    multiplier = [
        17,
        33,
        49,
        65,
        81,
        97,
        113,
        129,
        145,
        161,
        177,
        193,
        209,
        225,
        241,
        1,
    ]
    return (ord(string) * multiplier[index % len(multiplier)]) % 256


def hash_a_string(string: str) -> int:
    return (
        sum([hashin(s, len(string) - 1 - index) for index, s in enumerate(string)])
        % 256
    )


all_label = [[] for i in range(256)]
all_focus = [[] for i in range(256)]


class Step:
    def __init__(self, string: str) -> None:
        if "-" in string:
            self.operation = "-"
            self.label, self.focus = string.split("-")
        elif "=" in string:
            self.operation = "="
            self.label, self.focus = string.split("=")
        self.box_position = hash_a_string(self.label)

    def operate(self, all_label: list[list[str]], all_focus: list[list[int]]):
        if self.operation == "-":
            if self.label in all_label[self.box_position]:
                positions = [
                    i
                    for i, label in enumerate(all_label[self.box_position])
                    if label == self.label
                ]
                for position in positions[::-1]:
                    all_label[self.box_position].pop(position)
                    all_focus[self.box_position].pop(position)
            else:
                print(f"no {self.label} in {all_label[self.box_position]}")
        elif self.operation == "=":
            if self.label in all_label[self.box_position]:
                for i, label in enumerate(all_label[self.box_position]):
                    if label == self.label:
                        all_focus[self.box_position][i] = self.focus
            else:
                all_label[self.box_position].append(self.label)
                all_focus[self.box_position].append(self.focus)
        else:
            print("No operation called")
        return all_label, all_focus


# print(strings)
for s in strings:
    step = Step(s)
    all_label, all_focus = step.operate(all_label, all_focus)
result = 0
for i, label in enumerate(all_label):
    if label:
        for j in range(len(label)):
            result += (i + 1) * (j + 1) * int(all_focus[i][j])

# print(list(zip(all_label, all_focus)))
print(result)
