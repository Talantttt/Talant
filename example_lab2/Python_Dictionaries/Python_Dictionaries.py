#Python Dictionaries
thisdict={
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}

"""Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates."""

thisdict={
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
print(thisdict)
print("\n")

"""Dictionary Items
Dictionary items are ordered, changeable, and does not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name."""

thisdict={
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
print(thisdict["brand"])
print("\n")

#Duplicates Not Allowed
thisdict={
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964",
    "year": "2020"
}
print(thisdict)
print("\n")

#Dictionary Length
print(len(thisdict))
print("\n")

#Dictionary Items - Data Types
thisdict={
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964",
    "colors": ["red", "white", "blue"]
}
print(thisdict)
print("\n")

#type()
thisdict={
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
print(type(thisdict))
print("\n")

#The dict() Constructor
thisdict=dict(name="John", age="36", country="Norway")
print(thisdict)
