#creating empty set
s=set()
print(s)
print(type(s))
s1={}
print(s1)
print(type(s1))

s={1,2,3,'Codegnan',(1,2)}
s.add(3)
print(s)
#s={1,2,3,'Codegnan',(1,2),[1,2,3]}
#print(s)-TypeError: unhashable type: 'list'
#print(s[0])-TypeError: 'set' object is not subscriptable

#sets allows unique elements
s={1,1,2,1,2,1}
print(s)

#sets read inputs integer values  from the user
s=set(map(int,input().split()))
print(s)

#sets read inputs  float values from the user
s=set(map(float,input().split()))
print(s)

#sets read inputs  float values from the user
s=set(map(str,input().split()))
print(s)'''

'''s={1,2,3,4}
print(s)
#add(element)-Add element to the set.
s.add(100)
print("After add operation:",s)
#update(iterable)-It update the current set with new  iterable element.
s.update([1,20,30])
print("After update operation:",s)
#remove(element)-It removes the element from the set,otherwise "keyError".
s.remove(2)
print("After remove operation:",s)
#discard(element)-It removes the element from the set,otherwise does nothing.
s.discard(20)
print("After discard operation:",s)
#pop()-It removes the random element from the set.
val=s.pop()
print("After pop operation:",val,s)
#clear()-It removes all the elements from the set.
s.clear()
print("After clear operation:",s)

s={1,2,3,4,100}
print("Original set:",s)
s.add(100)
print(s)

#s.remove(101)
#print(s)#KeyError: 101

s.discard(101)
print(s)

#s=set()
#s.pop()
#print(s)#KeyError: 'pop from an empty set'

#union(),intersection(),difference(),symmetric_difference()
s1={1,2,3,4}
s2={3,4,5,6}
union=s1.union(s2)
intersection=s1.intersection(s2)
difference=s1.difference(s2)
symmetric_difference=s1.symmetric_difference(s2)
print(union,intersection,difference,symmetric_difference)

#issubset(),issuperset(),isdisjoint()
s1={1,2,3,4,5,6}
s2={4,6}
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.isdisjoint(s2))
print(s2.issubset(s1))

