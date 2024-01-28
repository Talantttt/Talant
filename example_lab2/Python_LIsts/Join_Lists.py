#Join Two Lists
list1=["a", "b", "c"]
list2=[1, 2, 3]
list3=list1+list2
print(list3)
print("\n")

#Another way to join two lists is by appending all the items from list2 into list1, one by one:
lsit1=["a", "b", "c"]
list=[1, 2, 3]

for x in list2:
    list1.append(x)
print(list1)
print("\n")

#Or you can use the extend() method, where the purpose is to add elements from one list to another list:
list1=["a", "b", "c"]
list2=[1, 2, 3]

list1.extend(list2)
print(list1)
print("\n")
