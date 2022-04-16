#Functions and user Defined Modules



#A function is a block of code which only runs when it is called.


def my_func(fname, lname):
  print(fname + " " + lname)

my_func("Samuel","Sekhar")

#Arbitary Arguments

def my_function(*kids):
  print("The youngest child is " + kids[1])

my_function("Sagar", "Choclate", "Sam")
