```
In this problem, we need to count how many areas (pipe or empty) inside the loop

FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L

Answer: 10



This will start after the last step in solution 1:
1. Traceback the loop from meeting point and replace all walls by "0"
2. After reaching starting point, loop back again and :
    2.1 Because we dont know if the inside area it at the left or right, we will try to fill each side separately using *four directional flood fill* into and change each of the element with "I". Either
        a. The wrong side will evetually tries to fill outside the matrix border, in this case, move to next fill side
        b. All will be filled correctly, count all "I" in all the image
```
