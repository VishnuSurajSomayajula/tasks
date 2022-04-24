#Code
n = int(input("Enter the Number: "))

flag = 0

if len(str(n))<3:
    print(n, "- not a fascinating number.")

else:
    n1 = n
    n2 = n * 2
    n3 = n * 3
    total = str(n1)+str(n2)+str(n3)
    print(total)
    for num in total:
        if len(total)!=9 or total.count(num)>1 or total.count(num)==0:
            flag = 1
            break
    if flag == 1:
        print(n ," is not a fascinating number.")
    else:
        print(n, "is a fascinating number")