```
Given maps that has "." as empty, "#" as walls, and "S" as starting points

...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........

Starting from S, walk four directional only to sides adjacent to it, except if it is walls. This is first step.
Second step start from the first possible steps to its adjacent four sides, including reverse. Count the number of possible position in n steps

In this example, after 6 steps, there is 16 possible values

Steps
Lets use numpy >:)
Get wall configguration to be a mask
Mark starting position as array of 0 except 1 at S
To walk:
    get four copies of current position, shift them up, down, left, and right.
    Combine all copies with or operation and mask it with wall. This will be the next position

Finally, count all available positions

```
