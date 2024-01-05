```
Given text of . and #
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
For each rows and columns that dont have any # on them, add one more rows or column next to it once.
Then count four directional distance between two # for all two pairs of # and add them

Answer: 374

Steps:
1. Read all lines into list of string.
    1.1 If any rows and columns that contains no #, duplicate it
    1.2 For each # in any line: save it to an object containing its position. And save all to list
2. Set sum to 0. For all # object in list:
    for all # object after the first:
        calculate difference in position and add it to sum
```
