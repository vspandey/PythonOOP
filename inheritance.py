class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    def increase_salary(self, percentage):
        self.__salary += self.__salary * (percentage / 100)

    def __str__(self):
        return f"{self.name} is a Tester with a salary of {self.salary}"

class Tester(Employee):
    
    def run_tests(self):
        print(f"{self.name} is running tests")

    

class Developer(Employee):


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


t1 = Tester("Rahul", 25, 2000)
d1 = Developer("Mohit", 30, 5000, "flask")

print(t1)
print(d1)

t1.increase_salary(10)
d1.increase_salary(10, 1000)

print(t1)
print(d1) 

    