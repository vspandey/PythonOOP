""" SLots is a feature of Python that allows you to predefine the attributes of a class. And it makes python faster and 
consumes less memory. its added to the class definition by defining a variable __slots__ and assigning it to a list of. example"""

class Employee:
    __slots__ = ['name', 'age', 'salary']

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)

    def __str__(self):
        return f"{self.name} is a Tester with a salary of {self.salary}"

class Developer(Employee):
    __slots__ = ['framework']

    def __init__(self, name, age, salary, framework = None):
        super().__init__(name, age, salary)
        self.framework = framework

    def write_code(self):
        print(f"{self.name} is writing code")

    def increase_salary(self, percentage, bonus = 0):
        super().increase_salary(percentage)
        self.salary += bonus

    def __str__(self):
        return super().__str__() + f" and works with {self.framework} framework"