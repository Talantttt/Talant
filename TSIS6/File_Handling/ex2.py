import os
path=os.getcwd()
print(path)

if os.access(path, os.F_OK):
    print("Existence")

if os.access(path, os.R_OK):
    print("Readability")

if os.access(path, os.W_OK):
    print("Writability")

if os.access(path, os.X_OK):
    print("Executability")