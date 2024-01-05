import numpy as np

filename = "./Day 21/data.txt"
MAX_STEPS = 64

with open(filename) as file:
    lines = np.array([list(line.strip()) for line in file.readlines()])

starting_positions = lines == "S"
walls_masking = lines == "#"


def shift_left(starting_positions):
    width, height = starting_positions.shape
    return np.c_[starting_positions[:, 1:], np.zeros((width, 1)) > 0]


def shift_right(starting_positions):
    width, height = starting_positions.shape
    return np.c_[np.zeros((width, 1)) > 0, starting_positions[:, :-1]]


def shift_up(starting_positions):
    width, height = starting_positions.shape
    return np.r_[starting_positions[1:, :], np.zeros((1, height)) > 0]


def shift_down(starting_positions):
    width, height = starting_positions.shape
    return np.r_[np.zeros((1, height)) > 0, starting_positions[:-1, :]]


def move(starting_positions):
    return (
        shift_down(starting_positions)
        | shift_up(starting_positions)
        | shift_left(starting_positions)
        | shift_right(starting_positions)
    ) & (walls_masking == False)


for i in range(MAX_STEPS):
    starting_positions = move(starting_positions)
print(np.sum(starting_positions))
