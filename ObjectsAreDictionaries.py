class Employee:

    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.__position = position
        self._salary = salary


    def increase_salary(self, percentage):
        self._salary += self._salary * (percentage / 100)

    def __str__(self):
        return f"{self.name} is a {self.__position} with a salary of {self._salary}"
    

#instantiating objects    
mohit = Employee("Mohit", 25, "Software Developer", 50000)
rahul = Employee("Rahul", 30, "Manager", 80000)

print(mohit)
print(rahul)

mohit.increase_salary(10)
rahul.increase_salary(8)

print("salary raised by 10% for mohit and 8% for rahul")
print(mohit)
print(rahul)


mohit.salary = 60000
print(mohit)