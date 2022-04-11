#capitalize
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

#center
x = txt.center(20)
print(x)

#count

x = txt.count("my")
print(x)

#ends with

x = txt.endswith(".")
print(x)

#find
x = txt.find("welcome")
print(x)

#index
x = txt.index("welcome")
print(x)

#isalnum

txt = "Company12"
x = txt.isalnum()
print(x)

#isalpha

txt = "CompanyX"
x = txt.isalpha()
print(x)

#isdecimal
txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)

#islower

txt = "hello world!"
x = txt.islower()
print(x)

#lower

txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

#join 

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

#istitle

txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

#isupper

txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

#replace

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

#rstrip

txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

#title

txt = "Welcome to my world"
x = txt.title()
print(x)

#split

txt = "welcome to the jungle"
x = txt.split()
print(x)