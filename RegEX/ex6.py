import re
x=input()
y=re.sub(r'[\s,.]',r':',x)
print(y)