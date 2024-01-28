#Append Items
thislist=["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
print("\n")

#Insert Items
thislist=["apple", "banana", "cherry"]
thislist.insert(1,"orange")
print(thislist)
print("\n")

#Extend List
thislist=["apple", "banana", "cherry"]
tropical=["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
print("\n")

#Add Any Iterable 
thislist=["apple", "banana", "cherry"]
thistuple=("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
print("\n")
