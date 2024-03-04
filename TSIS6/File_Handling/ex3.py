import os
a=os.getcwd()
if os.access(a, os.F_OK):
    print(os.listdir(a))
else:
    print("Path does not exist!")