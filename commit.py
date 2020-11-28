import os

file = open("file.py", "w+")
print(file)
file.write("#auto generated file testing")
file.close()

f = open("file.py", "w")
f.write("#auto generated file \n")
f.write("#auto generated file testing ")
f.close()
f = open("file.py", "a+")
f.write("#auto generated file \n")
f.write("#auto generated file testing ")
f.close()