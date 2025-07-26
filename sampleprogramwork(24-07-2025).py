#1.Write a program to check whether a number is positive or not.
num=int(input())
if num>0:
    print(f"{num} is positive")
else:
    if num<0:
        print(f"{num} is negative")
    else:
        print(f"{num} is zero")

#2.Check whether a number is even or odd.
num=int(input())
if num%2==0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

#3.Find the greater of two numbers.
a=int(input())
b=int(input())
if a>b:
    print(f"{a} is Greater")
else:
    print(f"{b} is Greater")


#4.Find the largest among three numbers.
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(f"{a} is Larger")
else:
    if b>a and b>c:
        print(f"{b} is Larger")
    else:
        print(f"{c} is Larger")

#5.Check if a number is divisible by 5 and 11.
num=int(input())
if num%5==0 and num%11==0:
    print(f"{num} is divisible by 5 and 11")
else:
    print(f"{num} is not divisible by 5 and 11")

#6.Check if a year is a leap year.
year=int(input())
if (year%4==0 and year%100!=0) or year%400==0:
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")

#7.Check whether a character is a vowel or a consonant.
a=input()
b=a.lower()
l=['a','e','i','o','u']
if b in l:
    print("Character is a vowel")
else:
    print("Character is a consonant")

#8.Check whether a number is a multiple of 3 or 7.
num=int(input())
if num%3==0 or num%7==0:
    print(f"{num} is a multiple of 3 or 7.")
else:
    print(f"{num} is not a multiple of 3 or 7.")

#9.check whether a character is uppercase,lowercase,digit or special symbol.
s=input()
if s.islower():
    print(f"{s} is a LowerCase")
else:
    if s.isupper():
        print(f"{s} is a UpperCase")
    else:
        if s.isdigit():
            print(f"{s} is a digit")
        else:
            print(f"{s} is a Special Symbol")





























          
