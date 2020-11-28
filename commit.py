import os

for i in range(6):
    f = open("file.py", "a+")
    f.write("#auto generated file \n")
    f.write("#auto generated script for testing\n")
    f.close()
    #"w" operation truncates previous file

    os.system('cmd /c "git add file.py"')
    os.system('cmd /c "git commit -m "this is an automated commit""')
    os.system('cmd /c "git push"')