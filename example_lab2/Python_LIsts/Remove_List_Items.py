#Remove Specified Item
thislist=["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
print("\n")

#If there are more than one item with the specified value, the remove() method removes the first occurance:
thislist=["apple", "banana", "cherry'", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
print("\n")

#Remove Specified Index
thislist=["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
print("\n")

#If you do not specify index, the pop() method removes the last item
thislist=["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
print("\n")

#del: The del keyword also removes the specified index:
thislist=["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
print("\n")

#The del keyword can also delete the list completely
thislist=["apple", "banana", "cherry"]
del thislist
print("\n")

#Clear the List

#clear
thislist=["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
print("\n")
