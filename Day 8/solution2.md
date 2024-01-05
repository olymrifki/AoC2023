```
This problem is similar to part one except we will start from multiple node that ends with letter A and follow the all the nodes together until it all ends with node that ends with Z.
That means the while loop condition should be changed

The solution used here will follow each step separately to count the total path
Then find least common multiple for all the node steps



LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)

the answer for this example will be 6
```
