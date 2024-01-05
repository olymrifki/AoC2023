filename = "./Day 24/data.txt"


class Line:
    def __init__(self, x, y, vx, vy) -> None:
        self.x1 = x
        self.y1 = y
        self.x2 = x + vx
        self.y2 = y + vy


# Steps
# 0. Read input

min_val, max_val = 0, 0
lines = []
with open(filename) as file:
    alllines = [line.strip() for line in file.readlines()]
    min_val, max_val = (int(a) for a in alllines[0].split(" "))

    for line in alllines[1:]:
        position, velocity = line.split(" @ ")
        position = [int(p) for p in position.split(", ")]
        velocity = [int(p) for p in velocity.split(", ")]
        lines.append(Line(position[0], position[1], velocity[0], velocity[1]))

# 1. Check if intersect (from wikipedia):
#     1.1 Each line has point1 at x1, y1 and point 2 at  x1+vx1, at y1+vy1
#     1.2 for other line with point 3 and point 4:
#         line with intersect if
#             det=(x1-x2).(y3-y4)-(y1-y2).(x3-x4)!=0
#         If it will intersect, the intersection point is at
#             x=((x1y2-y1x2)(x3-x4)-(x1-x2)(x3y4-y3x4))/(det)
#             and
#             y=((x1y2-y1x2)(y3-y4)-(y1-y2)(x3y4-y3x4))/(det)
#     1.3 If this point inside the square and not happening in the past, add counter
#     1.4 to check it it is not happening in the past, the sign of x relative to x1 has to be the same as x2 relative to x1


def is_line_intersect_within_square(
    line1: Line, line2: Line, min_val: int, max_val: int
) -> bool:
    x1, x2, y1, y2 = line1.x1, line1.x2, line1.y1, line1.y2
    x3, x4, y3, y4 = line2.x1, line2.x2, line2.y1, line2.y2
    det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if det == 0:
        return False
    x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (det)
    y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (det)
    condition1 = (
        min_val <= x
        and x <= max_val
        and (x - x1) * (x2 - x1) >= 0
        and (x - x3) * (x4 - x3) >= 0
    )
    condition2 = (
        min_val <= y
        and y <= max_val
        and (y - y1) * (y2 - y1) >= 0
        and (y - y3) * (y4 - y3) >= 0
    )
    # print(x, y)
    return condition1 and condition2


# 2. Do for all combinations of lines
t = 0
result = 0
for i, line1 in enumerate(lines):
    for line2 in lines[i + 1 :]:
        t += 1
        result += int(is_line_intersect_within_square(line1, line2, min_val, max_val))
# print(min_val, max_val)
# print(t)
print(result)
