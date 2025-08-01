#3.check if two strings equal or not.
s1=input()
s2=input()
if s1==s2:
    print("Strings are equal")
else:
    print("Strings are not equal")

#4.Check if a number is divisible by 3 and 5.
num=int(input())
if num%3==0 and num%5==0:
    print(f"{num} is divisible by 3 and 5")
else:
    print(f"{num} is not divisible by 3 and 5")


#5.Count Vowels and Consonants in a string.
s=input()
l=list(s)
a=['a','e','i','o','u','A','E','I','O','U']
Vowels=0
Consonants=0
for i in range(len(l)):
    if l[i] in a:
        Vowels+=1
    else:
        Consonants+=1
print(f"Vowels:{Vowels},Consonants:{Consonants}")

#6.Remove Duplications from a list While Maintaining Order
l=list(map(int,input().split()))
a=[]
for i in range(len(l)):
    if l[i] not in a:
        a.append(l[i])
    else:
        i=i+1
print(a)
        
