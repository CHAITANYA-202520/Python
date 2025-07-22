#integer conversion-int()
#float conversion-float()
#string conversion-str()
#list conversion-list()
#set conversion-set()
#tuple conversion-tuple()
#dictionary conversion-dict()

#integer to float,string
num=100
float=float(num)
print(float)
string=str(num)
print(string)
print(type(float),type(string))

#float to int,str conversion
num=100.0
i=int(num)
print(i,type(i))
s=str(num)
print(s,type(s))

#string to integer,float,set,tuple,list
s1='123'
s2='abc12a'
print(int(s1))
print(float(s1))
print(list(s2))
print(set(s2))
print(tuple(s2))

#list to set,tuple,string
lst=[1,2,3,'a','b',1,2]
print(set(lst))
print(tuple(lst))
print(str(lst))

#list of tuples to dictionary
l=[('a',2),('a',3),('c',(1,2,3))]
print(dict(l))

#dictionary to list
d={'a': 3, 'c': (1, 2, 3),'a':[1,2],'d':2}
print(list(d))

#tuple to set,list,string
t=(1,3,'Codegnan',55)
print(list(t))
print(set(t))
print(str(t))

#set to list,tuple,string
s={'Codegnan',1,3,55}
print(list(s))
print(tuple(s))
print(str(s))






























