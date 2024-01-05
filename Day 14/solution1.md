```
Given formation of . (empty space), # (immovable), and O (movable) objects
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....

try to move all the Os up until it hit the edge, #, or other O. then calculate the score if the bottom most O is one point, second bottom most row is two points, and so on

Answer: 136


Steps:
Here, we'll rotate the formation 90 degrees so that we can calculate score using a single string
1. Read input and save each column into a string
2.In a single string, walk from left to right:
    add # at first element and last element
    find index of all #s
    between these index, count all Os
        set O counter to 0
        for each O:
            add O counter
            add score to ((total length-2) - (#'s start index  + O conuter))
                the magic number 2 is there to get true length at the first O position
3. Add score for all string
```
