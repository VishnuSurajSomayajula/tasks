# index, find, format, capitalize, lower, center, count, split, ends with, starts with, join, l-strip, r-strip,
# isdigit,isdecimal remove prefix, title, remove suffix,replace


s = "Sam is a good boy"

# index
print(s.index("Sam"))

# find
print(s.find("good"))

# capitalize

s.capitalize()
print(s)

# lower

s.lower()
print(s)

# upper
s.upper()
print(s)

# center
m = s.center(len(s))
print(m)

#count
print(s.count("a"))

#split

s1 = s.split()
print(s1)

# ends with
e = s.endswith("od")
print(e)

#starts with

ee = s.startswith("go")
print(ee)

#join

ss = "ss is a s s"
s3 = s.join(ss)
print(s3)

#lstrip

r = "  is a good boy  "
print(len(r))
m = r.lstrip(r)
print(m)

#rstrip
print(len(r))
m = r.rstrip(r)
print(m)

#length of string

print(len(r))

#isdigit
