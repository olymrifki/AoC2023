Read line
"""Card 1: 41 48 83 86 17 | 83 86 6 31 17 9 48 53"""
The left is list of winning numbers and the right is list of random
Compare list of winning numbers to some random list of numbers.
For each number in random list, if the number is in the winning numbers, add match score
If no match score, final score is 0
else final score is 2^(match score - 1)
Add all final score for each line of card
