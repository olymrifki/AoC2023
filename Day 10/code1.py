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


def get_current_pipe(position: tuple[int]) -> str:
    if position[0] < 0 or position[0] >= len(pipe_map[0]):
        return "."
    elif position[1] < 0 or position[1] >= len(pipe_map):
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

while len(positions) == len(set(positions)):
    current_pipes = [get_current_pipe(position) for position in positions]
    next_directions = [
        get_next_direction(previous_directions[i], current_pipes[i])
        for i in range(len(previous_directions))
    ]
    for index, direction in enumerate(next_directions):
        if direction == (0, 0):
            next_directions.pop(index)
            positions.pop(index)
    positions = [
        add_position(positions[i], next_directions[i])
        for i in range(len(next_directions))
    ]

    previous_directions = next_directions
    step_count += 1

print(step_count)
