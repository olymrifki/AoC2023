# Read line
# """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"""
example = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"


# The left is list of winning numbers and the right is list of random
def get_winning_numbers(line: str) -> list[int]:
    """Get list of winning numbers (left of |) from a line
    Line example:
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    """
    string_of_winning_numbers = line.split(": ")[1].split(" |")[0].split()
    return [int(number) for number in string_of_winning_numbers]


def get_random_numbers(line: str) -> list[int]:
    """Get list of winning random (right of |) from a line
    Line example:
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    """
    string_of_random_numbers = line.split("| ")[1].split()
    return [int(number) for number in string_of_random_numbers]


def get_final_score(line: str) -> int:
    """Get game final score from a line
    Line example:
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    """
    # Compare list of winning numbers to some random list of numbers.
    # For each number in random list, if the number is in the winning numbers, add match score
    winning_numbers = get_winning_numbers(line)
    random_numbers = get_random_numbers(line)
    match_score = [1 for number in random_numbers if number in winning_numbers]
    # If no match score, final score is 0
    # else final score is 2^(match score - 1)
    # Add all final score for each line of card
    final_score = 0
    if match_score:
        final_score = pow(2, sum(match_score) - 1)
    return final_score


with open("./Day 4/data.txt") as file:
    print(sum([get_final_score(line) for line in file.readlines()]))
