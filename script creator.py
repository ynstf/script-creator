import os
os.system('cls')
print("WELCOM TO PYTHON SCRIPT CREATOR")
print("writ your codes lines")
print("writ exit to finish")

f=open("test.py", "w")
while True:
    line = input(">> ")
    if line == "exit" or line == "EXIT" :
        f.close
        break
    with open("test.py", "a+") as f:
        line = line + "\n"
        f.write(line)
    


q=input("you wanna run it ? ")
if q=="yes" or q=="YES" or q=="y" or q=="Y":
    os.system('test.py')
else:
    print("your script is ready as test.py")
