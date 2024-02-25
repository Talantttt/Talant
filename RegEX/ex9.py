import re 
x=input()
y=re.compile('(?=[A-Z])')
z=y.sub(' ', x)
print(z)