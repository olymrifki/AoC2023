```
Given looping pipe connections 

..F7.
.FJ|.
SJ.L7
|F--J
LJ...

Where:

| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position representing a pipe

Find the furthest pipe from the start of the loop represented by steps from the start

Answer: 8
..45.
.236.
01.78
14567
23...

Steps:
1. Read text of input into 2D list
2. From the starting point S follow all four side of adjacent to it until it is connected to an invalid connection or two of them meet at a point. Track the steps in step_count

```