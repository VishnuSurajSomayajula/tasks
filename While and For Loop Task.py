r1 = int(input("Enter the Starting Range: "))
r2 = int(input("Enter the Ending Range: "))


#Break when the number is multiple of 16
for i in range(r1,r2):
    if i%3 == 0:
        print(" * ")
        pass
    elif i%5 == 0:
        continue
    elif i%16 == 0:
        break
    else:
        print(i)
