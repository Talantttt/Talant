#Sort List Alphanumerically
thislist=["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
print("\n")

thislist=[100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
print("\n")

#Sort Descending 
thislist=["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
print("\n")

thislist=[100, 50, 62, 83, 23]
thislist.sort(reverse = True)
print(thislist)
print("\n")

#Customize Sort Function 
def myfunc(n):
    return abs(n-50)
thislist=[100,50,65,82,23] 
thislist.sort(key=myfunc)
print(thislist)
print("\n")

#Case Insetive Sort
thislist=["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
print("\n")

#str.lower
thislist=["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)
print("\n")

#Reverse Order
thislist=["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
