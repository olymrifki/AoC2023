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


print(sum(hash_a_string(s) for s in strings))
