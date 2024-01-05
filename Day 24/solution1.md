```
Given list of objects' 3d position and velocity, determine wether the object's projection will intersect when only viewed from a square area inside x and y plane. Count all intersection inside this area only if it is going to happen (not happening in the past)

For area from atleast 7 until 27 with input
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3

there are 2 total collisions



Steps
0. Read input
1. Check if intersect (from wikipedia):
    1.1 Each line has point1 at x1, y1 and point 2 at  x1+vx1, at y1+vy1
    1.2 for other line with point 3 and point 4:
        line with intersect if
            det=(x1-x2).(y3-y4)-(y1-y2).(x3-x4)!=0
        If it will intersect, the intersection point is at
            x=((x1y2-y1x2)(x3-x4)-(x1-x2)(x3y4-y3x4))/(det)
            and
            y=((x1y2-y1x2)(y3-y4)-(y1-y2)(x3y4-y3x4))/(det)

    1.3 If this point inside the square and not happening in the past, add counter
    1.4 to check it it is not happening in the past, the sign of x relative to x1 has to be the same as x2 relative to x1
2. Do for all combinations of lines
```
