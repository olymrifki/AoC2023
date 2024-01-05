```
Given islands of . and # find horizontal or vertical reflection line
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#


Reflection lines
#.##.|.##.
..#.#|#.#.
##...|...#
##...|...#
..#.#|#.#.
..##.|.##.
#.#.#|#.#.

#...##..#
#....#..#
..##..###
#####.##.
---------
#####.##.
..##..###
#....#..#

then the score for an island is the number of column at the left of vertical line
or 100 times of the number of rows above horizontal line
Add score for all island

Answer: 405

Steps:
1. Read lines into islands
    We will develop way to find only horizontal line. Island object will also have rotated version
2. To detect horizontal line:
    2.1 Searching from the first row:
        if two consecutive row are identical:
            Save the bottom row index
            Start comparing all rows aboe and below it
            If we rows keep matching until out of rows:
                return saved row index
            But if there is a mismatch
                keep searching
        if no match at all:
            return 0
3. Each island object will have to multiply the score by 100 or not
    Then sum all the score

```
