print("         Welcome to Lovely Dhaba     ")
name = input("Enter Your name: ")
adhaarid = input("Enter the Aadhar id: ")
check_in_hours = input("check in time in hours: ")
check_in_minutes = input("check in time in minutes: ")
number_of_days = int(input("enter number of days to stay: "))
mode = input("enter the mode AC / NON-AC: ")
mode = mode.upper()
e=0
foodie ={
        "biryani": 200,
        "drinks":50,
        "veg biryani":150,
        "panner": 150
    }
n = int(input("no of items: "))

print(foodie)
for i in range (n):
    d = input("enter the item: ")
    d = d.lower()
    e = e+foodie.get(d)
check_out_hours = input("check out time in hours: ")
check_out_minutes = input("check out time in minutes: ")

if mode == "AC":
    e = e+150  
else:
    e = e+50
g = 250 * number_of_days
bill = e+g

print("Your Bill is Generating...")

print("Customer Name: ", name)
print("Customer Aadhar Id is :",adhaarid)
print("Check-in time of user is:",check_in_hours,":",check_in_minutes)
print("Number of Days Customer Stayed is :", number_of_days)
print(" Customer Stayed in :", mode.upper())
print("Total Bill is :", bill)
print("Check-out time of user is:",check_out_hours,":",check_out_minutes)