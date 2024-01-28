#Access Items 
thislist=["apple", "banana", "cherry"]
print(thislist)
print("\n")

#Negative Indexing
thislist=["apple", "banana", "cherry"]
print(thislist[-1])
print("\n")

#Range of Indexes
thislist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print("\n")
#Note: The search will start at index 2 (included) and end at index 5 (not included).

#By leaving out the start value, the range will start at the first item:
thislist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
print("\n")

#By leaving out the end value, the range will go on to the end of the list:
thislist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
print("\n")

#Range of Negative Indexes
thislist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
print("\n")

#Check if Item Exists
thislist=["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruit list")
