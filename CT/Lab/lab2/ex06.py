class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

shapes = [
    Circle(3),
    Rectangle(4, 5),
    Circle(5),
    Rectangle(2, 10)
]

total_area = 0
for shape in shapes:
    a = shape.area()
    print(f"Area {shape.__class__.__name__}: {a}")
    total_area += a

print(f"Total area: {total_area}")
