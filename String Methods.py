#String Concatenation by using '+'
s1="Code"
s2="Gnan"
print(s1+"  "+s2)
print(s1+s2)
a1="Welcome"
a2="to"
a3="Programming"
print(a1+" "+a2+" "+a3)

#Repeation of string using '*'
string="Chaitanya  "
print(string*3)
string="* "
print(string*3)
print(string*1)
print(string*2)
print(string*3)
print(string*4)
print(string*5)

#String case conversion
s="Chaitanya"
#lower()-It converts string to lower case
print(s.lower())
#upper()-It converts string to Upper case
print(s.upper())
#swapcase()-It converts string lower to upper and upper to lower case
print(s.swapcase())
#title()- It converts the every first letter in to upper case in the sentence 
a="i am chaitanya"
print(a.title())
#capitalize()-it converts the first letter as upper case in the sentence
print(a.capitalize())

#Remove white spaces
#strip()-It removes leading and lagging whitespaces
#lstrip()-It removes leading whitespaces
#rstrip()-It removes the lagging whitespaces
s="     abc        "
s1="               "
print(s1)
print(s.strip())
print(s.lstrip())
print(s.rstrip())
s2="@@@@@@@abc@@de@@@@@"
print(s2)
print(s2.strip('@)'))
print(s2.lstrip('@'))
print(s2.rstrip('@'))

#split()-convert the string in to list of substring as per the delimiter
s="I am a python programmer"
print(s.split())
print(s.split('a'))
print(s.split('p'))
print(s.split('x'))#If the string is not present in the given string it will take the string as substring.

#join()-It combines the all iterable values in to a single substring with a seperator value
list=['I','am','python','programmer']
print(''.join(list))
print('  '.join(list))
print('@'.join(list))
print('_'.join(list))

#find(sub_string)-It returns the first position of the substring occurrence in the string otherwise "-1"
#index(sub_string)-It returns the lower or first position of the substring occurrence in the string otherwise "ValueError"
#replace(sub_string)-It replace the old substring with new substring in all occurrences
s="I am a python programmer"
print(s.find('a'))
print(s.index('a'))
print(s.replace('python programmer','Codegnan student'))
print(s.find('z'))
#print(s.index('z'))#Output for these print(s.index('z')) ValueError: substring not found

#checking functions
#isalpha()-It returns true if the string contains all alphabet values
#isalnum()-It returns true if the string contains alphabets and numbers
#isdigit()-It  returns true if the string contains all number values
s1="abcd"
s2="abc123"
s3="1234"
s4="abc@123"
print(s1.isalpha(),s2.isalpha(),s3.isalpha())
print(s1.isalnum(),s2.isalnum(),s3.isalnum())
print(s1.isdigit(),s2.isdigit(),s3.isdigit())
print(s4.isalnum())

#string comparison-It compares the lexographical order
s1="abcd"
s2="absd"
print(s1>s2)
print(s1<s2)

s="Srinubabu"
print(s.upper().replace("S","@"))

print("_".join("Srinu babu".split()))

