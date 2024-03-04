a=open(r"C:\Users\user\Desktop\Python_II\TSIS6\copy_file.txt","w")
for word in open(r"C:\Users\user\Desktop\Python_II\TSIS6\text.txt"):
    a.write(word)
a.close()