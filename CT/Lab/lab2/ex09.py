class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay 
        self.bonus = bonus
class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
    def total_compensation(self):
        return self.salary.pay + self.salary.bonus
sal1 = Salary(5000, 1200)
emp1 = Employee("An", sal1)

sal2 = Salary(7000, 1500)
emp2 = Employee("Binh", sal2)

print(f"{emp1.name} - Total: {emp1.total_compensation()}")
print(f"{emp2.name} - Total: {emp2.total_compensation()}")