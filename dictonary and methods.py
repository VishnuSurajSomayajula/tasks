# dictonary and methods
# clear,copy,fromkeys,get,items,keys,pop,popitem,setdefault,update,values
person = {
  "name": "Sam",
  "age": "45",
  "year": 1999
}
#copy function
a = person.copy()
print(a)
#get function
a= person.get("age")
print(a)
#items
a = person.items()
print(a)
#keys   to get keys
a = person.keys()
print(a)
#pop- to delete
person.pop("age")
print(person)
#pop item
person.popitem()
print(person)
#default- not to change
a = person.setdefault("age", "2")
print(a)
#update - to update the value
person.update({"year": "2100"})
print(person)
#values- to get the values
a = person.values()
print(a)
#clear - to make it empty
person.clear()
print(person)
#
a = ('key1', 'key2', 'key3')
b = 0
dict = dict.fromkeys(a, b)
print(dict)


