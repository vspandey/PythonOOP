
## Why OOPs is needed?
- Better maintainability
- Reusability of code through inheritance
- Encapsulation for better data security
- Easier to manage and debug complex systems

## OOP Principles

1. **Encapsulation**: Encapsulation is the concept of wrapping data and methods that operate on the data within a single unit, typically a class. This helps in protecting the data from outside interference and misuse.

2. **Inheritance**: Inheritance allows a class to inherit properties and behavior from another class. This promotes code reusability and establishes a natural hierarchy between classes.

3. **Polymorphism**: Polymorphism allows methods to do different things based on the object it is acting upon. It enables one interface to be used for a general class of actions, making it easier to manage and extend.

4. **Abstraction**: Abstraction is the process of hiding the complex implementation details and showing only the necessary features of an object. It helps in reducing programming complexity and effort.

## Class and Objects in Memory Management

In Python, a class is a blueprint for creating objects. When an object is created, Python allocates memory for the object and its attributes. Each object has a unique memory address. Python uses a dynamic memory allocation system and garbage collection to manage memory efficiently.

When you pass an object to a function, it is passed by reference, meaning the function receives a reference to the original object, not a copy. This allows the function to modify the object's attributes directly, reflecting changes outside the function scope.

## Variable Naming Conventions in Python

1. **`var`**: This is a regular variable name. It is accessible from anywhere in the code where it is in scope.

2. **`_var`**: A single leading underscore indicates a weak "internal use" indicator. It is a convention to signal that the variable or method is intended for internal use only and should not be accessed directly from outside the class.

3. **`__var`**: A double leading underscore causes name mangling. The interpreter changes the name of the variable in a way that makes it harder to create subclasses that accidentally override the private attributes and methods. This is used to avoid naming conflicts in subclasses.

## `__name__` in Python

The `__name__` variable is a special built-in variable in Python. It is used to determine if a module is being run as the main program or if it is being imported into another module. When a Python file is run directly, `__name__` is set to `"__main__"`. If the file is imported as a module in another script, `__name__` is set to the module's name.

This allows for conditional execution of code, such as running tests or executing a main function only when the script is run directly:

```python
if __name__ == "__main__":
    # Code to execute when the script is run directly
    main()

## Access Level Control in Python

## Access Level Control in Python

In Python, access level control for methods and variables is managed through naming conventions rather than explicit keywords like in Java. Here are the conventions:

1. **Public**: Methods and variables are public by default. They can be accessed from anywhere.
    ```python
    class MyClass:
        def __init__(self):
            self.public_var = "I am public"
        
        def public_method(self):
            return "This is a public method"
    ```

2. **Protected**: A single leading underscore (`_`) indicates that a method or variable is intended for internal use. It is a convention and does not prevent access from outside the class.
    ```python
    class MyClass:
        def __init__(self):
            self._protected_var = "I am protected"
        
        def _protected_method(self):
            return "This is a protected method"
    ```

3. **Private**: A double leading underscore (`__`) triggers name mangling, making it harder to access the method or variable from outside the class. This is used to avoid accidental access and name conflicts in subclasses.
    ```python
    class MyClass:
        def __init__(self):
            self.__private_var = "I am private"
        
        def __private_method(self):
            return "This is a private method"
    ```

These conventions help manage access levels, but they rely on the discipline of the programmer to respect them.

