import re
x=input()
y=re.match("a{1}b{2,3}", x)
print(y)