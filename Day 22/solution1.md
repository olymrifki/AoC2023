```
In this problem, given sets of 3d coordinates. In each set, there is start and stop position of a brick. The brick will all fall down and stack to each other without rotating, they will glued right away. The ground is at coordinate Z=0. After every brick fell, we need to count each brick that can be removed because it is not the only support for other brick or it does not support any brick at all. Count all bricks that can be removed

1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9

the answer here is 5


Steps:
1. Read inputs
2. Sort input from least to highest z coordinate
3. Put least z to ground, and so on
    3.1 During this process, find the nearest laid object and put it above this object.
    3.2 We will use one numpy array of booleans for laid object position and one numpy array to store the objects identity.
        3.2.1 We need to detect maximum and minimumm value of each axis.
        3.2.2 For all x and y coordinates for this brick, search the nearest laid object. After nearest laid objects are found by its boolean value, get all of the objects in the other array, add them to this object's support. And fill the boolean array and the object array to this object.
4. After all sorted list of bricks are laid, in all object, if the object does not support exactly one brick, add 1 it to result
```
