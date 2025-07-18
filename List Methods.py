lst=list("Codegnan")
print(lst)
print('_'.join(list('Codegnan')))

#creating empty list
l=[]
l1=list()
print(type(l))
print(type(l1))

l=[1,2,3,"Hi","a",12.5,36.4]
print(l[-1])
l[0]=22
print(l)

c="Chaitanya"
c1=list(c)#String to list type casting
print(type(c))
print(type(c1))
print(c1)

l1=list(map(int,input().split()))#reading  list of integer values from user
print(l1)

l2=list(map(str,input().split()))#reading list of string values from user
print(l2)

l3=list(map(float,input().split()))#reading list of float values from user
print(l3)

#append(value)-It add the single value at the end of the list
l=[1,2,3,'Hi','Hello',10.5,22,2,2,3]
l.append(100)
print("After append operation:",l)
#extend(value)-It adds the iterable values at the end of the list
l.extend([22,85])
print("After extend operation:",l)
#insert(position,value)-adds the specified position value and followed  value are right shifted
l.insert(1,'Welcome')
print("After insert operation:",l)
#remove(value)-It remove the value of first occurrence position
l.remove(2)
print("After remove operation:",l)
#pop(value)-returns and remove the pop value at specified position,otherwise pop value at last valu
l.pop(0)
print(l)
l.pop()
print("After pop operation:",l)
#del(value)-It removes the list
del(l[0])
del(l[2:5])
print("After del operation:",l)
#clear(value)-It removes all elements in the list
l.clear()
print("After clear operation:",l)
l=[1,2,3,'Hi','Hello',10.5,22,2,2,3]
a=l.remove(3)
b=l.pop()
print(l)
print(a,b)
#min(list_name)-returns the min value from the list
#max(list_name)-returns the max value from the list
#sum(list_name)-sum the all elements in the list
l=[12,35,88,45,6,7,2,3,5,2,3,2,5,2,3]
min_val= min(l)
max_val= max(l)
sum_val= sum(l)
print("Mininmum value in the list:",min_val)
print("Maximum value in the list:",max_val)
print("sum of  values in the list:",sum_val)
#count(value)-returns the total occurrence of the value in the list
count_value=l.count(2)
print("After performing count operation on value 2 is:",count_value)
#index(value)-It returns the value of first  position,otherwise ValueError
index_value=l.index(2)
print("After performing index operation on value 2 is:",index_value)
#index_value=l.index(2000)
#print("After performing index operation on value 2 is:",index_value)
#len(list_name)-returns the total elements of the list or length of the list
length=len(l)
print("length of the list:",length)
print(l[-1])
#reverse()-It reverse the original list in reverse order
l.reverse()
print("After performing reverse operation:",l)
#sort()-It sorts the original list in particular order
l.sort()#Ascending order
print("After performing sort operation:",l)
l.sort(reverse=True)#Descending order
print("After performing reverse operation with Descending order:",l)
#sorted()-It sorts the list in particular order and it returns the new sorted list of values
new_list=sorted(l)
print("After performing sorted operation:",new_list)


