```
Given map of a maze, determine the longest possible path from entrance to exit.
Rule:
0. # is wall and . is empty space
1. No tile walked twice
2. There is a one directional indicator >, v, <, and ^.

#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#

the answer here is 94 steps

Steps
1. Read input
2. We need to be able to mark turnable points. This will be our node
    2.1 A turnable point is a point where it is empty, there is atleast one empty space at its left or right and atleast one spacce at its up or down sides.
    2.2 Mark every point with this property
3. Longest path maybe can be found using djikstra modification


```
