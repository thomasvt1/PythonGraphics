import math
from lines import *


class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = float(x), float(y), float(z)

    def rotateY(self, angle):
        """ Rotates the point around the Y axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        z = self.z * cosa - self.x * sina
        x = self.z * sina + self.x * cosa
        return Point(x, self.y, z)

    def transform(self, win_width, win_height, fov, viewer_distance):
        """ Transforms this 3D point to 2D using a perspective projection. """
        factor = fov / (viewer_distance + self.z)
        x = self.x * factor + win_width / 2
        y = -self.y * factor + win_height / 2
        return Point(x, y, 1)


class Simulation:
    def __init__(self, win_width=640, win_height=480):
        self.points = [
            Point(-1, -1, -1),
            Point(1, -1, -1),
            Point(1, 1, -1),
            Point(-1, 1, -1),
            Point(-1, -1, 1),
            Point(1, -1, 1),
            Point(1, 1, 1),
            Point(-1, 1, 1)
        ]

        self.win_width = win_width
        self.win_height = win_height

        # Define the points that compose each of the 6 faces. These numbers are
        # indices to the vertices list defined above.
        self.faces = [(0, 1, 2, 3), (1, 5, 6, 2), (5, 4, 7, 6), (4, 0, 3, 7), (0, 4, 5, 1), (3, 2, 6, 7)]

    def run(self, y=30):
        # Create lines class
        l = Lines(self.win_width, self.win_height)
        # Will hold transformed vertices.
        t = []

        for v in self.points:
            # Rotate the point around Y axis.
            r = v.rotateY(y)

            # Transform the point from 3D to 2D
            p = r.transform(self.win_width, self.win_height, 256, 4)

            # Put the point in the list of transformed vertices
            t.append(p)

        for f in self.faces:
            l.addLine((t[f[0]].x, t[f[0]].y), (t[f[1]].x, t[f[1]].y))
            l.addLine((t[f[1]].x, t[f[1]].y), (t[f[2]].x, t[f[2]].y))
            l.addLine((t[f[2]].x, t[f[2]].y), (t[f[3]].x, t[f[3]].y))
            l.addLine((t[f[3]].x, t[f[3]].y), (t[f[0]].x, t[f[0]].y))

        l.draw()


Simulation().run(30)