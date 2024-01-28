#Boolean Values
print(10>9)
print(10==9)
print(10<9)
print("\n")

a=200
b=33
if b>a:
    print("b is grater than a")
else:
    print("b is not grater than a")
print("\n")
#Evalute Values and Variables
print(bool("Hello"))
print(bool(15))
print("\n")

x="Hello"
y=15
print(bool(x))
print(bool(y))
print("\n")


#Most values are true
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
print("\n")

#Some Values are False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
print("\n")

class myclass:
    def __len__(self):
        return 0

myobj=myclass()
print(bool(myobj))
print("\n")

#Functions can Return a Boolean
def myFunction() :
    return True

print(myFunction())
print("\n")

def myFunction():
    return True 
if myFunction():
    print("YES!")
else:
    print("NO!")
print("\n")

x=200
print(isinstance(x,int))
