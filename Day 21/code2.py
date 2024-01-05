import numpy as np

filename = "./Day 21/data.txt"
MAX_STEPS = 26501365
MAX_ITERATION = 2000
PATTERN_LENGTH = 5

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


def add_padding_of_zeros(starting_positions):
    width, height = starting_positions.shape
    starting_positions = np.c_[
        np.zeros((width, 1)) > 0, starting_positions, np.zeros((width, 1)) > 0
    ]

    starting_positions = np.r_[
        np.zeros((1, height + 2)) > 0, starting_positions, np.zeros((1, height + 2)) > 0
    ]
    return starting_positions


def move(starting_positions):
    return (
        shift_down(starting_positions)
        | shift_up(starting_positions)
        | shift_left(starting_positions)
        | shift_right(starting_positions)
    ) & (walls_masking == False)


def create_3by3_pattern(starting_positions):
    starting_positions = np.c_[
        starting_positions, starting_positions, starting_positions
    ]

    starting_positions = np.r_[
        starting_positions, starting_positions, starting_positions
    ]
    return starting_positions


pattern = 131  # this is the size of our (square) input
target_modulo = MAX_STEPS % pattern
# print(target_modulo)

starting_positions = add_padding_of_zeros(starting_positions)
walls_masking = add_padding_of_zeros(walls_masking)
escaped_path = (
    add_padding_of_zeros(np.ones_like(starting_positions[1:-1, 1:-1])) == False
)

borders = 0
temp1 = []
temp2 = []
for i in range(MAX_ITERATION):
    # print(temp1)
    borders = np.sum(starting_positions & escaped_path)
    if (
        (i > int(MAX_ITERATION / 5))
        and (i % pattern == target_modulo)
        and (len(temp1) < PATTERN_LENGTH)
    ):
        temp2.append(i)
        temp1.append(np.sum(starting_positions))
        if len(temp1) == PATTERN_LENGTH:
            print(f"Insert this pattern to wolfram alpha {temp1}")
            print(f"substitute at n={(MAX_STEPS-temp2[0])//pattern+1}")
            break
    if borders > 0:
        # print(i, borders)
        walls_masking = add_padding_of_zeros(
            create_3by3_pattern(walls_masking[1:-1, 1:-1])
        )
        temp = np.zeros_like(walls_masking)
        w, h = starting_positions[1:-1, 1:-1].shape
        temp[w : 2 * w + 2, h : 2 * h + 2] = starting_positions
        starting_positions = temp
        escaped_path = (
            add_padding_of_zeros(np.ones_like(starting_positions[1:-1, 1:-1])) == False
        )

    starting_positions = move(starting_positions)
else:
    print(
        f"This is the pattern, it might need more iterations. Current max iteration: {MAX_ITERATION}"
    )
    print(f"Insert this pattern to wolfram alpha {temp1}")
    print(f"substitute at n={(MAX_STEPS-temp2[0])//pattern+1}")
