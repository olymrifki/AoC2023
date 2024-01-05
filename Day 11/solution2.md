```
In this problem, instead of empty rows and columns contains become twice as large, it become 1 million times as much

To do this, we mark all empty rows and columns into *
Then to calculate distance, walk from one # to the other # one step at a time, detecting any * on the way. To get minimum value of the distance, we'll use djikstra's algorithm

Steps:
1. Replace all empty rows and columns to *
2. Calculate minimum distance and add them

Optimization:
My implementation of djikstra's algorithm didnot work.
To get minimum distance more efficiently, we walk toward destination from source. In each step, next step will be the shortest distance between if we are moving closer in x direction or y direction only
But the answer from the data are still being generated in a long time
```
