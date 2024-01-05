import math

filename = "./Day 17/example.txt"
MIN_STEPS = 4
MAX_STEPS = 10
# Steps:
# 1. Read input
with open(filename) as file:
    maps = [line.strip() for line in file.readlines()]

# 2. This will probably be astar problem

LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)


def add_position(pos1: tuple[int], pos2: tuple[int]) -> tuple[int]:
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])


def mult_position(multiplier, pos: tuple[int]) -> tuple[int]:
    return (multiplier * pos[0], multiplier * pos[1])


assert mult_position(3, (3, 1)) == (9, 3)
assert add_position((3, 0), (0, 1)) == (3, 1)


def get_tile(position: tuple[int], maps: list[str]) -> str:
    return maps[position[1]][position[0]]


def distance(start_position, end_position, maps):
    result = 0
    if start_position[0] == end_position[0]:
        if start_position[1] < end_position[1]:
            adder = 1
        else:
            adder = 0
        for y in range(
            min(start_position[1], end_position[1]) + adder,
            max(start_position[1], end_position[1]) + adder,
        ):
            result += int(get_tile((start_position[0], y), maps))
    elif start_position[1] == end_position[1]:
        if start_position[0] < end_position[0]:
            adder = 1
        else:
            adder = 0
        for x in range(
            min(start_position[0], end_position[0]) + adder,
            max(start_position[0], end_position[0]) + adder,
        ):
            result += int(get_tile((x, start_position[1]), maps))
    else:
        # print(start_position)
        # print(end_position)
        raise ValueError("Incorrect direction")
    if result == 0:
        raise ValueError("Incorrect pos")

    return result


assert distance((0, 0), (3, 0), ["0123"]) == 6
assert distance((3, 0), (0, 0), ["0123"]) == 3
assert distance((0, 0), (0, 2), ["0", "1", "2", "3"]) == 3
assert distance((0, 2), (0, 0), ["0", "1", "2", "3"]) == 1


def djikstra(source_position, destination_position, heuristic):
    minimum_distance_to = {}
    f_score = {}
    current_direction_to = {}
    queue = []
    prev = {}

    start_x = source_position[0]
    start_y = source_position[1]

    for x in range(1 + (destination_position[0])):
        for y in range(1 + (destination_position[1])):
            for dirs in [UP, DOWN, LEFT, RIGHT]:
                minimum_distance_to[((start_x + x, start_y + y), dirs)] = math.inf
                f_score[((start_x + x, start_y + y), dirs)] = math.inf

                current_direction_to[((start_x + x, start_y + y), dirs)] = None
                prev[((start_x + x, start_y + y), dirs)] = None
    queue.append((source_position, DOWN))
    queue.append((source_position, RIGHT))
    minimum_distance_to[(source_position, DOWN)] = 0
    minimum_distance_to[(source_position, RIGHT)] = 0
    f_score[(source_position, DOWN)] = heuristic(source_position)
    f_score[(source_position, RIGHT)] = heuristic(source_position)

    while queue:
        temp = [f_score[vert] for vert in queue]
        current_position, prev_direction = queue.pop(temp.index(min(temp)))
        # printing progress
        # print(
        #     (
        #         current_position[0] / destination_position[0]
        #         + current_position[1] / destination_position[1]
        #     )
        #     / 2
        #     * 100
        # )
        if current_position == destination_position:
            break
        # neighbours
        neighbours = []
        directions_to_neighbours = []
        if prev_direction == UP or prev_direction == DOWN:
            directions_to_neighbours.append(LEFT)
            directions_to_neighbours.append(RIGHT)
        elif prev_direction is not None:
            directions_to_neighbours.append(UP)
            directions_to_neighbours.append(DOWN)
        for direction_to_neighbour in set(directions_to_neighbours):
            for steps in range(MIN_STEPS - 1, MAX_STEPS):
                neighbour = (
                    add_position(
                        current_position,
                        mult_position(1 + steps, direction_to_neighbour),
                    ),
                    direction_to_neighbour,
                )
                neighbours.append(neighbour)
                current_direction_to[neighbour] = direction_to_neighbour

        for neighbour, direction_to_neighbour in neighbours:
            if (neighbour, direction_to_neighbour) in minimum_distance_to.keys():
                new_distance = minimum_distance_to[
                    (current_position, prev_direction)
                ] + distance(current_position, neighbour, maps)
                if (
                    new_distance
                    < minimum_distance_to[(neighbour, direction_to_neighbour)]
                ):
                    minimum_distance_to[
                        (neighbour, direction_to_neighbour)
                    ] = new_distance
                    f_score[
                        (neighbour, direction_to_neighbour)
                    ] = new_distance + heuristic(neighbour)
                    prev[(neighbour, direction_to_neighbour)] = (
                        current_position,
                        prev_direction,
                    )
                    if (neighbour, direction_to_neighbour) not in queue:
                        queue.append((neighbour, direction_to_neighbour))

    return min(
        minimum_distance_to[destination_position, DOWN],
        minimum_distance_to[destination_position, RIGHT],
    )


destination_position = (len(maps[0]) - 1, len(maps) - 1)
average = (
    sum([sum([int(char) / len(line) for char in line]) / len(maps) for line in maps])
    / 2
)
average = 1


def linear_heuristic(position):
    return (
        1
        * average
        * (
            destination_position[1]
            + destination_position[0]
            - position[0]
            - position[1]
        )
    )


print(djikstra((0, 0), destination_position, linear_heuristic))
