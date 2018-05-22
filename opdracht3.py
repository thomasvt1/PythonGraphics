from grid import *
import math

g = Grid(20, 20)


def drawline(x1, y1, x2, y2, c=1):
    if y1 == y2:
        length = abs(x1 - x2)
        x = min(x1, x2)
        print(length)
        for i in range(0, length):
            g.addPoint(x + i, y1, c)

    elif x1 == x2:
        length = abs(y1 - y2)
        y = min(y1, y2)
        print(length)
        for i in range(0, length):
            g.addPoint(x1, y + i, c)

    else:
        _x = abs(x1 - x2)
        _y = abs(y1 - y2)
        angle = math.degrees((math.atan(_y / _x)))
        print("! ERROR: No draw method found")
        print(angle)





drawline(5, 0, 0, 0)
drawline(0, 15, 0, 5)
drawline(0, 0, 3, 3)


g.draw()
