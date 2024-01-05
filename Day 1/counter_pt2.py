import re

[m.start() for m in re.finditer("test", "test test test test")]


def get_number(line: str) -> int:
    numbers = [number for number in line if number in "0123456789"]
    return int(numbers[0] + numbers[-1])


def get_intable_string(line: str) -> str:
    translation = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }
    translated = []
    for pattern in translation.keys():
        translated += [
            [matched.start(), translation[pattern]]
            for matched in re.finditer(pattern, line)
        ]

    translated.sort(key=lambda x: x[0])
    return "".join([x[1] for x in translated])


with open("./Day 1/data.txt") as file:
    # print(file.readline)
    print(sum(get_number(get_intable_string(line)) for line in file.readlines()))
