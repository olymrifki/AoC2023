filename = "./Day 14/data.txt"
# Steps:
# Here, we'll rotate the formation 90 degrees so that we can calculate score using a single string
# 1. Read input and save each column into a string
board = []
with open(filename) as file:
    strings = [("#" + string.strip() + "#") for string in list(file.readlines())]
    for i in range(len(strings[0])):
        board.append(
            "#" + "".join([string[len(strings[0]) - i - 1] for string in strings]) + "#"
        )
print(board[0])
# board[0] = "-" + board[0][1:]
# print(board[0])


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
    string_length = len(string)
    wall_positions = [i for i in range(string_length) if string[i] == "#"]
    for i in range(len(wall_positions) - 1):
        o_indices = [
            j
            for j, s in enumerate(string[wall_positions[i] : wall_positions[i + 1]])
            if s == "O"
        ]

        for o_index in o_indices:
            result += (string_length - 2) - (wall_positions[i] + o_index - 1)
    return result


def move_all_os_to_left_of_string(string: str) -> str:
    result = ""
    string_length = len(string)
    wall_positions = [i for i in range(string_length) if string[i] == "#"]
    for i in range(len(wall_positions) - 1):
        total_os = len(
            [1 for s in string[wall_positions[i] : wall_positions[i + 1]] if s == "O"]
        )
        result += (
            "#"
            + "O" * total_os
            + "." * (wall_positions[i + 1] - wall_positions[i] - 1 - total_os)
        )
    result += "#"
    return result


def move_all_os_to_left_of_board(board: list[str]) -> list[str]:
    return [move_all_os_to_left_of_string(s) for s in board]


def rotate_board_90deg_to_the_right(board: list[str]) -> list[str]:
    result = []
    # print(board)
    for i in range(len(board[0])):
        result.append("".join([string[i] for string in board[::-1]]))
    return result


print(rotate_board_90deg_to_the_right(["o.", "o-"]))
assert ["o.", "o-"] == rotate_board_90deg_to_the_right([".-", "oo"])


def cycle_board(board: list[str]) -> list[str]:
    for i in range(4):
        board = move_all_os_to_left_of_board(board)
        board = rotate_board_90deg_to_the_right(board)
    return board


# 3. Add score for all string
print(
    sum([calculate_score(string) for string in move_all_os_to_left_of_board(board)]),
)
for i in range(1000):
    board = cycle_board(board)
    # for bo in rotate_board_90deg_to_the_right(((board))):
    #     print(bo)
    print(
        i,
        sum([calculate_score(string) for string in (board)]),
    )
print(sum([calculate_score(string) for string in board]))
# from here, i can probably detect repeated calculation using code
# but from printing, i found that the data.txt has 26 cycle
# at the 1000 cycle, the score is at 98029, and this happen at 1 bilion cycle too
