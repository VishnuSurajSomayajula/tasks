# pop,append, extend, copy, clear, count, index, remove, reverse ,sort

lst = ["vinee", "vampire", "suraj"]
print(lst)
# pop function

lst.pop()
print(lst)

# append

lst.append("Sai")
print(lst)

# copy
lst2 = lst.copy()
print(lst2)

# clear
lst2.clear()
print(lst2)

# count
print(lst.count("Sai"))

# index
print(lst.index("vinee"))

# remove
lst.remove("vinee")
print(lst)

# sort

lst.sort()
print(lst)

# reverse

lst.reverse()

# extend

lst2 = [1, 2, 4]
lst1 = [4, 5, 6]

lst3 = lst1.extend(lst2)
print(lst3)
