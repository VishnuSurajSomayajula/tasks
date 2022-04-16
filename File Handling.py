#File Handling


# # Open function to open the file "MyFile1.txt"
# # (same directory) in read mode and
# file1 = open("E:\Codingrad\Tasks\test.py", "r")
	
# Program to show various ways to
# read data from a file.

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Creating a file
with open("E:\Codingrad\Tasks\test.py", "w") as file1:
	# Writing data to a file
	file1.write("Hello \n")
	file1.writelines(L)
	file1.close() # to change file access modes

with open("myfile.txt", "r+") as file1:
	# Reading form a file
	print(file1.read())

file1.close()