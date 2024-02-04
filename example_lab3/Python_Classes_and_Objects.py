#Python Classes and Objects
"""Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects."""

#Create a Class: Create a class named MyClass, with a property named x:
class MyClass:
    x=5
print("\n")

#Create Object: Now we can use the class named MyClass to create objects:
p1=MyClass()
print(p1.x)
print("\n")

#The __init__() Function
"""
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
"""
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
p1=Person("John", 36)
print(p1.name)
print(p1.age)
print("\n")

#The __str()__ Function
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
p1=Person("John", 36)
print(p1)
print("\n")

class Person:
    def __init__(self, name, age):
        self.name=name 
        self.age=age
    def __str__(self):
        return f"{self.name}({self.age})"
p1=Person("John", 36)
print(p1)
print("\n")

#Object Methods
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is "+self.name)
p1=Person("John", 36)
p1.myfunc()
print("\n")

#The self Parameter
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name=name
        mysillyobject.age=age
    
    def myfunc(abc):
        print("Hello my name is "+abc.name)
    
p1=Person("John", 36)
p1.myfunc()
print("\n")

#Modify Object Properties
p1.age=40

#Delete Object Properties
del p1.age

#The pass Statement
class Person:
    pass