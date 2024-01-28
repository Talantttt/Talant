#Add Items
thisset={"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
print("\n")

#Add Sets
thisset={"apple","banana", "cherry"}
tropical={"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
print("\n")

#Add Any Iterable 
thisset={"apple", "banana", "cherry"}
mylist=["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
print("\n")
