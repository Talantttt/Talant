thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


#Loop Through a Dictionary
for x in thisdict:
    print(x)
print("\n")

for x in thisdict:
    print(thisdict[x])
print("\n")

#values
for x in thisdict.values():
    print(x)
print("\n")

#keys()
for x in thisdict.keys():
    print(x)
print("\n")

#items
for x in thisdict.items():
    print(x)
