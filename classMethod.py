class Employee:

    __slots__ = ['name', 'age', 'position', '_salary']

    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self._salary = salary
    minimum_age = 18

    @classmethod                    #class method decorator, used to define a class method that is method does not interact with the instance of the class
    def is_adult(cls, age):
        return age >= cls.minimum_age
    
    @staticmethod                   #static method decorator, used to define a static method that does not interact with the instance of the class
    def is_valid_email(email):
        return "@" in email

e1 = Employee("Mohit", 25, "Software Developer", 2000)
print(Employee.is_adult(25))
print(Employee.is_valid_email("moht@@gmail.com"))
