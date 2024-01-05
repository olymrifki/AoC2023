# Steps:
# 1. Read text of input into 2D list
filename = "./Day 10/data.txt"
pipe_map = []
starting_position = ()
with open(filename) as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        if "S" in line:
            starting_position = (line.index("S"), i)
        pipe_map.append(line)


# pipe following will need previous direction, current pipe
# check if this two arguments valid and
# will return next direction (return (0,0) if invalid)
def get_next_direction(previous_direction: tuple[int], pipe: str) -> tuple[int]:
    # | is a vertical pipe connecting north and south.
    # - is a horizontal pipe connecting east and west.
    # L is a 90-degree bend connecting north and east.
    # J is a 90-degree bend connecting north and west.
    # 7 is a 90-degree bend connecting south and west.
    # F is a 90-degree bend connecting south and east.
    direction_to_pipe = {
        (0, -1): ["|", (0, -1), "7", (-1, 0), "F", (1, 0)],  # up
        (0, 1): ["|", (0, 1), "L", (1, 0), "J", (-1, 0)],  # down
        (1, 0): ["-", (1, 0), "7", (0, 1), "J", (0, -1)],  # right
        (-1, 0): ["-", (-1, 0), "L", (0, -1), "F", (0, 1)],  # left
    }
    if previous_direction not in direction_to_pipe.keys():
        return (0, 0)
    if pipe not in direction_to_pipe[previous_direction]:
        return (0, 0)
    pipe_index = direction_to_pipe[previous_direction].index(pipe)
    next_direction = direction_to_pipe[previous_direction][1 + pipe_index]
    return next_direction


def add_position(pos1: tuple[int], pos2: tuple[int]) -> tuple[int]:
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])


def is_position_not_in_map(position: tuple[int]) -> bool:
    if position[0] < 0 or position[0] >= len(pipe_map[0]):
        return True
    elif position[1] < 0 or position[1] >= len(pipe_map):
        return True
    return False


def get_current_pipe(position: tuple[int]) -> str:
    if is_position_not_in_map(position):
        return "."
    return pipe_map[position[1]][position[0]]


# 2. From the starting point S follow all four side of adjacent to it
# until it is connected to an invalid connection or two of them meet at a point.
#  Track the steps in step_count, positions, and previous_directions
step_count = 1
previous_directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
positions = [
    add_position(starting_position, previous_direction)
    for previous_direction in previous_directions
]


def get_next_positions(
    positions: list[tuple[int]], directions: list[tuple[int]]
) -> list[tuple[int]]:
    return [add_position(positions[i], directions[i]) for i in range(len(directions))]


def get_next_directions(
    positions: list[tuple[int]], directions: list[tuple[int]]
) -> list[tuple[int]]:
    current_pipes = [get_current_pipe(position) for position in positions]
    return [
        get_next_direction(directions[i], current_pipes[i])
        for i in range(len(directions))
    ]


while len(positions) == len(set(positions)):
    next_directions = get_next_directions(positions, previous_directions)
    for index, direction in enumerate(next_directions):
        if direction == (0, 0):
            next_directions.pop(index)
            positions.pop(index)
    positions = get_next_positions(positions, next_directions)
    previous_directions = next_directions
    step_count += 1
print(step_count)

# step 2:
# 1. Traceback the loop from meeting point and replace all walls by "0"


def change_string_character(string: str, index, new_character):
    return string[:index] + new_character + string[index + 1 :]


def change_pipe_into_wall(position: tuple[int]) -> None:
    pipe_map[position[1]] = change_string_character(
        pipe_map[position[1]], position[0], "0"
    )


# finding meeting position:
for i, position in enumerate(positions):
    positions_copy = positions.copy()
    positions_copy.pop(i)
    if position in positions_copy:
        meeting_position = position
# getting new direction:
pipe_to_outward_direction_map = {
    "|": [(0, 1), (0, -1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(1, 0), (0, -1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
}
backtrack_directions = pipe_to_outward_direction_map[get_current_pipe(meeting_position)]

backtrack_positions = [
    add_position(meeting_position, previous_direction)
    for previous_direction in backtrack_directions
]

change_pipe_into_wall(meeting_position)
change_pipe_into_wall(starting_position)
# save wall positions order
wall_positions = [[], []]
while step_count > 1:
    next_directions = get_next_directions(backtrack_positions, backtrack_directions)
    next_backtrack_positions = get_next_positions(backtrack_positions, next_directions)
    for i, position in enumerate(backtrack_positions):
        wall_positions[i].append(position)
        change_pipe_into_wall(position)
    backtrack_positions = next_backtrack_positions
    backtrack_directions = next_directions
    step_count -= 1
# for line in pipe_map:
#     print(line)


def fill_map(position: tuple[int]) -> None:
    pipe_map[position[1]] = change_string_character(
        pipe_map[position[1]], position[0], "I"
    )


def flood_fill(initial_position: tuple[int]) -> (bool, list[str]):
    # return true if floodfill success
    old_pipe_map = pipe_map.copy()
    queue = []
    fill_map(initial_position)
    queue.append(initial_position)
    while queue:
        position = queue.pop(0)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for direction in directions:
            new_position = add_position(position, direction)
            if is_position_not_in_map(new_position):
                return False, old_pipe_map
            current_char = get_current_pipe(new_position)
            if current_char not in "I0":
                fill_map(new_position)
                queue.append(new_position)

    return True, pipe_map


# 2. After reaching starting point, loop back again and :
#     2.1 Because we dont know if the inside area it at the left or right, we will try to fill each side separately using *four directional flood fill* into and change each of the element with "I". Either
#         a. The wrong side will evetually tries to fill outside the matrix border, in this case, move to next fill side
#         b. All will be filled correctly, count all "I" in all the image
# by the saved wall position
wall_positions[1].reverse()
ordered_wall_position = (
    [meeting_position] + wall_positions[0] + [starting_position] + wall_positions[1]
)


# clockwise left fill

ccw_left_direction_to_fill_map = {
    (0, -1): [(-1, 0), (-1, 1)],  # up -> fill left
    (0, 1): [(1, 0), (1, -1)],  # down -> fill right
    (1, 0): [(0, -1), (-1, -1)],  # right -> fill up
    (-1, 0): [(0, 1), (1, 1)],  # left -> fill down
}

cw_right_direction_to_fill_map = {
    (0, -1): [(1, 0), (1, 1)],  # up -> fill right
    (0, 1): [(-1, 0), (-1, -1)],  # down -> fill left
    (1, 0): [(0, 1), (-1, 1)],  # right -> fill down
    (-1, 0): [(0, -1), (1, -1)],  # left -> fill up
}


def fill_loop(direction_to_fill_map):
    global pipe_map
    pipe_map_copy = pipe_map.copy()
    for i in range(1, len(ordered_wall_position)):
        # if i % 500 == 0:
        #     print(f"progress: {i/len(ordered_wall_position)*100} %")
        direction = (
            ordered_wall_position[i][0] - ordered_wall_position[i - 1][0],
            ordered_wall_position[i][1] - ordered_wall_position[i - 1][1],
        )

        for delta in direction_to_fill_map[direction]:
            initial_position = add_position(ordered_wall_position[i], delta)
            if is_position_not_in_map(initial_position):
                continue
            current_char = get_current_pipe(initial_position)
            if current_char not in "I0":
                is_valid, pipe_map = flood_fill(initial_position)
                if not is_valid:
                    return pipe_map_copy, pipe_map_copy
    return pipe_map, pipe_map_copy


res, pipe_map = fill_loop(ccw_left_direction_to_fill_map)
score = 0
for line in res:
    for char in line:
        if char == "I":
            score += 1
print(score)

# for line in res:
#     print(line)
res, pipe_map = fill_loop(cw_right_direction_to_fill_map)
# _, pipe_map = flood_fill((12, 4))
score = 0
for line in res:
    for char in line:
        if char == "I":
            score += 1
print(score)

# for line in res:
#     print(line)
