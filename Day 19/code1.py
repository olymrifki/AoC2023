filename = "./Day 19/data.txt"


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

    def is_obeyed_by(self, parts: dict):
        if self.operation == ">":
            return parts[self.part] > self.value
        elif self.operation == "<":
            return parts[self.part] < self.value


assert Rule("a<2006:qkq").is_obeyed_by({"x": 787, "m": 2655, "a": 1222, "s": 2876})

assert not Rule("x<206:qkq").is_obeyed_by({"x": 787, "m": 2655, "a": 1222, "s": 2876})


class Container:
    def __init__(self, rules: str) -> None:
        rules = rules.split(",")
        self.last_contaienr_name = rules.pop()
        self.rules = [Rule(rule) for rule in rules]

    #         1.1.3 There is a function that can runs through the entire container rule and return the next container

    def get_next_container_name(self, parts: dict) -> str:
        for rule in self.rules:
            if rule.is_obeyed_by(parts):
                return rule.destination_container_name
        return self.last_contaienr_name


assert (
    Container("a<2006:qkq,m>2090:A,rfg").get_next_container_name(
        {"x": 787, "m": 2655, "a": 1222, "s": 2876}
    )
    == "qkq"
)
assert (
    Container("a<206:qkq,m<2090:A,rfg").get_next_container_name(
        {"x": 787, "m": 2655, "a": 1222, "s": 2876}
    )
    == "rfg"
)


def create_parts(string: str) -> dict:
    result = {}
    string = string[1:-1]
    string = string.split(",")
    for s in string:
        result[s[0]] = int(s[2:])
    return result


assert create_parts("{x=787,m=2655,a=1222,s=2876}") == {
    "x": 787,
    "m": 2655,
    "a": 1222,
    "s": 2876,
}
containers = {}
parts = []
with open(filename) as file:
    is_part = False
    for line in file.readlines():
        line = line.strip()
        if is_part:
            parts.append(create_parts(line))
            continue
        if line == "":
            is_part = True
            continue

        line = line[:-1]
        container_name, container_rules = line.split("{")
        containers[container_name] = Container(container_rules)


# print(containers)
# print(parts)
#         1.1.4 There is a function that accept parts and pass it to "in" container untill it reaches accepted or rejected


def filter_parts(
    parts: list[dict], containers: dict[str, Container]
) -> (list[dict[str, int]], list[dict[str, int]]):
    accepted_parts = []
    rejected_parts = []
    for part in parts:
        current_container_name = "in"
        while current_container_name not in "AR":
            current_container = containers[current_container_name]
            current_container_name = current_container.get_next_container_name(part)
        if current_container_name == "A":
            accepted_parts.append(part)
        else:
            rejected_parts.append(part)
    return accepted_parts, rejected_parts


#         1.1.5 There is one accepted and rejected container
#     1.2 Create list of parts dictionary

# 2. Run parts through containers and sum all values inside accepted container
accepted_parts, rejected_parts = filter_parts(parts, containers)
result = 0
for part in accepted_parts:
    result += sum(part.values())
print(result)
