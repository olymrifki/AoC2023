filename = "./Day 14/data.txt"
# Steps:
# Here, we'll rotate the formation 90 degrees so that we can calculate score using a single string
# 1. Read input and save each column into a string
strings = []
with open(filename) as file:
    lines = [line.strip() for line in list(file.readlines())]
    for i in range(len(lines[0])):
        strings.append("".join([line[i] for line in lines]))
# print(strings)


# 2.In a single string, walk from left to right:
#     add # at first element and last element
#     find index of all #s
#     between these index, count all Os
#         set O counter to 0
#         for each O:
#             add O counter
#             add score to ((total length-2) - (#'s start index  + O conuter))
# (making sure we get true length at the first O)
#     return singlle score
def calculate_score(string: str) -> int:
    result = 0
    string = "#" + string + "#"
    string_length = len(string)
    wall_positions = [i for i in range(string_length) if string[i] == "#"]
    for i in range(len(wall_positions) - 1):
        total_os = len(
            [1 for s in string[wall_positions[i] : wall_positions[i + 1]] if s == "O"]
        )
        for o_counter in range(total_os):
            result += (string_length - 2) - (wall_positions[i] + o_counter)
    return result


# 3. Add score for all string
print(sum([calculate_score(string) for string in strings]))
