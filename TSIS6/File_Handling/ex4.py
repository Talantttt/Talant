file=open(r"C:\Users\user\Desktop\Python_II\TSIS6\text.txt", "r")
count=0
for i in file:
    i.rstrip()
    count+=1
print(count)