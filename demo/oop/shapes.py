import math
from abc import ABC, abstractmethod

#Abstract class
class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def circumference(self):
        pass

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def area(self):
        return math.pi * self.r * self.r

    def circumference(self):
        return 2 * math.pi * self.r


class Rectangle(Shape):
    def __init__(self, x, y, l, w):
        super().__init__(x, y)
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

    def circumference(self):
        return 2 * (self.l + self.w)

c = Circle(10,20, 15)
print(c.area())

#s = Shape(10, 20)
