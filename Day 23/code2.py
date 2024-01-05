import sys

sys.setrecursionlimit(15000)
filename = "./Day 23/data.txt"
# Steps
# 1. Read input

# 2. We need to be able to mark turnable points. This will be our node
#     2.1 A turnable point is a point where it is empty, there is atleast one empty space at its left or right and atleast one spacce at its up or down sides.
#     2.2 Mark every point with this property
maze = []
nodes_position = []
with open(filename) as file:
    maze = [s.strip() for s in file.readlines()]
    for y in range(1, len(maze) - 1):
        for x in range(1, len(maze[0]) - 1):
            if maze[y][x] == ".":
                if (maze[y][x + 1] in ".><^v" or maze[y][x - 1] in ".><^v") and (
                    maze[y + 1][x] in ".><^v" or maze[y - 1][x] in ".><^v"
                ):
                    maze[y] = maze[y][:x] + "+" + maze[y][x + 1 :]
                    nodes_position.append((x, y))
# for line in maze:
#     print(line)


# 3. Longest path maybe can be found using djikstra modification


def get_neighbour_positions(node_position: tuple[int], maze):
    result = []
    # up
    for y in range(node_position[1] - 1, 0, -1):
        if maze[y][node_position[0]] not in "+.><^v":
            break
        elif maze[y][node_position[0]] == "+":
            result.append((node_position[0], y))
            break

    # low
    for y in range(node_position[1] + 1, len(maze) - 1):
        if maze[y][node_position[0]] not in "+.><^v":
            break
        elif maze[y][node_position[0]] == "+":
            result.append((node_position[0], y))
            break

    # left
    for x in range(node_position[0] - 1, 0, -1):
        if maze[node_position[1]][x] not in "+.><^v":
            break
        elif maze[node_position[1]][x] == "+":
            result.append((x, node_position[1]))
            break

    # right
    for x in range(node_position[0] + 1, len(maze[0]) - 1):
        if maze[node_position[1]][x] not in "+.><^v":
            break
        elif maze[node_position[1]][x] == "+":
            result.append((x, node_position[1]))
            break

    return result


class Node:
    def __init__(self, position, prev=None) -> None:
        self.position = position
        self.prev = []
        if prev:
            self.prev = [prev]


max_path_length = 0


is_visited = [[False for _ in maze[0]] for __ in maze]

# maps node to all its neighbours and distance
nodes_memo = {}

source = Node((1, 1))
for position in nodes_position:
    neighbours = [
        Node(temp, position) for temp in get_neighbour_positions(position, maze)
    ]
    distances = [
        abs(position[0] - n.position[0]) + abs(position[1] - n.position[1])
        for n in neighbours
    ]

    for i in range(len(neighbours)):
        temp_position = neighbours[i].position
        temp_dist = distances[i]
        prev_position = position
        while True:
            # if still one path (one neighbour)
            newest_neighbours = [
                Node(newest_neighbour, temp_position)
                for newest_neighbour in get_neighbour_positions(temp_position, maze)
                if newest_neighbour != prev_position
            ]
            if len(newest_neighbours) != 1:
                break
            prev_position = temp_position
            temp_dist += abs(temp_position[0] - newest_neighbours[0].position[0]) + abs(
                temp_position[1] - newest_neighbours[0].position[1]
            )
            temp_position = newest_neighbours[0].position

        neighbours[i].position = temp_position
        distances[i] = temp_dist
    # print(distances)

    # filling memo
    temp = [(neighbours[i].position, distances[i]) for i in range(len(neighbours))]
    nodes_memo[position] = nodes_memo.get(position, []) + temp


def find_max_path(source, destination, current_path_length):
    global max_path_length
    if is_visited[source.position[1]][source.position[0]]:
        return

    is_visited[source.position[1]][source.position[0]] = True
    if source.position == destination.position:
        if max_path_length < current_path_length:
            max_path_length = current_path_length
            print(max_path_length)
        is_visited[source.position[1]][source.position[0]] = False
        return

    if source.position in nodes_memo.keys():
        memod = [
            temp
            for temp in nodes_memo[source.position]
            if not is_visited[temp[0][1]][temp[0][0]]
        ]
        neighbours = [Node(temp[0], source.position) for temp in memod]
        distances = [temp[1] for temp in memod]
    else:
        raise ValueError(f"No position {source.position} in memo")

    for i in range(len(neighbours)):
        new_length = current_path_length + distances[i]
        find_max_path(neighbours[i], destination, new_length)

    is_visited[source.position[1]][source.position[0]] = False


find_max_path(Node((1, 1)), Node((len(maze[0]) - 2, len(maze) - 2)), 0)

# print(nodes_memo)
print(2 + max_path_length)
