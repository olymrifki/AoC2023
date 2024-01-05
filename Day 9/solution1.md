```
Given lines containing sequence of numbers
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45

in each line, try to keep generating new sequence of the difference between the sequence, until the all the difference are 0
0   3   6   9  12  15
  3   3   3   3   3
    0   0   0   0
then predict the next number in the original sequence
0   3   6   9  12  15  18
  3   3   3   3   3   3
    0   0   0   0   0
finally, add all predictions for all lines

The answer will be 114

Steps:
1. Read all lines and generate list of sequence
2. For each sequence:
    2.1 Get the last element add them to prediction
    2.2 Generate new sequence containing the difference of the element
    2.3 Check if the difference is all 0
3. Add all predictions

```
