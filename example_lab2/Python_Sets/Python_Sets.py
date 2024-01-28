myset={"apple", "banana", "cherry"}
#Set
thisset={"apple", "banana", "cherry"}
print(thisset)
print("\n")

#Set Items:
#Set items are unordered, unchangeable, and do not allow duplicate values.

#Unordered:
#Unordered means that the items in a set do not have a defined order.

#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

#Unchangeable:
#Set items are unchangeable, meaning that we cannot change the items after the set has been created.

#Duplicates Not Allowed
thisset={"apple", "banana", "cherry", "apple"}
print(thisset)
print("\n")

#True and 1 is considered the same value:
thisset={"apple", "banana", "cherry", True, 1, 2}
print(thisset)
print("\n")

#False and 0 is considered the same value:
thisset={"apple", "banana", "cherry", False, True, 0}
print(thisset)
print("\n")

#Get the Length of a Set
thisset={"apple", "banana", "cherry"}
print(len(thisset))
print("\n")

#Set Items - Data Types
set1={"apple", "banana", "cherry"}
set2={1, 2, 3}
set3={True, False, False}

#A set can contain different data types:
set1={"abc", 34, True, 40, "male"}

#type()
myset={"apple", "banana", "cherry"}
print(type(myset))

#The set() Constructor
thisset=set(("apple", "banana", "cherry")) #note the double round-brackets
print(thisset)
print("\n")
