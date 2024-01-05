```
Given undirectional graph, disconnect three edge so that the graph become two separate graph. Then multiply its size

One solution is from one of the comments here
https://www.reddit.com/r/adventofcode/comments/18qe8qo/2023_day_25_part_1_why_work_hard/
is by counting the highest frequency of edges in a lot of random path (is that what people called monte carlo??)
and also other discussion use networkx (i didnt know before)

This is may be true because this hottest edge, the edge between two big group of nodes, has to be the most walked if we take path from two random nodes.

```
