n=5
for i in range (1, n+1):
    for j in range (i+1):
        print(i,end=" ") 
    print(" ")


# 1 1  
# 2 2 2        
# 3 3 3 3      
# 4 4 4 4 4    
# 5 5 5 5 5 5    

n= int(input("enter the value"))
A= int(n/2+1)
for i in range(1, A):
    print(' '*n, end='') 
    print('* '*(i))

#output
#    enter the value20
#                     *       
#                     * *     
#                     * * *   
#                     * * * * 
#                     * * * * *
#                     * * * * * *
#                     * * * * * * *
#                     * * * * * * * *
#                     * * * * * * * * *
#                     * * * * * * * * * *

n=5
for i in range(n):
    for j in range(1, n-i):
        print(" ", end="")
    for k in range(0, i+1):
        print("*", end="")
    print()

# #output
#     *
#    **
#   ***
#  ****
# *****

n=5
for i in range(5):
    for j in range(i):
        print(" ", end="")
    for j in range(5, i, -1):
        print("*", end="")      
    print()

# #output
# *****
#  ****
#   ***
#    **
#     *


n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print()

 #output
#     *
#    ***   
#   *****  
#  ******* 
# *********