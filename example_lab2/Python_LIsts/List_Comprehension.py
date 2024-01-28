#List Comprehension
fruits=["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[]

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
print("\n")

#With list comprehesion you can do all that with only one line of code:
fruits=["apple", "banana", "cherry", "kiwi", "mango"]

newlist=[x for x in fruits if "a" in x]

print(newlist)

#The Syntax 
#newlist=[expression for item in iterable if condition == True]

#Condition
newlist=[x for x in fruits if x != "apple"]
print(newlist)
print("\n")

#The condition is optional nad can be omitted:
newlist=[x for x in fruits]
print(newlist)
print("\n")

#Iterable 
newlist=[x for x in range(10)]
print(newlist)
print("\n")

#Same example, but with a condition:
newlist=[x for x in range(10) if x<5]
print(newlist)
print("\n")

#Expression 
newlist=[x.upper() for x in fruits]
print(newlist)
print("\n")

#You can set the outcome to whatever you like:
newlist=['hello' for x in fruits]
print(newlist)
print("\n")
#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
fruits=["apple", "banana", "cherry", "orange", "kiwi", "mango"]
newlist=[x if x !="banana" else "orange" for x in fruits]
print(newlist)
print("\n")
