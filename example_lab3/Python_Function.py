#Python Functions
"""A function is a block of code which only runs when it is callled.
You can pass data, known as parameters, into a function.
A function can return data as a result"""
#Creating Function
def my_function():
    print("Hello from a function")
print("\n") 

#Calling a Function
def my_function():
    print("Hello from a function")
my_function()
print("\n")

#Arguments
def my_function(fname):
    print(fname+" Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
print("\n")

#Number of Arguments
def my_function(fname, lname):
    print(fname+" "+ lname)
my_function("Emil", "Refsnes")
print("\n")

#If you try to call the function with 1 or 3 arguments, you will get an error:
"""def my_function(fname, lname):
    print(fname+" "+lname)
my_function("Emil")"""

#Arbitrary Arguments, *args
def my_function(*kids):
    print("The youngest child is "+ kids[2])
my_function("Emil", "Tobias", "Linus")
print("\n")

#Keyword Arguments 
def my_function(child3, child2, child1):
    print("The youngest child is "+child3)
my_function(child1="Emil", child2="Tobias", child3="Linus")
print("\n")

#Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
    print("His last name is "+ kid["lname"])
my_function(fname="Tobias", lname="Refsnes")
print("\n")

#Defualt Parameter Value
def my_function(country="Norway"):
    print("I am from "+country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
print("\n")

#Passing a List as an Argument
def my_function(food):
    for x in food:
        print(x)
fruits=["apple", "banana", "cherry"]
my_function(fruits)
print("\n")

#Return Values
def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(5))
print(my_function(9))
print("\n")

#The pass Statement
def myfunction():
    pass
print("\n")

#Positional-Only Arguments
def my_function(x,/):
    print(x)
my_function(3)
print("\n")

#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
def my_function(x):
    print(x)
my_function(x=3)
print("\n")

#But when adding the , / you will get an error if you try to send a keyword argument:
"""def my_function(x,/):
    print(x)
my_function(x=3) #error
print("\n")"""

#Keyword-Only Arguments
def my_function(*,x):
    print(x)
my_function(x=3)
print("\n")

#Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:
"""def my_function(x):
    print(x)
myfunction(3) #error
"""

#But when adding the *, / you will get an error if you try to send a positional argument:
"""def my_function(*, x):
  print(x)

my_function(3) #error
"""

#Combine Positional-Only and Keyword -Only
def my_function(a,b, /, *, c,d):
    print(a+b+c+d)
my_function(5, 6, c=7, d=8)
print("\n")

#Recursion
"""Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it."""
def tri_recursion(k):
    if(k>0):
        result=k+tri_recursion(k-1)
        print(result)
    else:
        result=0
    return result
print("\n\nRecursion Example Results")
tri_recursion(6)