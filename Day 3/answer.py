import re


def is_special_symbol(char: str) -> bool:
    return char not in "0123456789. \n"


def is_number(char: str) -> bool:
    return char in "0123456789"


class NumberInLine:
    def __init__(self, line) -> None:
        self.numbers = []

        temp = ["", [], False]  # contain: (numbers, indices, is_adjacent)
        num = False
        for index, char in enumerate(line):
            if is_number(char):
                if not num:
                    num = True
                    temp[1].append(index)
                temp[0] = temp[0] + char
            elif num:
                num = False
                temp[1].append(index - 1)
                temp[0] = int(temp[0])
                self.numbers.append(temp)
                temp = ["", [], False]

    def is_symbol_adjacent(self, symbol_index):
        for number in self.numbers:
            number[-1] = number[-1] or (
                symbol_index >= int(number[1][0]) - 1
                and symbol_index <= int(number[1][-1]) + 1
            )


# print(NumberInLine("467..114..", 1).numbers)
# print(bool("0"))

with open("./Day 3/data.txt") as file:
    numbers = [NumberInLine(line) for line in file.readlines()]
    # for number in numbers:
    #     print(number.numbers)
    file.seek(0)
    print(set((" ".join([line for line in file.readlines()]))))

    file.seek(0)
    for line_index, line in enumerate(file.readlines()):
        line.strip()
        for char_index, char in enumerate(line):
            if is_special_symbol(char):
                if line_index - 1 >= 0:
                    numbers[line_index - 1].is_symbol_adjacent(char_index)
                numbers[line_index].is_symbol_adjacent(char_index)
                if line_index + 1 < len(numbers):
                    numbers[line_index + 1].is_symbol_adjacent(char_index)
    # print("===========================")
    # for number in numbers:
    #     print(number.numbers)
    adjacent_sum = 0
    for number in numbers:
        adjacent_sum += sum([el[0] for el in number.numbers if el[-1]])
    print(adjacent_sum)
