```
NOTE: This solution can answer the data correctly, but still missing cases because it cant answer code 1 data. It just somehow works

In this problem, the direction and distance is translated from hex color before.

Because the size of the maps in solution 1 will be very large, we cant represent it again to a list of string.

We will find the area covered by rectangle when we move left then up or down and right then up or down
And add or subtract them ultil instruction finished
```
