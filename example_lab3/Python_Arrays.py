#Python Arrays
cars=["Ford", "Volvo", "BMW"]

#Access the Elements of an Array
#You refer to an array element by referring to the index number:
x=cars[0]

#Modify the value of the first array item:
cars[0]="Toyota"

#The Length of Array
#Use the len() method to return the length of an array (the number pf elements in an array).
x=len(cars)
print(x)
print("\n")

#Looping Array Elements
for x in cars:
    print(x)
print("\n")

#Adding Array Elements
cars.append("Honda")
for x in cars:
    print(x)
print("\n")

#Removing Array Elements
cars.pop(1)
for x in cars:
    print(x)
print("\n")

#You can also the remove()  method to remove an element from the array:
cars.remove("BMW")
for x in cars:
    print(x)

#Array Methods
"""
Method	        Description
append()	    Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()        Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the first item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list
"""