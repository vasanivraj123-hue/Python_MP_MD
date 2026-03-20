class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(10, 20)
p2 = Point(5, 5)

p3 = p1 + p2
p4 = p1 - p2

print(f"Addition: {p1} + {p2} = {p3}")
print(f"Subtraction: {p1} - {p2} = {p4}")
