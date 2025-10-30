class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return (f"{self.name} is {self.age}")
p1 = Person("Nam", 20)
p2 = Person("An", 23)
print(p1)
print(p2)