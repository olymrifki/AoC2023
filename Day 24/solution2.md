```
In this problem, find sum of initial position (at t=0) of a line that will intersect all of the given lines

19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3

A line starting at 24, 13, 10 with velocity -3, 1, 2
will intersect all lines separately
Therefore, the answer is 47

Assumption: because the result is integer and all inputs are integers, the intersection time is probably integer for all lines

I followed the discussion here
https://www.reddit.com/r/adventofcode/comments/18pptor/2023_day_24_part_2java_is_there_a_trick_for_this/
this is a bruteforce approach where you set velocity of the line and change input line's velocity relative to this line. Then, the intersection will always occure at the initial position.
They suggest that it can be simplified by just using previous code. It can, but still not sure how it ends up getting the z coordinate. We can extrapolate it, but still there are multiple collision that can occur for just three lines by just looking at x and y coordinate

so i assume that all coordinates for the answer has to be integers >:]

```
