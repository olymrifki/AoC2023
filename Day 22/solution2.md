```
In this problem, calculate the sum of total briicks that will fall when non removable bricks are removed.
We can continue this from the first problem.
For each non removable brick, get all bricks that is being supported by this brick, then also get bricks that is being supported by those bricks.
One edge case is that a brick can be supported by two bricks, like an arch, in that case, mark the brick untill its other support is also removed by the initial non removable brick.
```
