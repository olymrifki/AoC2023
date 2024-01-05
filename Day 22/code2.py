import numpy as np

filename = "./Day 22/data.txt"


class Vector3:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"


class Brick:
    def __init__(self, start: Vector3, end: Vector3) -> None:
        self.supported_bricks = []
        self.start = start
        self.end = end

    def add_platform(self, string):
        self.supported_bricks.append(string)

    def __repr__(self) -> str:
        return f"({str(self.start)}, {str(self.end)})"

    # def __hash__(self) -> int:
    #     return hash(self.__repr__())


# Steps:
# 1. Read inputs
bricks = []
with open(filename) as file:
    lines = [line.strip() for line in file.readlines()]
    for line in lines:
        start_coordinate, end_coordinate = line.split("~")
        start_coordinate = [int(x) for x in start_coordinate.split(",")]
        start_coordinate = Vector3(*start_coordinate)
        end_coordinate = [int(x) for x in end_coordinate.split(",")]
        end_coordinate = Vector3(*end_coordinate)

        bricks.append(Brick(start_coordinate, end_coordinate))

x_min = min([brick.start.x for brick in bricks] + [brick.end.x for brick in bricks])
x_max = max([brick.start.x for brick in bricks] + [brick.end.x for brick in bricks])
y_min = min([brick.start.y for brick in bricks] + [brick.end.y for brick in bricks])
y_max = max([brick.start.y for brick in bricks] + [brick.end.y for brick in bricks])
z_min = min([brick.start.z for brick in bricks] + [brick.end.z for brick in bricks])
z_max = max([brick.start.z for brick in bricks] + [brick.end.z for brick in bricks])
positions_of_placed_bricks = np.zeros((x_max + 1, y_max + 1, z_max + 1))
brick_names = np.empty((x_max + 1, y_max + 1, z_max + 1), dtype=Brick)
positions_of_placed_bricks[:, :, 0] = 1
ground = Brick(Vector3(0, 0, 0), Vector3(0, 0, 0))
brick_names[positions_of_placed_bricks == 1] = ground


print(brick_names.shape)


# 2. Sort input from least to highest z coordinate

bricks = sorted(bricks, key=lambda brick: min(brick.start.z, brick.end.z))


# 3. Put least z to ground, and so on
#     3.1 During this process, find the nearest laid object and put it above this object.
#     3.2 We will use one numpy array of booleans for laid object position and one numpy array to store the objects identity.
#         3.2.1 We need to detect maximum and minimumm value of each axis.
#         3.2.2 For all x and y coordinates for this brick, search the nearest laid object. After nearest laid objects are found by its boolean value, get all of the objects in the other array, add them to this object's support. And fill the boolean array and the object array to this object.


def get_platform_indices_for(brick, positions_of_placed_bricks):
    indices = [
        (x, y)
        for x in range(brick.start.x, brick.end.x + 1)
        for y in range(brick.start.y, brick.end.y + 1)
    ]
    result = []
    for x, y in indices:
        line = positions_of_placed_bricks[x, y, ::-1]
        current_occupied_z = len(line) - 1 - np.argmax(line)
        result.append(current_occupied_z)
    max_z = max(result)
    result = np.rot90(
        np.array(
            [
                np.array((index[0], index[1], max_z))
                for i, index in enumerate(indices)
                if result[i] == max_z
            ]
        )
    )[::-1, :]
    return result


def place_brick(brick, positions_of_placed_bricks, brick_names):
    platform_indices = get_platform_indices_for(brick, positions_of_placed_bricks)
    for brick_name in set(
        brick_names[
            platform_indices[0, :],
            platform_indices[1, :],
            platform_indices[2, :],
        ]
    ):
        brick.add_platform(brick_name)

    lowest_z_index = platform_indices[2, 0] + 1

    indices = [
        (x, y, z)
        for x in range(brick.start.x, brick.end.x + 1)
        for y in range(brick.start.y, brick.end.y + 1)
        for z in range(brick.end.z + 1 - brick.start.z)
    ]
    placement_index = np.rot90(
        np.array(
            [
                np.array(
                    (
                        index[0],
                        index[1],
                        index[2] + lowest_z_index,
                    )
                )
                for index in indices
            ]
        )
    )[::-1, :]
    positions_of_placed_bricks[
        placement_index[0, :], placement_index[1, :], placement_index[2, :]
    ] = 1
    brick_names[
        placement_index[0, :], placement_index[1, :], placement_index[2, :]
    ] = brick


# 4. After all sorted list of bricks are laid, in all object, if the object does not support exactly one brick, add 1 it to result

for i, brick in enumerate(bricks):
    place_brick(brick, positions_of_placed_bricks, brick_names)

non_removable_bricks = []
str_bricks = [str(b) for b in bricks]
for brick in bricks:
    if len(brick.supported_bricks) == 1:
        non_removable_bricks += brick.supported_bricks
non_removable_bricks = set(non_removable_bricks)
non_removable_bricks.remove(ground)
# print(non_removable_bricks)
bricks_map = {brick: brick for brick in bricks}


def calculate_total_bricks_supported_by(base_brick):
    temps = {}
    base_bricks = [base_brick]
    result = set()
    while base_bricks:
        current_base_brick = base_bricks.pop(0)
        for brick in bricks:
            if brick not in result and current_base_brick in brick.supported_bricks:
                if len(brick.supported_bricks) == 1:
                    base_bricks.append(brick)
                    result.add(brick)
                    if temps.get(brick, None):
                        brick.supported_bricks = temps[brick]
                        del temps[brick]
                else:
                    if not temps.get(brick, None):
                        temps[brick] = brick.supported_bricks.copy()
                    brick.supported_bricks.remove(current_base_brick)
    if temps.keys():
        for key in temps.keys():
            bricks_map[key].supported_bricks = temps[key]

    return len(result)


temp = [calculate_total_bricks_supported_by(brick) for brick in non_removable_bricks]
print(sum(temp))
# print(max(temp))
print(sorted(temp))
