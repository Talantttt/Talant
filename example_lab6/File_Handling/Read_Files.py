#Python File Open

#Open a file on the Server
#Assume we have the following file, located in the same folder as Python:

#demofile.txt:
"""Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!"""

#To open the file, use the built-in open() function.

#The open() function returns a file object, which has a read() method for reading the content of the file:
f=open("demofile.txt", "r")
print(f.read())

#If the file is located in a different location, you will have to specify the file path, like this:
f=open("C:\Users\user\Desktop\Python_II\example_lab6\demofile.txt", "r")
print(f.read())

#Reads Only Parts of the File
#By default the read() method returns the whole text, but you can also specify how many characters you want to return:

f=open("demoofile.txt", "r")
print(f.read(5))

#Read Lines: readline()
f=open("demofile.txt", "r")
print(f.readline())

#By calling readline() two times, you can read the two first lines:
f=open("demofile.txt", "r")
print(f.readline())
print(f.readline())

#By looping through the lines of the file, you can read the whole file, line by line:
f=open("demofile.txt", "r")
for x in f:
    print(x)

#Close Files
f=open("demofile.txt", "r")
print(f.readline())
f.close()
#Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.