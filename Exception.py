#Exception

# No exception Exception raised in try block
a = int(input("Enter the numerator number: "))
b = int(input("enter the denominator number: "))
try:
	k = a//b # raises divide by zero exception.
	print(k)

# handles zerodivision exception
except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	# this block is always executed
	# regardless of exception generation.
	print('This is always executed')
