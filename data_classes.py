from collections import namedtuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):    # magic method
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
print(id(p1))
print(id(p2))

# Better to use named tuples

Points = namedtuple("Points", ["x", "y"])

p1 = Points(x=1, y=2)
p2 = Points(x=1, y=2)
print(p1 == p2)
