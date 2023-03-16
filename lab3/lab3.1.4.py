import math


class Point(object):
    def __init__(self, x, y):
        self.dy = None
        self.dx = None
        self.x = x
        self.y = y

    def show(self):
        return print(self.x, self.y)

    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        self.x = self.x + dx
        self.y = self.y + dy

    def dist(self, other):
        return math.sqrt((other[0] - self.x) ** 2 + (other[1] - self.y) ** 2)