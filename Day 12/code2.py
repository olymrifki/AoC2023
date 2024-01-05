filename = "./Day 12/data.txt"
# Steps:
# 1. Real line, separate . and #s with its group number
lines = []
group_numbers = []
with open(filename) as file:
    file_lines = file.readlines()
    for line in file_lines:
        line = line.strip()
        line, groups = line.split(" ")
        groups = [int(num) for num in groups.split(",")]
        line = ((line + "?") * 5)[:-1]
        groups = groups * 5
        lines.append(line)
        group_numbers.append(groups)


#     2.2 To compare window:
#         For each string in window and cropped line:
#             if ith crpped element is ? or ith cropped element equals ith elementof window:
#                 continue
#             else return false
#         return true
def is_equal(window: str, cropped_line: str) -> bool:
    for i in range(len(window)):
        if cropped_line[i] == "?" or cropped_line[i] == window[i]:
            continue
        return False
    return True


# 2. For each line,
#     Add . at both sides of the line
#     2.1 Get first group number
#         Say group number of n: Create window of size n+2 containing ".#*n."
#         If window length is more than inserted line:
#             return 0
#         If group number is empty:
#             If no # in line return 1
#             otherwise return 0
#         Set result to 0
#         Read from left to right:
#             If line slot has any #:
#                 stop search after that first # disappear
#             If Window can fits that line slot:
#                 Add result with Step2 with line starting from left_index + n+2
#         return result
memod = {}


def count_arrangements(line: str, group_number: list[int]) -> int:
    if (line, tuple(group_number)) in memod.keys():
        return memod[(line, tuple(group_number))]
    if len(group_number) == 0:
        return "#" not in line

    number = group_number[0]
    if len(line) < number:
        return 0
    window = "." + "#" * number + "."
    line = "." + line + "."
    result = 0
    # stop searching after the 1st "#" disappear from the searched line
    if "#" in line:
        anchored_index = min(line.index("#"), len(line) - len(window) + 1)
    else:
        anchored_index = len(line) - len(window) + 1

    for i in range(anchored_index):
        if is_equal(window, line[i : i + len(window)]):
            result += count_arrangements(
                line[i + len(window) : len(line) - 1], group_number[1:]
            )

    # print(f"{line[1:-1]} {group_number} -> {result}")
    memod[(line[1:-1], tuple(group_number))] = result
    return result


# print(count_arrangements(".??..??...?##.", [1, 1, 3]))
# print(count_arrangements("?#?#?#?#?#?#?#?", [1, 3, 1, 6]))
# print(count_arrangements("??????????.?????#?", [1, 1, 3, 1, 1, 1]))
# print(count_arrangements("?????#?", [1, 3, 1, 1, 1]))
# print(count_arrangements("?????#?", [1, 1, 1]))
# print(count_arrangements("?###????????", [3, 2, 1]))
# print(count_arrangements("????.#???#?", [1, 1, 3]))  # -> 8
# print(count_arrangements("???.#.?.???????####?", [1, 2, 4]))  # -> 5
# print(count_arrangements("#.?.???????####?", [2, 4]))  # -> 0
# print(count_arrangements("?????", [1, 1]))

# 3. Add the result
print(sum([count_arrangements(lines[i], group_numbers[i]) for i in range(len(lines))]))
