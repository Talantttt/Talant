#Access Tuple Items 
thistuple=("apple", "banana", "cherry")
print(thistuple[1])
print("\n")

#Negative Indexing
thistuple=("apple", "banana", "cherry")
print(thistuple[-1])
print("\n")

#Range of Indexes
thistuple=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print("\n")

#By leaving out the start value, the range will start at the first item:
thistuple=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
print("\n")

#By leaving out the end value, the range will go on the end of the tuple:
thistuple=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
print("\n")

#Range of Negative Indexes
thistuple=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
print("\n")

#Check if Item Exists
thistuple=("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
