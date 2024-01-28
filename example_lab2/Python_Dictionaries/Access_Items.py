#Accessing Items
thisdict={
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
x=thisdict["model"]
print(x)
print("\n")

#get()
x=thisdict.get("model")
print(x)
print("\n")

#Get Keys
x=thisdict.keys()
print(x)
print("\n")

car={
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
x=car.keys()

print(x) # before the change

car["color"]= "white"

print(x) #after the change

#Get Values
x=thisdict.values()
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

#Get Items
x=thisdict.items()
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change



car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

#Check if Key Exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
