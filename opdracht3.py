from grid import *
import math

g = Grid(25, 25)


def drawline(x1, y1, x2, y2, c=1):
    min_x = min(x1, x2)
    min_y = min(y1, y2)

    if y1 == y2:
        length = abs(x1 - x2)
        print(length)
        for i in range(0, length):
            g.addPoint(min_x + i, y1, c)

    elif x1 == x2:
        length = abs(y1 - y2)
        print(length)
        for i in range(0, length):
            g.addPoint(x1, min_y + i, c)

    else:
        _x = abs(x1 - x2)
        _y = abs(y1 - y2)
        _angle = math.degrees((math.atan(_y / _x)))
        print("! WARNING: No draw method found")
        print(_angle)
        print(_x)

        if _angle == 45:
            for i in range(0, _x):
                g.addPoint(min_x + i, min_y + i, c)

        else:
            has_gone = False
            anglex = 90 - _angle
            has_gonex = False

            angle_tot = 0
            anglex_tot = 0

            line_length = _x

            angle = _angle / 45
            anglex /= 45

            print("angle: ", angle)
            for i in range(0, line_length):
                g.addPoint(x1, y1, c)
                if angle <= 1:
                    x1 += 1
                else:
                    anglex_tot += anglex
                    if anglex_tot > 0.5 and has_gonex == False:
                        x1 += 1
                        has_gonex = True
                    if anglex_tot >= 1:
                        anglex_tot -= 1
                        has_gonex = False
                angle_tot += angle
                if angle_tot > 0.5 and has_gone is False:
                    y1 += 1
                    has_gone = True
                if angle_tot >= 1:
                    angle_tot -= 1
                    has_gone = False
                print("AnglexTot: ", anglex_tot, "hasGonex: ", has_gonex)




#drawline(5, 0, 0, 0)
#drawline(0, 15, 0, 5)
#drawline(1, 1, 6, 6)
#drawline(10, 10, 6, 6)
#drawline(3, 3, 0, 0)
drawline(0, 0, 10, 5)

g.draw()
