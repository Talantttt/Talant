#Loop Through a Tuple 
thistuple=("apple", "banana", "cherry")
for x in thistuple:
    print(x)
print("\n")

#Loop Through the Index Numbers 
thistuple=("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])
print("\n")

#Using a While Loop
thistuple=("apple", "banana", "cherry")
i=0
while i<len(thistuple):
    print(thistuple[i])
    i+=1
