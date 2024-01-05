filename = "./Day 13/data.txt"
# Steps:


# 2. To detect horizontal line:
#     2.1 Searching from the first row:
#         if two consecutive row are identical:
#             Save the bottom row index
#             Start comparing all rows aboe and below it
#             If we rows keep matching until out of rows:
#                 return saved row index
#             But if there is a mismatch
#                 keep searching
#         if no match at all:
#             return 0


# Smudge detector function to detect if two row are matching, and also return smudge:
# Get row, mirrored row, and boolean containing is smudge ever happen:
#     If exact match:
#         return true
#     If only one smudge and smudge never happen:
#         return true
#     return false
def is_smudge_match(row1: str, row2: str) -> bool:
    smudge_count = 0
    for i in range(len(row1)):
        if row1[i] != row2[i]:
            smudge_count += 1
            if smudge_count > 1:
                return False
    return smudge_count == 1


def is_almost_match(row1: str, row2: str, is_smudged_before: bool) -> (bool, bool):
    if row1 == row2:
        return True, is_smudged_before
    if (not is_smudged_before) and is_smudge_match(row1, row2):
        return True, True
    return False, is_smudged_before


def get_row_count_above_reflection_line(island: list[str]) -> int:
    result = 0
    for i in range(1, len(island)):
        match, is_smudged_before = is_almost_match(island[i], island[i - 1], False)
        if match:
            result = i
            is_possible_matching = True

            index = 1  # to avoid comparing the same line twice and messing smudge history, start from 1 instead of 0
            while i + index < len(island) and i - 1 - index >= 0:
                match, is_smudged_before = is_almost_match(
                    island[i + index], island[i - 1 - index], is_smudged_before
                )
                if not match:
                    is_possible_matching = False
                    break
                index += 1
            if is_possible_matching and is_smudged_before:
                return result
            else:
                result = 0
    return result


class Island:
    def __init__(self, lines: list[str]) -> None:
        self.island = [line for line in lines]
        self.rotated_island = []
        for i in range(len(lines[0])):
            self.rotated_island.append("".join([line[i] for line in lines]))

    def get_score(self):
        return get_row_count_above_reflection_line(
            self.island
        ) * 100 + get_row_count_above_reflection_line(self.rotated_island)


# 1. Read lines into islands
#     We will develop way to find only horizontal line. Island object will also have rotated version
with open(filename) as file:
    all_lines = file.readlines()
    islands = []
    temp_lines = []
    for line in all_lines:
        line = line.strip()
        if line != "":
            temp_lines.append(line)
        else:
            islands.append(Island(temp_lines))
            temp_lines = []

    islands.append(Island(temp_lines))
# 3. Each island object will have to multiply the score by 100 or not
#     Then sum all the score
print(sum([island.get_score() for island in islands]))
