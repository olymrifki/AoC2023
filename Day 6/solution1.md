```
Given list of time and distance in multiple races

Time:      7  15   30
Distance:  9  40  200
(race 1: time=7, distance=9)
Where time and distance will be integer

In each race, there is preparation stage and race stage.
In preparation time, the longer the preparation, the faster you move in race time
given by formula: 1 time prearation gives 1 speed. (Speed will be constant in race stage)

The time given above is the total time of the race
Meanwhile the distance is the current best distance

For each race, count the total of preparation times that will win (*win_count*)

Find the multiplication of all *win_count*s

Example solution is 288

Steps:
1. Read list of time and list of distance
2. In a race, the number of win_count will be determined by:
    2.1 Determine if a preparation time is a win:
        speed = preparation_time
        Win prep time will met:
            best_distance < (max_time - preparation_time) * speed
    2.2 Then the win_count will be:
        maximum_prep_time to win - minimum_prep_time to win + 1
3. Multiply all win_count

```
