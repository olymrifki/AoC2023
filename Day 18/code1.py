filename = "./Day 18/example1.txt"

directions = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, -1),
    "D": (0, 1),
}


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
        direction, distance, color = line.split(" ")
        direction = directions[direction]
        distance = int(distance)
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

print(min_pos, max_pos)
map_size = (max_pos[0] - min_pos[0] + 1, max_pos[1] - min_pos[1] + 1)
print(map_size)
maps = ["." * map_size[0] for _ in range(map_size[1])]

with open("./Day 18/temp1.txt", "w") as f_write:
    for line in maps:
        f_write.write(f"{line}\n")
    print("Done")


def change_string_character(string: str, index, new_character):
    return string[:index] + new_character + string[index + 1 :]


def change_position_to_wall(position: tuple[int], maps: list[str]) -> list[str]:
    result = maps.copy()
    result[position[1]] = change_string_character(result[position[1]], position[0], "#")
    return result


position = add_position((0, 0), mult_position(-1, min_pos))
positions = [position]
maps = change_position_to_wall(position, maps)
with open(filename) as file:
    for line in file.readlines():
        line = line.strip()
        direction, distance, color = line.split(" ")
        direction = directions[direction]
        distance = int(distance)
        for i in range(distance):
            changed_position = add_position(position, mult_position(1 + i, direction))
            positions.append(changed_position)
            maps = change_position_to_wall(changed_position, maps)
        position = add_position(position, mult_position(distance, direction))

with open("./Day 18/temp.txt", "w") as f_write:
    for line in maps:
        f_write.write(f"{line}\n")
    print("Done")
# 2. Loop detection wil be similar to Day 10 solution, without the flood fill
# from day 10
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


def is_position_not_in_map(position: tuple[int], maps) -> bool:
    if position[0] < 0 or position[0] >= len(maps[0]):
        return True
    elif position[1] < 0 or position[1] >= len(maps):
        return True
    return False


def fill_map(position: tuple[int], maps) -> None:
    result = maps.copy()
    result[position[1]] = change_string_character(result[position[1]], position[0], "#")
    return result


def get_current_char(position, maps):
    return maps[position[1]][position[0]]


def flood_fill(initial_position: tuple[int], maps) -> (bool, list[str]):
    # return true if floodfill success
    old_maps = maps.copy()
    queue = []
    maps = fill_map(initial_position, maps)
    queue.append(initial_position)
    while queue:
        position = queue.pop(0)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for direction in directions:
            new_position = add_position(position, direction)
            if is_position_not_in_map(new_position, maps):
                return False, old_maps
            current_char = get_current_char(new_position, maps)
            if current_char != "#":
                maps = change_position_to_wall(new_position, maps)
                queue.append(new_position)

    return True, maps


def fill_interior_by_one(direction_to_fill_map, maps):
    old_maps = maps.copy()
    for i in range(1, len(positions)):
        direction = (
            positions[i][0] - positions[i - 1][0],
            positions[i][1] - positions[i - 1][1],
        )

        for delta in direction_to_fill_map[direction]:
            initial_position = add_position(positions[i], delta)
            if is_position_not_in_map(initial_position, maps):
                continue
            current_char = get_current_char(initial_position, maps)
            if current_char not in "#":
                is_valid, maps = flood_fill(initial_position, maps)
                if not is_valid:
                    return old_maps, old_maps, False
    return maps, old_maps, True


result, maps, is_success = fill_interior_by_one(ccw_left_direction_to_fill_map, maps)
if is_success:
    with open("./Day 18/temp1.txt", "w") as f_write:
        for line in result:
            f_write.write(f"{line}\n")
        print("Done")


score = 0
for line in result:
    for char in line:
        if char == "#":
            score += 1
print(score)
result, maps, is_success = fill_interior_by_one(cw_right_direction_to_fill_map, maps)
if is_success:
    with open("./Day 18/temp1.txt", "w") as f_write:
        for line in result:
            f_write.write(f"{line}\n")
        print("Done")


score = 0
for line in result:
    for char in line:
        if char == "#":
            score += 1
print(score)
