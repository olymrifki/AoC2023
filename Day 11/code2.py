import math

filename = "./Day 11/data.txt"
EXPANSION_MULTIPLIER = 1_000_000
percentage1 = 0
# Steps:
# 1. Replace all empty rows and columns to *
all_maps = []
with open(filename) as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        all_maps.append(line)


def replace_char(char: str, position: int, string: str) -> str:
    return string[:position] + char + string[position + 1 :]


#     1.1 If any rows and columns that contains no #, duplicate it
def expand_rows(all_maps: list[str]) -> list[str]:
    result = all_maps.copy()
    initial_column_length = len(result)

    for i in range(initial_column_length):
        if "#" not in result[i]:
            result[i] = "*" * len(result[0])
    return result


def expand_columns(all_maps: list[str]) -> list[str]:
    result = all_maps.copy()
    initial_row_length = len(result[0])

    for i in range(initial_row_length):
        if "#" not in [result[j][i] for j in range(len(result))]:
            for j, string in enumerate(result):
                result[j] = replace_char("*", i, string)

    return result


def expand_map(all_maps: list[str]) -> list[str]:
    return expand_columns(expand_rows(all_maps))


assert expand_rows([".."]) == ["**"]
assert expand_columns([".#", ".."]) == ["*#", "*."]
assert expand_map([".#", ".."]) == ["*#", "**"]


# 2. Calculate minimum distance and add them
def distance(char: str) -> int:
    if char == "*":
        return EXPANSION_MULTIPLIER
    elif char in ".#":
        return 1


def get_char(position: list[int]):
    return all_maps[position[1]][position[0]]


def is_position_inside_box(box_start, box_end, position):
    return abs(position[0] - box_start[0]) <= abs(box_end[0] - box_start[0]) and abs(
        position[1] - box_start[1]
    ) <= abs(box_end[1] - box_start[1])


def djikstra(source_position, destination_position):
    dist = {}
    queue = []

    start_x = source_position[0]
    start_y = source_position[1]
    if source_position[0] < destination_position[0]:
        direction_x = 1
    else:
        direction_x = -1
    if source_position[1] < destination_position[1]:
        direction_y = 1
    else:
        direction_y = -1
    for x in range(1 + abs(source_position[0] - destination_position[0])):
        for y in range(1 + abs(source_position[1] - destination_position[1])):
            total_p2 += 1
            dist[(start_x + x * direction_x, start_y + y * direction_y)] = math.inf
            queue.append((start_x + x * direction_x, start_y + y * direction_y))
    dist[source_position] = 0
    while queue:
        temp = [dist[vert] for vert in queue]
        temp_vertex = queue.pop(temp.index(min(temp)))
        if temp_vertex == destination_position:
            break
        # neighbours
        neighbours = [
            (temp_vertex[0] + direction_x, temp_vertex[1]),
            (temp_vertex[0], temp_vertex[1] + direction_y),
        ]
        for neighbour in neighbours:
            if neighbour in queue:
                alt = dist[temp_vertex] + distance(get_char(neighbour))
                if alt < dist[neighbour]:
                    dist[neighbour] = alt

    return dist[destination_position]


def better_djikstra(source_position, destination_position):
    if source_position[0] < destination_position[0]:
        direction_x = 1
    else:
        direction_x = -1
    if source_position[1] < destination_position[1]:
        direction_y = 1
    else:
        direction_y = -1

    current_position = source_position
    dist = 0
    while current_position != destination_position:
        neighbours = [
            (current_position[0] + direction_x, current_position[1]),
            (current_position[0], current_position[1] + direction_y),
        ]

        if not is_position_inside_box(
            source_position, destination_position, neighbours[0]
        ):
            dist += distance(get_char(neighbours[1]))
            current_position = neighbours[1]
        elif not is_position_inside_box(
            source_position, destination_position, neighbours[1]
        ):
            dist += distance(get_char(neighbours[0]))
            current_position = neighbours[0]
        else:
            if distance(get_char(neighbours[0])) > distance(get_char(neighbours[1])):
                dist += distance(get_char(neighbours[1]))
                current_position = neighbours[1]
            else:
                dist += distance(get_char(neighbours[0]))
                current_position = neighbours[0]
    return dist


all_maps = expand_map(all_maps)
positions = [
    (i, j)
    for j in range(len(all_maps))
    for i in range(len(all_maps[0]))
    if all_maps[j][i] == "#"
]
print(len(positions))
result = 0
total_p1 = len(positions) * (len(positions) + 1) / 2
for i, position in enumerate(positions):
    for other_position in positions[i:]:
        print(f"{percentage1/total_p1*100:.2f}")
        percentage1 += 1
        result += better_djikstra(position, other_position)
print(result)
