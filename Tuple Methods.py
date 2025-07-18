'''#Creating empty tuple
t1=()
t2=tuple()
print(type(t1),type(t2))

t1=(1,2,3,'a','b',"Codegnan",[4,5],7,12.5)
#immutable
#t1[0]=100 --TypeError: 'tuple' object does not support item assignment
#index based and sliceable
print(t1[0])
print(t1[-1])
print(t1[2:-3:1])
print(t1[-2:6:1])
print(t1[4:100])
    
#tuple with multiple values
t3=(1,2,3,"Codegnan")
#tuple with single values
t4=(10)
print(type(t3),type(t4))
t4=(10,)
print(type(t4))

#Read tuple from user 
tuple=tuple(map(int,input().split()))
print(tuple)'''

#tuple concatenation using '+'
t1=(1,2,3,'Hi',[1,2,23],2,21,3)
t2=(4,5,6,'Welcome')
print(t1+t2)

#tuple repeatition using '*'
print(t1*3)

#index(value)-It return the position of  value in the tuple otherwise "ValueError"
ind=t1.index(2)
print("Index of 2 element is:",ind)
#count(value)-It returns the total occurrence of value in the tuple
count=t1.count(2)
print("Count of 2 element is:",count)
#min()-It returns the min value in the tuple
#max()-It returns the max value in the tuple
#sum()-It returns the sum of values in the tuple
#len()-It returns the length of elements in the tuple
t=(1,8,5,4,7,3,6,9)
print("Minimum value in the tuple:",min(t))
print("Maximum value in the tuple:",max(t))
print("Sum of values in the tuple:",sum(t))
print("Length of  values in the tuple:",len(t))

#sorted-It sort the tuple in particular order and it returns new sorted tuple oo values
new_sort1=sorted(t,reverse=False)#Ascending order
new_sort2=sorted(t,reverse=True)#Descendi0ng order
print("Ascending order:",new_sort1)
print("Descending order:",new_sort2)

