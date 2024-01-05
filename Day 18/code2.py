filename = "./Day 18/example.txt"


def add_position(pos1: tuple[int], pos2: tuple[int]) -> tuple[int]:
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])


def mult_position(multiplier, pos: tuple[int]) -> tuple[int]:
    return (multiplier * pos[0], multiplier * pos[1])


# Steps
# 1. Read file and create 2d map of the wall

position = (0, 0)
positions = [position]
with open(filename) as file:
    for line in file.readlines():
        line = line.strip()
        _, __, color = line.split(" ")

        # directions = {
        #     "2": (-1, 0),
        #     "0": (1, 0),
        #     "3": (0, -1),
        #     "1": (0, 1),
        # }
        # direction = directions[color[7]]
        # distance = int(color[2:7], 16)

        directions = {
            "L": (-1, 0),
            "R": (1, 0),
            "U": (0, -1),
            "D": (0, 1),
        }
        direction = directions[_]
        distance = int(__)
        positions.append(
            add_position(positions[-1], mult_position(distance, direction))
        )
min_pos = (
    min([position[0] for position in positions]),
    min([position[1] for position in positions]),
)
max_pos = (
    max([position[0] for position in positions]),
    max([position[1] for position in positions]),
)

map_size = (max_pos[0] - min_pos[0] + 1, max_pos[1] - min_pos[1] + 1)
print(map_size)

# We will find the area covered by rectangle when we move left then up or down and right then up or down
# And add or subtract them ultil instruction finished
position = add_position((1, 0), mult_position(-1, min_pos))

current_moving_state = None
prev_moving_state = None
result = 0
with open(filename) as file:
    lines = list(file.readlines())

    _, __, color = lines[0].strip().split(" ")

    # moving_state = {
    #     "2": "H",
    #     "0": "H",
    #     "3": "V",
    #     "1": "V",
    # }
    # direction = directions[color[7]]
    # distance = int(color[2:7], 16)
    # prev_moving_state = moving_state[color[7]]
    moving_state = {
        "L": "H",
        "R": "H",
        "U": "V",
        "D": "V",
    }
    direction = directions[_]
    distance = int(__)
    prev_moving_state = moving_state[_]
    vertical_distance = (0, 0)
    if prev_moving_state == "V":
        vertical_distance = add_position(
            vertical_distance, mult_position(distance, direction)
        )
    else:
        if direction == (-1, 0):
            result += distance
        position = add_position(position, mult_position(distance, direction))

    for line in lines[1:]:
        _, __, color = line.strip().split(" ")
        # direction = directions[color[7]]
        # distance = int(color[2:7], 16)
        # current_moving_state = moving_state[color[7]]
        direction = directions[_]
        distance = int(__)
        current_moving_state = moving_state[_]

        if current_moving_state == "H":
            if direction == (-1, 0):
                result += distance
            if vertical_distance[1] > 0:
                result += position[0] * vertical_distance[1]
            else:
                result += (position[0] - 1) * vertical_distance[1]

            vertical_distance = (0, 0)
            position = add_position(position, mult_position(distance, direction))
        else:
            vertical_distance = add_position(
                vertical_distance, mult_position(distance, direction)
            )
        prev_moving_state = current_moving_state
    result += position[0]
print(result)
