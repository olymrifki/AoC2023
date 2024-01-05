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
def get_row_count_above_reflection_line(island: list[str]) -> int:
    result = 0
    for i in range(1, len(island)):
        if island[i] == island[i - 1]:
            result = i
            index = 0
            is_matching = True
            while i + index < len(island) and i - 1 - index >= 0:
                if island[i + index] != island[i - 1 - index]:
                    is_matching = False
                    break
                index += 1
            if is_matching:
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
