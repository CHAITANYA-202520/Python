#creating empty string
s=' '
s1=" "
s2=str()
print(type(s))
print(type(s1))
print(type(s2))
#String slicing
s="abcde"
#######Forward indexing
#String slicing without end index
print(s[0:])
#string slicing without start index
print(s[:5])
#string slicing without start and end index
print(s[:])
#string slicing with start and end index
print(s[0:5])
#######Backward indexing
#String slicing without end index
print(s[-1: :-1])
#string slicing without start index
print(s[:-5:-2])
#string slicing with start and end index
print(s[-2:-5:-1])
