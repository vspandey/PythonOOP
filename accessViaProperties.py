class Employee:

    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):

        raise AttributeError("Cannot set salary directly")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.__age = age

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if position not in ["Software Developer", "Manager", "Data Analyst"]:
            raise ValueError("Position is not valid")
        self.__position = position

    def increase_salary(self, percentage):
        self.__salary += self.__salary * (percentage / 100)

    def __str__(self):
        return f"{self.name} is a {self.position} with a salary of {self.salary}"


e1 = Employee("Mohit", 25, "Software Developer",2000)
print(e1)

e1.increase_salary(10)
print(e1, ":  after a 10% raise")

# print(e1.salary)
# print(e1.age)
# print(e1.position)

e1.__salary = 20000
print(e1.salary)