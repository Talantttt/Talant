#Join Two Sets: union()
set1={"a", "b", "c"}
set2={1, 2, 3}
set3=set1.union(set2)
print(set3)
print("\n")

#update()
set1={"a", "b", "c"}
set2={1, 2, 3}
set1.update(set2)
print(set1)
print("\n")
#Both union() and update() will exclude any duplicate items.


#Keep Only the Duplicates: intersection_update()
x={"apple", "banana", "cherry"}
y={"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
print("\n")

#intersection()
x={"apple", "banana", "cherry"}
y={"google", "microsoft", "apple"}
z=x.intersection(y)
print(z)
print("\n")

#Keep All, But Not the Duplicates: symmetric_difference_update()
x={"apple", "banana", "cherry"}
y={"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
print("\n")

#symmetric_difference
x={"apple", "banana", "cherry"}
y={"google", "microsoft", "apple"}
x.symmetric_difference(y)
print(x)
print("\n")

#True and 1 is considered the same value:
x={"apple", "banana", "cherry", True}
y={"google", 1, "apple", 2}
x.symmetric_difference(y)
print(x)
