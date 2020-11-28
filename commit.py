import os

f = open("file.py", "a+")
f.write("#auto generated file \n")
f.write("#auto generated file testing ")
f.close()
#"w" operation truncates previous file

os.system('cmd /c "git add commit.py"')
os.system('cmd /c "git commit -m "this is an automated commit""')
os.system('cmd /c "git push"')