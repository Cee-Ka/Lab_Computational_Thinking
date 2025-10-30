class Circle:
    def __init__(self, radius):
        self._radius = radius  

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("radius must >= 0")
        self._radius = value

    def area(self):
        return 3.14 * (self._radius ** 2)

try:
    c = Circle(5)
    print("radius:", c.radius)
    print("area:", c.area())

    c.radius = 10
    print("new radius:", c.radius)
    print("new area:", c.area())

    c.radius = -3  
except ValueError as e:
    print("error:", e)
