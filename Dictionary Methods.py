#Creating empty dictionary
d={}
d1=dict()
print(type(d),type(d1))

#Dictionary  values access by using keys
d={1:'a','A':2,6:4,(1,2):4,5:[1,2,(3,4),5],'A':10}
print(d[1])
print(d['A'])
print(d[5])
c=d.keys()
d=d.values()
print(c)
print(d)

d={'language':"python",'version':'3.13.5','level':'high level'}
#keys()-It returns the keys of dictionary.
keys=d.keys()
print(keys)
#values()-It returns the values of dictionary.
values=d.values()
print(values)
#items()-It returns the list of tuple of key value pairs.
items=d.items()
print(items)
print(type(keys),type(values),type(items))

#items to list type conversion
items={'language':"python",'version':'3.13.5','level':'high level'}
items_list=list(items)
print(type(items_list))
print(items_list)
a=items_list[1]
print(a)

items={'language':"python",'version':'3.13.5','level':'high level'}
#pop(key)-It pops the  value of key  if key  is present in dictionary,otherwise error
a=items.pop('version')
#b=items.pop('v') KeyError: 'v'
print(a)
print(items)
items1={'language':"python",'version':'3.13.5','level':'high level'}
#popitem()-It returns and removes the last updated item from the dictionary.
c=items1.popitem()
print(c)
print(items1)

#Accessing and updating the values
d={'language':'python','version':'3.13.5','level':'High level'}
print(d['language'])
d['A']=1
d['language']='java'
print(d)

d={'language':'Python','version':'3.13.5','level':'High level'}
#get(key,default)-It returns the value of the key ,otherwise default value.
val=d.get('language')
print(val)
val=d.get('10','value is not in the dictionary')
print(val)
d1={'language':'Python','version':'3.13.5'}
d2={'language':'Java','level':'High level'}
#update(dictionary)-It updates the new items of the dictionary.
d1.update(d2)
print(d1)
print(d2)
d1={'language':'Python','version':'3.13.5'}
d2={'language':'Java','level':'High level'}
d2.update(d1)
print(d2)
print(d1)

#clear()-It removes the all items from the dictionary
d={'language':'Python','version':'3.13.5','level':'High level'}
d.clear()
print(d)

a={'A':[1,2,3,4],3:(4,5,6,7)}
print(a['A'][3])
print(a[3][2])

