import re 
#file = open(fr'C:\Users\user\Desktop\Python_II\TSIS5\row.txt', 'r', encoding='utf-8')
x=input()
y=re.match(r'a(b*)+',x)
print(y)