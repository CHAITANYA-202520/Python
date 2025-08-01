#Types of output formatting
#1.Using Old style formatting[using comma method]
name="siva"
age=25
email="siva@gmail.com"
print("Name:",name,"Age:",age,"Email:",email)
print('Name:',name,'Age:',age,'Email:',email)
#2.Using Modulo operator
#%s-string
#%d-integers
#%f-float
print("Name:%s, Age:%d, Email:%s"%(name,age,email))
print('Name:%s, Age:%d, Email:%s'%(name,age,email))
#3.Using F-format Method
print(f"Name:{name},Age:{age},Email:{email}")
val=25.0000034
print(f'Name:{name},Age:{val:.4f},Email:{email}')
#4.Using Dot-Format Method
print("Name:{},Age:{},Email:{}".format(name,age,email))
print('Name:{},Age:{},Email:{}'.format(name,age,email))

#Conditional Statements/Decision Making Statements
#1.if
#If condition is true it will execute if block otherwise execute after if block.
#Syntax: if condition:
             #if block code
#Example
a=10
b=20
if a==20:
    print(a+30)
print(a+b)
#Check Whether the number is zero
num=int(input())
if num==0:
    print("The input number is zero")
print("Program Done")
#2.if-else
#If condition is true it will execute if block code otherwise execute else block code.
#Syntax:  if condition:
                   #if block code
          #else:
                   #else block code
#Example-1:To Check whether a person is eligible for vote are not.
age=int(input())
if age>=18:
    print(f"{age} years person is eligible for vote")
else:
    print(f"{age} years person is not eligible for vote")
#Example-2:Write a program whether the number is positive are not.
num=int(input())
if num>0:
    print("The number is Positive:",num)
else:
    print("The number is Negative:",num)
              
#3.if elif else-If the if condition false it checks the elif condition otherwise else condition.
a,b,c=map(int,input().split())
if a>b and a>c:
    print(f"{a} is Greater")
elif b>a and b>c:
    print(f"{b} is Greater")
else:
    print(f"{c} is Greater")


