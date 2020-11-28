import os

f = open("file.py", "a+")
f.write("#auto generated file \n")
f.write("#auto generated file testing ")
f.close()
#"w" operation truncates previous file