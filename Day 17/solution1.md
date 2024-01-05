```
Given maps containing numbers, walk through the map from top-left to bottom-right with the least sum of numbers.
Rules: 1. Walking in a straight line cant be more than 3 blocks. After that, you have turn left or right, no reverse.
2. Initial posiion at top left does not count unless you turn there afterward

2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533

The answer will be 102

Steps:
1. Read input
2. This will probably be djikstra problem
   I ended up using a-star algorithm, not sure if it is optimized that much


```
