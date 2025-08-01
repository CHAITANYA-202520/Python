#1.write a python program to find sum of array.
l=list(map(int,input().split()))
a=0
for i in range(len(l)):
    a+=l[i]
print("Sum of Array:",a)

#2.Write a python program to find largest element in an array
l=list(map(int,input().split()))
Max_element=l[0]
for i in range(1,len(l)):
    if l[i]>Max_element:
        Max_element=l[i]
print(f"{Max_element} is the Largest Element in an array")

#3.Write a python program for array rotation
l=list(map(int,input().split()))
option=input("Enter the which option you want 1.Left Rotation 2.Right Rotation")
rotations=int(input("Enter how many times to rotate"))
n=len(l)
rotations=rotations%n
if option=="1":
    for _ in range(rotations):
        l.append(l.pop(0))
elif option=='2':
    for _ in range(rotations):
        l.insert(0,l.pop())
else:
    print("Invalid option")
print("Rotation array:",l)

#4.Write a python program to split the array and add the first part to the end.
l=list(map(int,input().split()))
a=len(l)//2
first_part=l[:a]
second_part=l[a:]
result=second_part+first_part
print("Modified Array:",result)























        

    
