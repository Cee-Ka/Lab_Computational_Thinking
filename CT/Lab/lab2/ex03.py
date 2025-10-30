class Student:
    def __init__(self, name, grade=0):
        self.name = name          
        self.__grade = grade      

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            raise ValueError("Grade must in range 0 - 100!")

    def get_grade(self):
        return self.__grade



s1 = Student("An")
s1.set_grade(85)

s2 = Student("Binh")
s2.set_grade(95)

print(f"{s1.name}: {s1.get_grade()}")
print(f"{s2.name}: {s2.get_grade()}")

try:
    s1.set_grade(120)
except ValueError as e:
    print("Error:", e)
