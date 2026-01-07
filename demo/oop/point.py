class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"X = {self.x}, Y = {self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return  self.x * self.y > other.x * other.y

p1 = Point(10, 20)
p2 = Point(10, 20)
p3 = Point(10, 10)

lst = [p1, p2, p3]
for p in sorted(lst):
    print(p)

print(p1)  # str(p1) ->  p1.__str__()
print(p1 == p2)  # p1.__eq__(p2)
print(p1 == p3)

print(p1 > p3)  # p1.__gt__(p3)
print(p1 < p2)  # p1.__gt__(p2)