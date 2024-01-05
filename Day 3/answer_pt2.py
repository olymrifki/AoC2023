import re


def is_special_symbol(char: str) -> bool:
    return char in "*"


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

    def fix_symbol_adjacent(self, symbol_index):
        for number in self.numbers:
            number[-1] = number[-1] or (
                symbol_index >= int(number[1][0]) - 1
                and symbol_index <= int(number[1][-1]) + 1
            )


def get_symbol_adjacent_number(number, symbol_index):
    if symbol_index >= int(number[1][0]) - 1 and symbol_index <= int(number[1][-1]) + 1:
        return number[0]


with open("./Day 3/data.txt") as file:
    numbers = [NumberInLine(line) for line in file.readlines()]

    gear_ratio = 0
    file.seek(0)

    result = 0
    for line_index, line in enumerate(file.readlines()):
        line.strip()
        for char_index, char in enumerate(line):
            if is_special_symbol(char):
                gear_numbers = []
                if line_index - 1 >= 0:
                    gear_numbers += [
                        get_symbol_adjacent_number(number, char_index)
                        for number in numbers[line_index - 1].numbers
                        if get_symbol_adjacent_number(number, char_index)
                    ]

                    gear_numbers += [
                        get_symbol_adjacent_number(number, char_index)
                        for number in numbers[line_index].numbers
                        if get_symbol_adjacent_number(number, char_index)
                    ]
                    if line_index + 1 < len(numbers):
                        gear_numbers += [
                            get_symbol_adjacent_number(number, char_index)
                            for number in numbers[line_index + 1].numbers
                            if get_symbol_adjacent_number(number, char_index)
                        ]
                if len(gear_numbers) == 2:
                    result += gear_numbers[0] * gear_numbers[1]
    # adjacent_sum = 0
    # for number in numbers:
    #     adjacent_sum += sum([el[0] for el in number.numbers if el[-1]])
    print(result)
