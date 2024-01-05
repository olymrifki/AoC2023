filename = "./Day 11/data.txt"
# Steps:
# 1. Read all lines into list of string.
all_maps = []
with open(filename) as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        all_maps.append(line)


def insert_char(char: str, position: int, string: str) -> str:
    return string[:position] + char + string[position:]


#     1.1 If any rows and columns that contains no #, duplicate it
def expand_rows(all_maps: list[str]) -> list[str]:
    result = all_maps.copy()
    initial_column_length = len(result)
    extra_index = 0
    for i in range(initial_column_length):
        if "#" not in result[i + extra_index]:
            result.insert(i + extra_index, result[i + extra_index])
            extra_index += 1
    return result


def expand_columns(all_maps: list[str]) -> list[str]:
    result = all_maps.copy()
    initial_row_length = len(result[0])
    extra_index = 0
    for i in range(initial_row_length):
        if "#" not in [result[j][i + extra_index] for j in range(len(result))]:
            result = [insert_char(".", i + extra_index, string) for string in result]
            extra_index += 1
    return result


def expand_map(all_maps: list[str]) -> list[str]:
    return expand_columns(expand_rows(all_maps))


assert expand_rows(["."]) == [".", "."]
assert expand_columns([".", "."]) == ["..", ".."]
assert expand_map(["."]) == ["..", ".."]
all_maps = expand_map(all_maps)
#     1.2 For each # in any line: save it to an object containing its position. And save all to list
positions = [
    (i, j)
    for j in range(len(all_maps))
    for i in range(len(all_maps[0]))
    if all_maps[j][i] == "#"
]
# 2. Set sum to 0. For all # object in list:
#     for all # object after the first:
#         calculate difference in position and add it to sum
result = 0
for i, position in enumerate(positions):
    for other_position in positions[i:]:
        result += abs(position[0] - other_position[0]) + abs(
            position[1] - other_position[1]
        )
print(result)
