#1.Check whether a number is positive,negative,or zero and even/odd.
num=int(input())
if num>0:
    print(f"{num} is Positive")
    if num%2==0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
elif num<0:
    print(f"{num} is Negative")
    if num%2==0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
else:
    print(f"{num} is Zero")
    print(f"{num} is neither Even or Odd")

#2.Assign grades based on marks(90+:A+.80-89:A,etc)
marks=int(input())
if marks>=90:
    print(f"{marks}:A+ grade")
elif marks>=80:
    print(f"{marks}:A grade")
elif marks>=70:
    print(f"{marks}:B+ grade")
elif marks>=60:
    print(f"{marks}:B grade")
elif marks>=50:
    print(f"{marks}:c grade")
elif marks>=40:
    print(f"{marks}:Pass grade")
else:
    print(f"{marks}:Fail grade")

#3.Create a simple calculator using +,-,*,/ operators.
a=int(input())
b=int(input())
option=input("Enter the which operation you want +.Addition ,-.Subtraction,*.Multiplication,/.Division")
if option=='+':
             print(f"Addition of {a} and {b} is {a+b}")
elif option=='-':
    print(f"Subtraction of {a} and {b} is {a-b}")
elif option=='*':
    print(f"Multiplication of {a} and {b} is {a*b}")
else:
    print(f"Division of {a} and {b} is {a/b}")

#4.Check whether a triangle is valid based on the sum of its angles.
a,b,c=map(int,input().split())
if a+b+c==180:
    print(f"Sum of angles of {a},{b} and {c}=180 then the triangle is valid")
else:
    print(f"Sum of angles of {a},{b} and {c}!=180 then the triangle is invalid")
    
    
#5.Check if a number is divisible by 3 and 5.
num=int(input())
if num%3==0 and num%5==0:
    print(f"{num} is divisible by 3 and 5")
else:
    print(f"{num} is not divisible by 3 and 5")

#6.Determine if a number is a three digit number.
num=int(input())
if num<=999 and num>=100:
    print(f"{num} is a three digit number")
else:
    print(f"{num} is not a three digit number")

#7.Check if a number is even and multiple of 7.
num=int(input())
if num%2==0 and num%7==0:
    print(f"{num} is even and multiple of 7")
else:
    print(f"{num} is not even and multiple of 7")

#8.Determine the type of triangle(Equilateral,Isosceles,Scalene) using sides.
a,b,c=map(int,input().split())
if a==b==c:
    print(f"{a},{b} and {c} all three sides are equal it is a Equilateral Triangle")
elif a==b!=c or a!=b==c or a==c!=b:
    print(f"{a},{b} and {c} two sides are equal it is a Isosceles Triangle")
else:
    print(f"{a},{b} and  {c}  are no side is equal it is a Scalene Triangle")

#9.Calculate electricity bill based on slab-wise rates.
units=int(input())
if units<=100:
    a=units*1.50
    print(f"{a} amount for electricity bill for {units} units")
else:
    if units<=200:
        a=100*1.50
        b=units-100
        c=b*2.00
        total=a+c
        print(f"{total} amount for electricity bill for {units} units")
    elif units<=330:
        a=100*1.50
        b=100*2.00
        c=units-200
        d=c*3.00
        total=a+b+d
        print(f"{total} amount for electricity bill for {units} units")
    else:
        a=100*1.50
        b=100*2.00
        c=130*3.00
        d=units-330
        e=d*5.00
        total=a+b+c+e
        print(f"{total} amount for electricity bill for {units} units")



#10.Check if a number is within a range(eg.,50-100)
num=int(input())
if num>=50 and num<=100:
    print(f"{num} is within a range of 50-100")
else:
    print(f"{num} is not within a range of 50-100")

#11.Check whether a given year is a century year.
year=int(input())
if year%100==0:
    print(f"{year} is a Century Year")
else:
    print(f"{year} is not a Century Year")


#12.Compare two numbers and display the greater and the difference.
a,b=map(int,input().split())
if a>b:
    print(f"{a} is Greater")
    print(f"{a-b} is the Difference of {a} and {b}")
else:
    print(f"{b} is Greater")
    print(f"{b-a} is the Difference of {a} and {b}")

#13.Check if a day number(1-7) corresponds to weekday or weekend.
day=int(input())
if day%7==0:
    print(f"{day} is a Sunday")
elif day%7==1:
    print(f"{day} is a Monday")
elif day%7==2:
    print(f"{day} is a Tuesday")
elif day%7==3:
    print(f"{day} is a Wednesday")
elif day%7==4:
    print(f"{day} is a Thursday")
elif day%7==5:
    print(f"{day} is a Friday")
else:
    print(f"{day} is a Saturday")

#14.Check if three sides can form a right-angled triangle.
a,b,c=map(int,input().split())
if a>b and a>c:
    if a**2==b**2+c**2:
        print(f"{a},{b} and {c} sides form a right-angled triangle")
    else:
        print(f"{a},{b} and {c} sides cannot form a right-angled triangle")
elif b>a and b>c:
    if b**2==a**2+c**2:
        print(f"{a},{b} and {c} sides form a right-angled triangle")
    else:
        print(f"{a},{b} and {c} sides cannot form a right-angled triangle")
elif c>a and c>b:
    if c**2==a**2+b**2:
        print(f"{a},{b} and {c} sides form a right-angled triangle")
    else:
        print(f"{a},{b} and {c} sides cannot form a right-angled triangle")


#15.Find the roots of a quadratic equation and display their nature.
a,b,c=map(int,input().split())
d=((b**2)-(4*a*c))
if d>0:
    e=d**0.5
    root1=(-b+e)/(2*a)
    root2=(-b+e)/(2*a)
    print(f"{root1} and {root2} are roots and the Nature is Two Distinct Real roots")
elif d==0:
    root1=(-b)/(2*a)
    print(f"{root1} and {root2} are roots and the Nature is Two Equal Real roots")
else:
    e=d**0.5
    root1=(-b+e)/(2*a)
    root2=(-b+e)/(2*a)
    print(f"{root1:.2f} and {root2:.2f} are roots and the Nature is Two Complex(imaginary) roots")
    






























    
    


































































        
