#Gmail Division


A = ["name@gmail.com", "sai@hotmail.com", "Sagar@hotmail.com", "Vinee@gmail.com","Sai@gmail.com"]
gmail = []
hotmail=[]

for i in A:
    if i.endswith("gmail.com"):
        gmail.append(i)
    else:
        hotmail.append(i)
print(gmail)
print(hotmail)