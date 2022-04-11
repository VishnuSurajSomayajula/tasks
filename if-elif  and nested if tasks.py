#looping Statements , Conditional
# if -elif -else ,nested-if, for , while

a = float(input("Enter the 1st Value: "))
b = float(input("Enter the 2nd Value: "))
c = float(input("Enter the 3rd Value: "))
d = float(input("Enter the 4th Value: "))

if a > b :
    if a > c and a > d:
        print(a,"is the biggest value ")
    elif a > c or a > d :
        if c > d :
            print(a, "is the 2nd biggest value  after ",c)
        else:
            print(a, "is the 2nd biggest value after ",d)
    else:
        print(a, " is the 3rd biggest value after ",c," ", d)
elif b > c :
    if b > a and b > d:
        print(b,"is the biggest value ")
    elif b > a or b > d :
        if a > d :
            print(b, "is the 2nd biggest value  after ",a)
        else:
            print(b, "is the 2nd biggest value after ",d)
    else:
        print(b, " is the 3rd biggest value after ",a," ", d)
elif c > d :
    if c > a and c > d:
        print(c,"is the biggest value ")
    elif c > a or c > d :
        if a > d :
            print(c, "is the 2nd biggest value  after ",a)
        else:
            print(c, "is the 2nd biggest value after ",d)
    else:
        print(c, " is the 3rd biggest value after ",a," ", d)

else:
    print(d, "is the biggest Value")
