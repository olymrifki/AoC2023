filename = "./Day 24/data.txt"


class Line:
    def __init__(self, x, y, z, vx, vy, vz) -> None:
        self.x1 = x
        self.y1 = y
        self.z1 = z
        self.x2 = x + vx
        self.y2 = y + vy
        self.z2 = z + vz
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def substract_velocity(self, vx, vy, vz):
        return Line(self.x1, self.y1, self.z1, self.vx - vx, self.vy - vy, self.vz - vz)


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
        lines.append(
            Line(
                position[0],
                position[1],
                position[2],
                velocity[0],
                velocity[1],
                velocity[2],
            )
        )

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


def is_line_intersect(line1: Line, line2: Line):
    x1, x2, y1, y2 = line1.x1, line1.x2, line1.y1, line1.y2
    x3, x4, y3, y4 = line2.x1, line2.x2, line2.y1, line2.y2
    det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if det == 0:
        return False, x1, x2
    x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (det)
    y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (det)
    condition1 = (x - x1) * (x2 - x1) >= 0 and (x - x3) * (x4 - x3) >= 0
    condition2 = (y - y1) * (y2 - y1) >= 0 and (y - y3) * (y4 - y3) >= 0
    res = condition1 and condition2
    # print(x, y)
    # print()
    return (res, x, y)


line1 = lines[1]
line2 = lines[2]
line3 = lines[3]
for _vx in range(1000):
    for _vy in range(1000):
        for s1 in range(2):
            for s2 in range(2):
                vx = _vx * (-1) ** s1
                vy = _vy * (-1) ** s2
                rel_line1 = line1.substract_velocity(vx, vy, 0)
                rel_line2 = line2.substract_velocity(vx, vy, 0)
                rel_line3 = line3.substract_velocity(vx, vy, 0)
                is_intersect1, x1, y1 = is_line_intersect(rel_line1, rel_line2)
                is_intersect2, x2, y2 = is_line_intersect(rel_line2, rel_line3)
                if is_intersect1 and is_intersect2 and x1 == x2 and y1 == y2:
                    t1 = (rel_line1.x1 - x1) / -rel_line1.vx
                    z1 = line1.z1 + t1 * line1.vz

                    t2 = (rel_line2.x1 - x1) / -rel_line2.vx
                    z2 = line2.z1 + t2 * line2.vz
                    z0 = z2 - (z2 - z1) * t2 / (t2 - t1)
                    # for _vz in range(1000):
                    #     for s3 in range(2):
                    #         vz = _vz * (-1) ** s3
                    #         if z1 == z0 + t1 * vz:
                    if sum([x1, y1, z0]) == int(sum([x1, y1, z0])):
                        print(sum([x1, y1, z0]))
                    # if z1 == z2:
                    #     print(x1, y1, z1)
