# Guess a number
for i in range(5):
    c = int(input("enter the guessing number bw 120 to 220: "))
    if c == 146:
        print(c,"the number was correct")
    else:
        print("you lost a ",i+1 , "Chance")
        