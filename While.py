a = int(input("Enter the number: "))

while a>0:
    if a%7==0:
        pass
    elif a%11==0:
        continue
    elif a%13==0:
        break
    else:
        "None"
    print(a)
    a= a+1