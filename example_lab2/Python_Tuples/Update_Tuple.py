#Change Tuple Values 
x=("apple", "banana", "cherry")
y=list(x)
y[1]="kiwi"
x=tuple(y)

print(x)
print("\n")

#Add Items: Convert into a list
thistuple=("apple", "banana", "cherry")
y=list(thistuple)
y.append("orange")
thistuple=tuple(y)
print(thistuple)
print("\n")

#Add Items: Add tuple to a tuple
thistuple=("apple", "banana", "cherry")
y=("orange",)
thistuple+=y
print(thistuple)
print("\n")

#Remove Items 
thistuple=("apple", "banana", "cherry")
y=list(thistuple)
y.remove("apple")
thistuple=tuple(y)
print(thistuple)
print("\n")

#del
thistuple=("apple", "banana", "cherry")
del thistuple 
print(thistuple) #this will raise an error because the tuple no longer exists
