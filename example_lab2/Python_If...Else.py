#Python Conditions and If statements
"""
Equals:                    a == b
Not Equals:                a != b
Less than:                 a < b
Less than or equal to:     a <= b
Greater than:              a > b
Greater than or equal to:  a >= b"""

#If statement 
a=33
b=200
if b>a:
    print("b is greater than a")

#Indentation
"""a=33
b=200
if b>a:
print("b is greater than a")"""
print("\n")

#Elif
a=33
b=33
if b>a:
    print("b is greater than a")
elif b==a:
    print("a and b are equal")
print("\n")

#Else
a=200
b=33
if b>a:
    print("b is greater than a")
elif b==a:
    print("a and b are equal")
else:
    print("a is greater than b")
print("\n")

a=200
b==3
if b>a:
    print("b is greater than a")
else:
    print("a is greater than b")
print("\n")

#Short Hand If
if a>b:print("a is greater than b")
print("\n")

#Short Hand If..Else
a=2
b=330
print("A") if a>b else print("B")
print("\n")

a=330
b=330
print("A") if a>b else print("=") if a==b else print("B ") 

#And
a=200
b=33
c=500
if a>b and c>a:
    print("Both conditions are True")
print("\n")

#Or
a=200
b=33
c=500
if a>b or c>a:
    print("At least one of the condiotions is True")

#Not
a=33
b=200
if not a>b:
    print("a is NOT greather than  b")
print("\n")

#Nested If
x=41
if x>10:
    print("Above ten,")
    if x>20:
        print("and also above 20!")
    else:
        print("but not above 20.")
print("\n")

#The pass Statement
a=33
b=200
if b>a:
    pass
