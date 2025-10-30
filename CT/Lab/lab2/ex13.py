class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee(name={self.name}, salary={self.salary})"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def __str__(self):
        return f"Manager(name={self.name}, salary={self.salary}, department={self.department})"

class Executive(Manager):
    def __init__(self, name, salary, department, stock_options):
        super().__init__(name, salary, department)
        self.stock_options = stock_options

    def __str__(self):
        return (f"Executive(name={self.name}, salary={self.salary}, "
                f"department={self.department}, stock_options={self.stock_options})")

e = Employee("An", 50000)
m = Manager("Binh", 70000, "HR")
x = Executive("Cuong", 150000, "Engineering", 10000)

print(e)
print(m)
print(x)