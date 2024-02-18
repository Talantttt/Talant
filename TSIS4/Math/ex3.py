import math
a=int(input("Input number of sides:"))
b=int(input("Input length of a side:"))
print("The area of the polygon is:", math.floor((a*b**2)/(4*math.tan(math.pi/a))))