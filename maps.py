
#Map.

def addition(n):
	return n + n

# We double all numbers using map()
nums = (1, 2, 3, 4)
result = map(addition, nums)
print(list(result))
