```
In this problem, the Os not only going to be moved up, but up, left, down, right, called one cycle.
We need to calculate what the score is for 1_000_000_000 cycles

Answer will be 64


Guess method:
Because the number is too big, this will probably be a repeated position like what happens when you move rubics cube in the same pattern many times.
We migght not be repeating right away, but only after some cycles.
Therefore, we need to do each cycle and  calculate score repeatedly untill the scores are repeating. Then we will take the remainder of the rest of the 1 bilion cycle with the repeated move.


Functions needed:
1. Unlike before, we need to rotate the "board" to the right
2. Also we need to physcally move all the Os to the proper sides


```
