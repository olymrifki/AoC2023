from enum import Enum
from typing import Protocol

filname = "./Day 20/data.txt"


class Pulse(Enum):
    HIGH = 1
    LOW = 2


# Steps:
# 0. Read all input and create module dictionary hashed by its name (after prefix)
# 1. Create class for broadcaster, flip-flop, and conjunction modules


class Transmission:
    def __init__(self, pulse: Pulse, sender: str, receiver: str) -> None:
        self.pulse = pulse
        self.sender = sender
        self.receiver = receiver


class Module(Protocol):
    def receive_and_send_transmission(
        self, transmission: Transmission
    ) -> list[Transmission]:
        ...


class Broadcaster:
    def __init__(self, name: str, destinations: tuple[str]) -> None:
        self.name = name
        self.destinations = destinations

    def receive_and_send_transmission(
        self, transmission: Transmission
    ) -> list[Transmission]:
        result = []
        for destination in self.destinations:
            result.append(Transmission(transmission.pulse, self.name, destination))
        return result


class FlipFlop:
    def __init__(self, name: str, destinations: tuple[str]) -> None:
        self.name = name
        self.destinations = destinations
        self.state = "OFF"

    def receive_and_send_transmission(
        self, transmission: Transmission
    ) -> list[Transmission]:
        result = []
        if transmission.pulse == Pulse.HIGH:
            return result

        if self.state == "OFF":
            output_pulse = Pulse.HIGH
            self.state = "ON"
        else:
            output_pulse = Pulse.LOW
            self.state = "OFF"

        for destination in self.destinations:
            result.append(Transmission(output_pulse, self.name, destination))
        return result


class Conjunction:
    def __init__(
        self, name: str, destinations: tuple[str], input_names: list[str]
    ) -> None:
        self.name = name
        self.destinations = destinations
        self.last_input_pulses = {input_name: Pulse.LOW for input_name in input_names}

    def is_all_input_high(self) -> bool:
        return sum(v.value for v in self.last_input_pulses.values()) == len(
            self.last_input_pulses.values()
        )

    def receive_and_send_transmission(
        self, transmission: Transmission
    ) -> list[Transmission]:
        result = []

        self.last_input_pulses[transmission.sender] = transmission.pulse
        if self.is_all_input_high():
            output_pulse = Pulse.LOW
        else:
            output_pulse = Pulse.HIGH

        for destination in self.destinations:
            result.append(Transmission(output_pulse, self.name, destination))
        return result


assert Conjunction("AAA", ("1",), ["E", "s"]).is_all_input_high() == False


# 2. Each class can *recieve a pulse* and schedule the broadcasted pulse into a buffer
def get_all_sender_names(module_name: str, lines: list[str]) -> list[str]:
    result = []
    for line in lines:
        sender_name, destination_names = line.split(" -> ")
        sender_name = sender_name[1:]
        if module_name in destination_names:
            result.append(sender_name)
    return result


# 3. Initially, the buffer will be sending low pulse into broadcaster (this is why we dont create button module)
def press_button(modules: dict[str, Module]) -> tuple[int, int]:
    buffer = [Transmission(Pulse.LOW, "button", "broadcaster")]
    high_pulse_count = 0
    low_pulse_count = 0
    while buffer:
        current_transmission = buffer.pop(0)
        if current_transmission.pulse == Pulse.HIGH:
            high_pulse_count += 1
        elif current_transmission.pulse == Pulse.LOW:
            low_pulse_count += 1
        else:
            raise ValueError("Incorrect pulse type")
        try:
            current_module = modules[current_transmission.receiver]
        except KeyError:
            continue
        buffer += current_module.receive_and_send_transmission(current_transmission)
    return high_pulse_count, low_pulse_count


# 4. Record each pulse that happen when reading the buffer
# 5. After the buffer is emptied, one cycle is done. Add low and high pulse count to button push score, reset the pulse count.
# 6. Calculate score.


def calculate_score(scores: list[tuple[int, int]]) -> (int, int):
    high_score = sum(s[0] for s in scores)
    low_score = sum(s[1] for s in scores)
    return high_score, low_score


modules = {}
with open(filname) as file:
    lines = [line.strip() for line in file.readlines()]
    for line in lines:
        module_name, destination_names = line.split(" -> ")
        module_type = module_name[0]
        module_name = module_name[1:]
        destination_names = tuple(destination_names.split(", "))
        if module_type == "&":
            sender_names = get_all_sender_names(module_name, lines)
            modules[module_name] = Conjunction(
                module_name, destination_names, sender_names
            )
        elif module_type == "%":
            modules[module_name] = FlipFlop(module_name, destination_names)
        elif module_type == "b":
            modules["broadcaster"] = Broadcaster("broadcaster", destination_names)
        else:
            raise ValueError(f"No modules with type code: '{module_type}'")
high, low = calculate_score([press_button(modules) for _ in range(1000)])
print(high * low)


# This is a shame corner of premature optimmization
# I initially thought the calculation will be expensive in the second problem, but thats not the case :)
# so i tried this cycle detection for an hour that did not work
# because i cant calculate the period if there is repeating element among (us) nonrepeating elements

# this is modified from stackoverflow trying to calculate period
# def guess_seq_len(seq):
#     max_len = int(len(seq) / 2)
#     for x in range(1, max_len):
#         if seq[0:x] == seq[x : 2 * x]:
#             for y in range(max_len - 1, 0, -1):
#                 if seq[0:y] == seq[y : 2 * y]:
#                     if x == y:
#                         return x

#     return -1


# # this is a floyd cycle checker from wikipedia
# def is_cycle(sequence: list[tuple[int, int]]) -> (bool, int):
#     if len(sequence) <= 2:
#         return False, 0, 0
#     tortoise = 1
#     hare = 2
#     try:
#         while sequence[tortoise] != sequence[hare]:
#             tortoise += 1
#             hare += 2

#         starting_index = 0
#         tortoise = 0
#         while sequence[tortoise] != sequence[hare]:
#             tortoise += 1
#             hare += 1
#             starting_index += 1

#         return True, starting_index
#     except IndexError:
#         return False, 0, 0


# assert is_cycle([3, 1, 2, 2, 1, 2, 2, 1, 2, 2]) == (True, 1)
# assert is_cycle([3, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2]) == (True, 1)
# # print(is_cycle([1, 2, 3, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]))
# assert is_cycle([1, 2, 3, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == (True, 3)
