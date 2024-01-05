filename = "./Day 9/data.txt"
# Steps:
# 1. Read all lines and generate list of sequence
line = "0 3 6 9 12 15"


def get_sequence(line: str) -> list[int]:
    return [int(number) for number in line.split(" ")]


assert get_sequence(line) == [0, 3, 6, 9, 12, 15]

with open(filename) as file:
    sequences = [get_sequence(line) for line in file.readlines()]

# 2. For each sequence:
#     2.1 Get the last element add them to prediction
#     2.2 Generate new sequence containing the difference of the element
#     2.3 Check if the difference is all 0


def is_over(sequece: list[int]) -> bool:
    for element in sequece:
        if element != 0:
            return False
    return True


def get_prediction(sequence: list[int]) -> int:
    prediction = sequence[0]
    sign = -1
    while not is_over(sequence):
        sequence = [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]
        prediction += sign * sequence[0]
        sign *= -1
    return prediction


# 3. Add all predictions

print(sum(get_prediction(seq) for seq in sequences))
