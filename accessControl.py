class demo:

    def __init__(self, name, profession, age):
        self._name = name
        self.__profession = profession
        self.age = age

demo1 = demo("demo1", "Software Developer", 25)

print(demo1.__dict__)

print(demo1._name) #non-public attribute
print(demo1._demo__profession) #private attribute, demo is the class name.
print(demo1.age) #public attribute

#name mangling, cannot directly call __profession
print(demo1.__profession) #AttributeError: 'demo' object has no attribute '__profession'

    