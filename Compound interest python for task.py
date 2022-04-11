#Compound interest CI = P(1+r/100)^t

P = int(input("Enter the Principal Amount: "))
T = int(input("Enter the Time in years: "))
R = float(input("Enter the rate of interest: "))

Compound_interest = P * pow((1+(R/100)),T)

print("Compound interest :" , Compound_interest)