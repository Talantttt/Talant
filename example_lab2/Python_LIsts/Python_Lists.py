#List
thislist=["apple", "banana", "cherry"]
print(thislist)
print("\n")

#Allow Duplicates
thislist=["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print("\n")

#List Length
thislist=["apple", "banana", "cherry"]
print(len(thislist))
print("\n")

#List Items - Data Types
list1=["apple", "banana", "cherry"]
list2=[1,5,7,9,3]
list3=[True, False, False]

#A list can contain different data types :
list1=["abc", 34, True, 40, "male"]

#type()
mylist=["apple", "banana", "cherry"]
print(type(mylist))
print("\n")

#The list() Constructor
thislist=list(("apple", "banana", "cherry")) #note the double round-brackets
print(thislist)
print("\n")

#Python Collections (Arrays)
"""
List        is a collection which is ordered and changeable. Allows duplicate members.
Tuple       is a collection which is ordered and unchangeable. Allows duplicate members.
Set         is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary  is a collection which is ordered** and changeable. No duplicate members."""
