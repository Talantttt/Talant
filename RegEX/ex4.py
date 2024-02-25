import re 
x=input()
y=re.findall(r'[A-Z][a-z]+',x)
print(y)