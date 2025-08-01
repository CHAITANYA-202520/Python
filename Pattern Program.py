#1.Square Pattern
n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
#output
5
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 

#2.
n=int(input())
for i in range(1,n):
    for j in range(1,n):
        print(j,end=" ")#j+1
    print()
#output:
1 2 3 4 
1 2 3 4 
1 2 3 4 
1 2 3 4 

#3.
n=int(input())
for i in range(1,n):
    for j in range(1,n):
        print(i,end=" ")#i+1
    print()
#output
5
1 1 1 1 
2 2 2 2 
3 3 3 3 
4 4 4 4

n=int(input())
num=1
for i in range(1,n):
    for j in range(1,n):
        print(num,end=" ")#i+1
        num+=1
    print()

#output
5
1 2 3 4 
5 6 7 8 
9 10 11 12 
13 14 15 16


#4.Right angled triangle pattern
5
*
**
***
****'''
'''n=int(input())
for i in range(1,n):
    for j in range(1,n):
        if j<i+1:
            print('*',end=" ")
        #else:
         #   print()
    print()

#5.reverse right angled pattern
5
****
***
**
*
n=int(input())
for i in range(1,n):
    for j in range(1,n):
        if j+1>i:
            print('*',end="")
    print()
#6.
5
1 2 3 4 
1 2 3 
1 2 
1 
n=int(input())
for i in range(1,n):
    for j in range(1,n-i+1):
            print(j,end=" ")
    print()

#7.
5
1 
1 2 
1 2 3 
1 2 3 4
n=int(input())
for i in range(1,n):
    for j in range(1,n):
        if i+1>j:
            print(j,end=" ")
    print()

#8.Hallow Square
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1:
            print("*",end=" ")
        else:
            if j==0 or j==n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()
#output
5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 

































