#Python Inheritance
"""Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

"""

#Create a Parent Class
class Person:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    
    def printname(self):
        print(self.firstname, self.lastname)
#Use the Person class to create an object, and them execute the printname method:
x=Person("John", "Doe")
x.printname()
print("\n")

#Create a Child class
class Student(Person):
    pass

#Now the Student class has the same properties and methods as the Person class.
x=Student("Mike", "Olsen")
x.printname()
print("\n")

#Add the __init__() Function
"""class Student(Person):
    def __init__(self, fname, lname):
        #add properties etc."""

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
print("\n")

#Use the seuper() Function
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

#Add Properties
class Student(Person):
    def __init(self, lname, fname):
        super().__init__(self, fname, lname)
        self.graduationyear=2019

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear=year

x=Student("Mike", "Olsen", 2019)

#Add Methods
class Student(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.graduationyear=year
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)