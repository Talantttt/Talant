import os 
path=os.getcwd()
print("list only directories: ",[dir for dir in os.listdir(path) if os.path.isdir(dir)])
print("list only files: ",[file for file in os.listdir(path) if os.path.isfile(file)])
print("directories and files ",os.listdir(path))