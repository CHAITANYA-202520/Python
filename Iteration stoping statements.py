#Iteration Stoping Statements
#1.break
#2.continue
#3.pass
#1.break-It exits the current loop when a break statement encounter
n=8
for i in range(n):
    if i==4:
        break
        print("Four",end="")
    print(i,end=" ")
print()
print("Program Done")

#2.continue-It skips the current iteration when a continue statement encounter and it goes to next iteration.
n=8
for i in range(n):
    if i==4:
        continue
        print("Four",end="")
    print(i,end=" ")
print()
print("Program Done")

#3.pass-It allows you to write code that is  syntatically correct but intentionally doed nothing in that block.
for i in range(8):
    if i==2:
        pass
    else:
        print(i,end=" ")
for i in range(7):
    pass
