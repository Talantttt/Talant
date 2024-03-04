a=open(r"C:\Users\user\Desktop\Python_II\TSIS6\file.txt", "w")
list= list(input().split())
for word in list:
    a.write(str(word)+'\n')