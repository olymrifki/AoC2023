```
Given list of direction, distance, and color

R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)

these directions will create a loop.
Count the loop wall and one extra layer inside the loop

The answer will be 62

Steps
1. Read file and create 2d map of the wall
2. Loop detection wil be similar to Day 10 solution, without the flood fill

```
