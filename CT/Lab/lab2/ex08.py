class vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        if isinstance(other, vector2D):
            return vector2D(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("add must be in the same type")
    def __str__(self):
        return f"({self.x}, {self.y})"
v1 = vector2D(2, 3)
v2 = vector2D(4, 1)

v3 = v1 + v2    
print(v3)
