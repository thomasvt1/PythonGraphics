from grid import *
import math

g = Grid(50, 50)


def rasterline(x1, y1, x2, y2, c=1):
    min_x = min(x1, x2)
    min_y = min(y1, y2)

    # First run two small if statements which are smaller and more efficient.

    if y1 == y2:
        length = abs(x1 - x2)
        print(length)
        g.addPoint(min_x, y1, c)
        for i in range(0, length):
            g.addPoint(min_x + i, y1, c)

    elif x1 == x2:
        length = abs(y1 - y2)
        print(length)
        for i in range(0, length):
            g.addPoint(x1, min_y + i, c)

    else:  # If no easy method is found run the advanced method.
        print("Running else function")
        angle_tot = 0
        x = x1  # Pick x1 - start value
        y = y1  # Pick y1 - start value

        y_temp = abs(y1 - y2)
        x_temp = abs(x2 - x1)

        angle = math.degrees(math.atan2(y_temp, x_temp))  # Calculates the angle of the line for y value

        angle_x = 90 - angle  # Angle of line for calculations for the x value
        angle_x_tot = 0

        has_gone = False
        has_gone_x = False

        if x_temp > y_temp:  # Checks if x or y is bigger to determine the line length
            line_length = x_temp
        else:
            line_length = y_temp

        for i in range(0, line_length):
            g.addPoint(x, y, c)

            if angle <= 45:  # Checks if the degree is more or less than 45
                x += 1
            else:
                angle_x_tot += angle_x  # Adds to total to see how far the line is in correlation to the gridsquares
                if angle_x_tot > 22.5 and has_gone_x is False:
                    x += 1
                    has_gone_x = True
                if angle_x_tot >= 45:
                    angle_x_tot -= 45
                    has_gone_x = False

            angle_tot += angle

            if angle_tot > 22.5 and has_gone is False:
                if y1 > y2:
                    y -= 1
                else:
                    y += 1
                has_gone = True

            if angle_tot >= 45:
                angle_tot -= 45
                has_gone = False


#for i in range(0, 25):
#    drawline(i, 25, 5, i % 5)

rasterline(0,0,0,0)
#drawline(5, 0, 0, 0)
#drawline(0, 15, 0, 5)
#drawline(1, 1, 6, 6)
#drawline(10, 10, 6, 6)
#drawline(3, 3, 0, 0)
#drawline(10, 5, 0, 0)

#drawline(0, 10, 10, 0)

#drawline(10, 10, 0, 0)

#drawline(10, 5, 0, 0)
#drawline(0, 0, 10, 5)
#drawline(0, 0, 5, 10, 0.5)

g.draw()
