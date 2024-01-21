Python - Global Variables
27)x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
28)x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
29)def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
30)x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
Python Data Types
31)x = 5
print(type(x))
