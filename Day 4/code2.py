# Given list of _original card_
# """Card 1: 41 48 83 86 17 | 83 86 6 31 17 9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3: 1 21 53 59 44 | 69 82 63 72 16 21 14 1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58 5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
# *Total card*s here are 30
# Where each _line_
# """Card 1: 41 48 83 86 17 | 83 86 6 31 17 9 48 53"""
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


# Calculate _match score_:
def calculate_match_score(line: str) -> int:
    # Compare list of _winning numbers_ to some _random numbers_ of numbers.
    # For each number in _random numbers_, if the number is in the _winning numbers_, add _match score_
    winning_numbers = get_winning_numbers(line)
    random_numbers = get_random_numbers(line)
    match_score = sum([1 for number in random_numbers if number in winning_numbers])
    return match_score


# Create _memo of added card_
added_card_memo = []
# Get all lines
with open("./Day 4/data.txt") as file:
    lines = list(file.readlines())

# Create queue of lines: containing _line index_
line_queue = [line_index for line_index in range(len(lines))]
# line queue is reversed so that the next line index's added card value already calculated, preventing more than 1 recursion
line_queue.reverse()


def calculate_added_cards(line_index: int) -> int:
    # Count added card from current line index
    # Because we work in reversed lines, index of memo will be len(lines) - line_index - 1
    memo_index = len(lines) - line_index - 1
    if memo_index < len(added_card_memo):
        # if line it is already compared:
        # get _added card_ from _memo of added card_
        added_card = added_card_memo[memo_index]
    else:
        # Otherwise: calculate _added card_ from current card and each next card if _match score_ is positive
        added_card = 1  # current card
        match_score = calculate_match_score(lines[line_index])
        # If _match score_ is positive, say n, add extra _added card_ from next n _copy card_ from n _line index_ below current one
        for new_line_index in range(1 + line_index, 1 + line_index + match_score):
            if new_line_index < len(lines):
                added_card += calculate_added_cards(new_line_index)
        # Add _added card_ to memo
        added_card_memo.append(added_card)
    return added_card


while line_queue:
    #  pop queue for next line
    calculate_added_cards(line_queue.pop(0))

# after all lines get memod, add all memod card
print(sum(number for number in added_card_memo))
