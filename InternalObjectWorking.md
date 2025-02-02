1. When a class is called like var1=classNAme()
then it calls 2 built in functions - \__new__ [ it creates object in memory and hold an empty dictionary, and sends it to __init__ function]. Eventlually the \__new__ creates the object which is refered as 'self' in constructor \__init__

2. All the attributes are stored in the object's internal dictionary. Call objectName.\__dict__ to see them

3. Objects ARE NOT dictionaries, but python use internal dictionaries to manage the objects.

4. use \__str__(self) method, to return the details about the object. For end users

5. use \__repr__(str) method to return details of objects for developers
