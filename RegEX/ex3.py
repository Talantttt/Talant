import re 
x=input()
y=re.findall(r'([a-z]+_[a-z]+)', x)
print(y)