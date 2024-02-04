#Python Lambda
"""A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
"""
#Syntax
#lambda arguments: expression

x=lambda a:a+10
print(x(5))
print("\n")

#Lambda can take any number of arguments:
x=lambda a,b :a*b
print(x(5,6))
print("\n")

x=lambda a, b, c: a+b+c
print(x(5, 6, 2))
print("\n")

#Why Use Lambda Functions?
"""The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, and that argument will be multipled with an unkown number:"""
def my_func(n):
    return lambda a: a*n

#Use that function definition to make a function that always doubles the number you send in:
def myfunc(n):
    return lambda a: a*n 
mydoubler=myfunc(2)
print(mydoubler(11))
print("\n")

#Or, use the same function definition to make a function that always triples the number you send in:
def my_func(n):
    return lambda a: a*n
mytripler=my_func(3)
print(mytripler(11))
print("\n")

#Or,use the same function definition to make both functions, in the same program:
def my_func(n):
    return lambda a: a*n
mydoubler=my_func(2)
mytripler=my_func(3)
print(mydoubler(11))
print(mytripler(11))