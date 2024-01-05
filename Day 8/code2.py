# Given sequence of steps and nodes

# LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)

# count how many steps needed to go from AAA to ZZZ.
# Here, from AAA we take L to BBB then L to AAA then R to BBB then the steps loop with L to AAA then L to BBB then R to ZZZ with total of 6 steps


# Steps:
# 1. Read input to store sequence of steps and nodes
#     1.1 Each node will have L and R nodes
#     1.2 Save node AAA


def read_step_line(line: str) -> list[int]:
    step_map = {"L": 0, "R": 1}
    return [step_map[char] for char in line]


assert read_step_line("LLR") == [0, 0, 1]

node_dict = {}


def generate_node(line: str) -> None:
    node_name, line = line.split(" = ")
    left_node = line[1:4]
    right_node = line[6:9]
    node_dict[node_name] = (left_node, right_node)


generate_node("BBB = (AAA, ZZZ)")
assert node_dict == {"BBB": ("AAA", "ZZZ")}
node_dict = {}

with open("./Day 8/data.txt") as file:
    lines = file.readlines()
    steps = read_step_line(lines[0].strip())

    for line in lines[2:]:
        generate_node(line.strip())

starting_nodes = [node for node in node_dict.keys() if node[-1] == "A"]
print(starting_nodes)


# 2. starting from node AAA:
def get_step_counts(current_node: str) -> int:
    step_count = 0
    total_steps = len(steps)
    print(node_dict)
    print(steps)
    #     2.1 Follow each step. In each step, add step count,
    while current_node[-1] != "Z":
        current_node = node_dict[current_node][steps[step_count % total_steps]]
        step_count += 1
    return step_count


step_counts = [get_step_counts(current_node) for current_node in starting_nodes]


# following wikipedia algorithm
def gcm(a: int, b: int) -> int:
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def lcm(a: int, b: int) -> int:
    return int(a * b / gcm(a, b))


# copied from internet, not importing functool
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value


#     2.2 then check if this next node is ZZZ. If so, end follow

step_count = reduce(lcm, step_counts)
print(step_count)
