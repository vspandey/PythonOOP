1. When a class is called like var1=className()
then it calls 2 built in functions - \_\_new_\_ [ it creates object in memory and hold an empty dictionary, and sends it to \_\_init__ function]. Eventlually the \_\_new_\_ creates the object which is refered as 'self' in constructor \__init__

2. All the attributes are stored in the object's internal dictionary. Call objectName.\_\_dict\_\_ to see them

3. Objects ARE NOT dictionaries, but python use internal dictionaries to manage the objects.

4. use \_\_str\_\_(self) method, to return the details about the object. For end users

5. use \_\_repr\_\_(str) method to return details of objects for developers
