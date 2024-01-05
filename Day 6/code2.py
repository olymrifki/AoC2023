# Steps:
# 1. Read list of time and list of distance

with open("./Day 6/data.txt") as file:
    lines = file.readlines()
    time = lines[0].split(":")[1].strip().split()
    time = [int("".join(time))]
    current_best_distances = lines[1].split(":")[1].strip().split()
    current_best_distances = [int("".join(current_best_distances))]


# 2. In a race, the number of win_count will be determined by:
#     2.1 Determine if a preparation time is a win:
#         speed = preparation_time
#         Win prep time will met:
#             best_distance < (max_time - preparation_time) * speed
def is_preparation_winning(preparation_time, max_time, best_distance):
    return best_distance < (max_time - preparation_time) * preparation_time


#     2.2 Then the win_count will be:
def get_win_count(max_time, best_distance):
    minimum_prep_time = 0
    maximum_prep_time = max_time
    while minimum_prep_time < maximum_prep_time and not is_preparation_winning(
        minimum_prep_time, max_time, best_distance
    ):
        minimum_prep_time += 1
    if minimum_prep_time == maximum_prep_time:
        return 0
    while minimum_prep_time < maximum_prep_time and not is_preparation_winning(
        maximum_prep_time, max_time, best_distance
    ):
        maximum_prep_time -= 1
    return maximum_prep_time - minimum_prep_time + 1


#         maximum_prep_time to win - minimum_prep_time to win + 1
# 3. Multiply all win_count
win_counts = [
    get_win_count(time[i], current_best_distances[i]) for i in range(len(time))
]
res = 1
for win_count in win_counts:
    res *= win_count
print(res)
