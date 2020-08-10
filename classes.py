# Class: blueprint for creating new objects eg.Human
# Object: instance of a class eg.John,Mary


#object is base class for all classes in python

class Point:
    default_color = "red"

    def __init__(self, x, y):  # self is reference to current object | Named self by convention
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x , self.y + other.y)

    def __gt__(self, other):  # pyhton will automatically figure out less than magic method once greater than is defined
        return self.x > other.x and self.y > other.y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(10, 20)
other = Point(1, 2)
print(point + other)
print(point == other)
print(point > other)
print(point < other)
print(point)

print(point.default_color)
print(Point.default_color)

p = Point.zero()
p.draw()

Point.default_color = "Yellow"
point.z = 10
print(type(point))
print(point.x)
print(isinstance(point, Point))
point.draw()

another = Point(3, 4)
print(another.default_color)
another.draw()
