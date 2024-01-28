#Tuple
thistuple=("apple", "banana", "cherry")
print(thistuple)
print("\n")

#Allow Duplicates
thistuple=("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print("\n")

#Tuple Length
thistuple=("apple", "banana", "cherry")
print(len(thistuple))
print("\n")

#Create Tuple With One Item
thistuple=("apple",)
print(type(thistuple))

#NOT a tuple
thistuple=("apple")
print(type(thistuple))
print("\n")

#Tuple Items - Data Types
tuple1=("apple", "banana", "cherry")
tuple2=(1, 5, 7, 9, 3)
tuple3=(True, False, False)
print("\n")

#A tuple can contain different types:
tuple1=("abc", 34, True, 40, "male")

#type()
mytuple=("apple", "banana", "cherry")
print(type(mytuple))

#The tuple() Constructor
thistuple=tuple(("apple", "banana", "cherry")) #note the double round-brackets
print(thistuple)