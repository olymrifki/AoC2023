filename = "./Day 19/data.txt"


# Each part still be dictionary containing its range (ex: {"x":[1:300], ...})

# We can imagine each rule is possibly going to be slicing the part into two parts
# one part will go the next container and the other will continue
#     The part that will go to the next container will be saved in some buffer before being processed later. Initial buffer: [("in",{"x":[1,4000],"m":[1,4000],"a":[1,4000],"s":[1,4000]})]
#     we keep processing until the buffer is empty (all parts into A or R)

# In combination calculation:
#     In a part range, the total part count will be the product if each x,m,a,s possible combination
#     Sum all part counts


class Parts:
    def __init__(
        self,
        x_range: tuple[int],
        m_range: tuple[int],
        a_range: tuple[int],
        s_range: tuple[int],
    ) -> None:
        self.ranges = {"x": x_range, "m": m_range, "a": a_range, "s": s_range}

    def __repr__(self) -> str:
        return str(self.ranges)

    def get_combinations(self) -> int:
        return (
            (self.ranges["x"][1] - self.ranges["x"][0] + 1)
            * (self.ranges["m"][1] - self.ranges["m"][0] + 1)
            * (self.ranges["a"][1] - self.ranges["a"][0] + 1)
            * (self.ranges["s"][1] - self.ranges["s"][0] + 1)
        )


def is_in_range(rang: tuple[int], value: int) -> bool:
    return (rang[0] <= value) and (value <= rang[1])


# Steps:
# 1. Read input
#     1.1 Create dictionary of rules and its container
#         1.1.1 Each rule container can be initialized by the conditions inside {}
class Rule:
    def __init__(self, rule: str) -> None:
        self.part = rule[0]
        self.operation = rule[1]
        value, self.destination_container_name = rule[2:].split(":")
        self.value = int(value)
        if self.operation not in "<>":
            raise ValueError("Incorrect rule operation")

    #         1.1.2 There is a function that accept parts and a single rule and return true or false

    def separate_passing_parts_to_(self, parts: Parts) -> (Parts, Parts):
        if is_in_range(parts.ranges[self.part], self.value):
            passing_parts = Parts(
                parts.ranges["x"],
                parts.ranges["m"],
                parts.ranges["a"],
                parts.ranges["s"],
            )

            non_passing_parts = Parts(
                parts.ranges["x"],
                parts.ranges["m"],
                parts.ranges["a"],
                parts.ranges["s"],
            )
            if self.operation == ">":
                passing_parts.ranges[self.part] = (
                    self.value + 1,
                    passing_parts.ranges[self.part][1],
                )
                non_passing_parts.ranges[self.part] = (
                    non_passing_parts.ranges[self.part][0],
                    self.value,
                )
            elif self.operation == "<":
                passing_parts.ranges[self.part] = (
                    passing_parts.ranges[self.part][0],
                    self.value - 1,
                )

                non_passing_parts.ranges[self.part] = (
                    self.value,
                    non_passing_parts.ranges[self.part][1],
                )

        else:
            # if value not in range, it is either greater or smaller than the range
            passing_parts = None
            non_passing_parts = parts
            if self.operation == ">":
                if parts.ranges[self.part][0] > self.value:
                    passing_parts = parts
                    non_passing_parts = None
            elif self.operation == "<":
                if parts.ranges[self.part][1] < self.value:
                    passing_parts = parts
                    non_passing_parts = None

        return (
            passing_parts,
            non_passing_parts,
        )


class Container:
    def __init__(self, rules: str) -> None:
        rules = rules.split(",")
        self.last_contaienr_name = rules.pop()
        self.rules = [Rule(rule) for rule in rules]

    #         1.1.3 There is a function that can runs through the entire container rule and return the next container

    def separate_parts(self, parts: Parts, buffer: list[tuple[str, Parts]]) -> str:
        for rule in self.rules:
            passing_parts, non_passing_parts = rule.separate_passing_parts_to_(parts)
            if passing_parts is not None:
                buffer.append((rule.destination_container_name, passing_parts))
            if non_passing_parts is None:
                return buffer
            parts = non_passing_parts

        buffer.append((self.last_contaienr_name, parts))
        return buffer


containers = {}
with open(filename) as file:
    for line in file.readlines():
        line = line.strip()
        if line == "":
            break

        line = line[:-1]
        container_name, container_rules = line.split("{")
        containers[container_name] = Container(container_rules)


# print(containers)
# print(parts)
#         1.1.4 There is a function that accept parts and pass it to "in" container untill it reaches accepted or rejected


def filter_parts(
    containers: dict[str, Container]
) -> (list[dict[str, int]], list[dict[str, int]]):
    accepted_parts = []
    rejected_parts = []
    buffer = [("in", Parts((1, 4000), (1, 4000), (1, 4000), (1, 4000)))]
    while buffer:
        # print(buffer)
        current_container_name, current_parts = buffer.pop(0)
        if current_container_name == "A":
            accepted_parts.append(current_parts)
        elif current_container_name == "R":
            rejected_parts.append(current_parts)
        else:
            current_container = containers[current_container_name]
            buffer = current_container.separate_parts(current_parts, buffer)

    return accepted_parts, rejected_parts


#         1.1.5 There is one accepted and rejected container
#     1.2 Create list of parts dictionary

# 2. Run parts through containers and sum all values inside accepted container
accepted_parts, rejected_parts = filter_parts(containers)
result = 0
# print(accepted_parts)
for part in accepted_parts:
    result += part.get_combinations()
print(result)
