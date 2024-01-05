filename = "./Day 16/data.txt"
# Steps:
# 1. Read inputs and set outputs to all 0s with the same size as input map
maps = []
scoreboard = []
with open(filename) as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        # line = line.replace("\.", "")
        maps.append(line)

for i in range(len(maps)):
    scoreboard.append([[] for _ in range(len(maps[0]))])

directions = {
    "right": (1, 0),
    "left": (-1, 0),
    "up": (0, -1),
    "down": (0, 1),
}


class Beam:
    def __init__(self, position: tuple[int], direction: str) -> None:
        # print(position)
        # print(direction)
        self.position = position
        self.direction = direction
        scoreboard[position[1]][position[0]].append(direction)


def get_tile(position: tuple[int], maps: list[str]) -> str:
    return maps[position[1]][position[0]]


def is_position_valid(position: tuple[int], maps: list[str]) -> bool:
    return (
        position[0] >= 0
        and position[0] < len(maps[0])
        and position[1] >= 0
        and position[1] < len(maps)
    )


def is_position_not_visited(
    position: tuple[int],
    direction: str,
):
    return direction not in scoreboard[position[1]][position[0]]


def add_position(pos1: tuple[int], pos2: tuple[int]) -> tuple[int]:
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])


# 2. Create list of beam with first element at top left to the right. Each beam will know its position and direction


#     2.1 Beam creation will mark output map to 1  at its position
#     2.2 To move the beam:
#         remove beam from list
#         for each beam:
#             get tile in its position
#             if position is possible:
#                 create new tile(s) with its direction and position
#             add it to list of beam
def move(beam: Beam, maps: list[str]) -> list[Beam]:
    result = []
    tile = get_tile(beam.position, maps)
    if tile == ".":
        next_beam_map = {
            "right": ["right"],
            "left": ["left"],
            "up": ["up"],
            "down": ["down"],
        }
    elif tile == "/":
        next_beam_map = {
            "right": ["up"],
            "left": ["down"],
            "up": ["right"],
            "down": ["left"],
        }
    elif tile == "\\":
        next_beam_map = {
            "right": ["down"],
            "left": ["up"],
            "up": ["left"],
            "down": ["right"],
        }
    elif tile == "-":
        next_beam_map = {
            "right": ["right"],
            "left": ["left"],
            "up": ["left", "right"],
            "down": ["left", "right"],
        }
    elif tile == "|":
        next_beam_map = {
            "right": ["up", "down"],
            "left": ["up", "down"],
            "up": ["up"],
            "down": ["down"],
        }
    for next_direction in next_beam_map[beam.direction]:
        if is_position_valid(
            add_position(beam.position, directions[next_direction]), maps
        ) and is_position_not_visited(
            add_position(beam.position, directions[next_direction]), next_direction
        ):
            result.append(
                Beam(
                    add_position(beam.position, directions[next_direction]),
                    next_direction,
                )
            )
        else:
            pass
            # print("beam destroyed")
    # for s in scoreboard:
    #     print(s)
    return result


beams = [Beam((0, 0), "right")]
while beams:
    beam = beams.pop(0)
    beams += move(beam, maps)
# 3. Add all output map
print(sum([sum([bool(s) for s in scoreboard[j]]) for j in range(len(scoreboard))]))
