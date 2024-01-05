import math

filename = "./Day 23/example.txt"
# Steps
# 1. Read input

# 2. We need to be able to mark turnable points. This will be our node
#     2.1 A turnable point is a point where it is empty, there is atleast one empty space at its left or right and atleast one spacce at its up or down sides.
#     2.2 Mark every point with this property
maze = []
with open(filename) as file:
    maze = [s.strip() for s in file.readlines()]
    for y in range(1, len(maze) - 1):
        for x in range(1, len(maze[0]) - 1):
            if maze[y][x] == ".":
                if (maze[y][x + 1] in ".><^v" or maze[y][x - 1] in ".><^v") and (
                    maze[y + 1][x] in ".><^v" or maze[y - 1][x] in ".><^v"
                ):
                    maze[y] = maze[y][:x] + "+" + maze[y][x + 1 :]
for line in maze:
    print(line)


# 3. Longest path maybe can be found using djikstra modification


def get_neighbour_positions(node_position: tuple[int], maze):
    result = []
    # up
    for y in range(node_position[1] - 1, 0, -1):
        if maze[y][node_position[0]] not in "+.^":
            break
        elif maze[y][node_position[0]] == "+":
            result.append((node_position[0], y))
            break

    # low
    for y in range(node_position[1] + 1, len(maze) - 1):
        if maze[y][node_position[0]] not in "+.v":
            break
        elif maze[y][node_position[0]] == "+":
            result.append((node_position[0], y))
            break

    # left
    for x in range(node_position[0] - 1, 0, -1):
        if maze[node_position[1]][x] not in "+.<":
            break
        elif maze[node_position[1]][x] == "+":
            result.append((x, node_position[1]))
            break

    # right
    for x in range(node_position[0] + 1, len(maze[0]) - 1):
        if maze[node_position[1]][x] not in "+.>":
            break
        elif maze[node_position[1]][x] == "+":
            result.append((x, node_position[1]))
            break

    return result


class Node:
    def __init__(self, position, prev=None) -> None:
        self.position = position
        self.prev = prev

    def is_not_from(self, other) -> bool:
        prev = self.prev
        current_node = self
        while prev:
            if prev.position == other.position:
                return False
            current_node = prev
            prev = current_node.prev
        return True

    def __eq__(self, __value: object) -> bool:
        if self.position == __value.position:
            if self.prev is None:
                return __value.prev is None
            elif __value.prev is None:
                return False
            if self.prev.position == __value.prev.position:
                return True
        return False


max_path_length = 0


def find_max_path(source, destination, current_path_length):
    global max_path_length
    if source.position == destination.position:
        max_path_length = max(max_path_length, current_path_length)
        return
    # neighbours
    neighbours = [
        Node(neighbour, source)
        for neighbour in get_neighbour_positions(source.position, maze)
    ]
    if source.prev:
        neighbours = [n for n in neighbours if n.position != source.prev.position]

    for neighbour in neighbours:
        find_max_path(
            neighbour,
            destination,
            current_path_length
            + abs(source.position[0] - neighbour.position[0])
            + abs(source.position[1] - neighbour.position[1]),
        )


# assert Node((0, 0, 0)) in [Node((0, 0, 0), Node((1, 1)))]
find_max_path(Node((1, 1)), Node((len(maze[0]) - 2, len(maze) - 2)), 0)
print(2 + max_path_length)

# temp = """#S#####################
# #OOOOOOO#########...###
# #######O#########.#.###
# ###OOOOO#OOO>.###.#.###
# ###O#####O#O#.###.#.###
# ###OOOOO#O#O#.....#...#
# ###v###O#O#O#########.#
# ###...#O#O#OOOOOOO#...#
# #####.#O#O#######O#.###
# #.....#O#O#OOOOOOO#...#
# #.#####O#O#O#########v#
# #.#...#OOO#OOO###OOOOO#
# #.#.#v#######O###O###O#
# #...#.>.#...>OOO#O###O#
# #####v#.#.###v#O#O###O#
# #.....#...#...#O#O#OOO#
# #.#########.###O#O#O###
# #...###...#...#OOO#O###
# ###.###.#.###v#####O###
# #...#...#.#.>.>.#.>O###
# #.###.###.#.###.#.#O###
# #.....###...###...#OOO#
# #####################O#"""
# print(sum([1 for char in temp if char == "O"]))
