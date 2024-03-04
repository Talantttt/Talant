import os
if os.path.exists(r"C:\Users\user\Desktop\Python_II\TSIS6\delete_file.txt"):
    os.remove(r"C:\Users\user\Desktop\Python_II\TSIS6\delete_file.txt")
else:
    print("file does not exist")