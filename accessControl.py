## Access Level Control in Python

""" In Python, access level control for methods and variables is managed through naming conventions rather than explicit keywords like in Java. Here are the conventions:
"""

""" **Public**: Methods and variables are public by default. They can be accessed from anywhere.
    ```python
    """
class MyClass:
        def __init__(self):
            self.public_var = "I am public"
        
        def public_method(self):
            return "This is a public method"

"""**Protected**: A single leading underscore (`_`) indicates that a method or variable is intended for internal use. It is a convention and does not prevent access from outside the class.
"""
class MyClass:
        def __init__(self):
            self._protected_var = "I am protected"
        
        def _protected_method(self):
            return "This is a protected method"


""" **Private**: A double leading underscore (`__`) triggers name mangling, making it harder to access the method or variable from outside the class. This is used to avoid accidental access and name conflicts in subclasses.
"""
class MyClass:
        def __init__(self):
            self.__private_var = "I am private"
        
        def __private_method(self):
            return "This is a private method"

