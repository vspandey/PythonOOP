class a:
    def __init__(self):
        pass

    def do_print(self):
        print("a")
        
class mixin1:
    def __init__(self):
        pass

    def do_print(self):
        print("mixin1")

class b(mixin1,a):

    def print_hey(self):
        print("hey")

#MRO will tell the order of inheritance, in this case it will be b -> mixin1 -> a


print(b.mro())
b1 = b()
b1.do_print()  

