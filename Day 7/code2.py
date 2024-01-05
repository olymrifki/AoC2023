# Steps:
# 1. Read each line into hand and bid
class Hand:
    def __init__(self, line: str) -> None:
        self.hand, self.bid = line.strip().split()
        self.bid = int(self.bid)

    def __lt__(self, other):
        if get_type_strength(self.hand) < get_type_strength(other.hand):
            return True
        elif get_type_strength(self.hand) > get_type_strength(other.hand):
            return False
        for index in range(len(self.hand)):
            if get_label_strength(self.hand[index]) < get_label_strength(
                other.hand[index]
            ):
                return True
            elif get_label_strength(self.hand[index]) > get_label_strength(
                other.hand[index]
            ):
                return False
        return False

    # 2. Add comparison to Hand:
    #     2.1 Determine type strength of a Hand


def get_type_strength(hand: str) -> int:
    label_count = {}
    j_label_count = 0
    for label in hand:
        if label == "J":
            j_label_count += 1
            continue
        label_count[label] = label_count.get(label, 0) + 1

    counts = sorted(label_count.values(), reverse=True)
    if j_label_count > 0:
        if j_label_count == 5:
            counts = [5]
        else:
            counts[0] = counts[0] + j_label_count
    counts = tuple(counts)
    strength_map = {
        (1, 1, 1, 1, 1): 1,
        (2, 1, 1, 1): 2,
        (2, 2, 1): 3,
        (3, 1, 1): 4,
        (3, 2): 5,
        (4, 1): 6,
        (5,): 7,
    }
    return strength_map[counts]


print(get_type_strength("JQ1AJ"))


def get_label_strength(card: str) -> int:
    label_map = {
        "2": 1,
        "3": 2,
        "4": 3,
        "5": 4,
        "6": 5,
        "7": 6,
        "8": 7,
        "9": 8,
        "T": 9,
        "J": 0,
        "Q": 11,
        "K": 12,
        "A": 13,
    }
    return label_map[card]


#     2.2 Determine ordered card strength


# 3. Sort hand, sum the multiplied index+1 with its bids
with open("./Day 7/data.txt") as file:
    lines = file.readlines()
    hands = [Hand(line) for line in lines]

res = 0
for i, hand in enumerate(sorted(hands)):
    res += (i + 1) * hand.bid
print(res)
