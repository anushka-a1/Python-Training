# file handling in python
# open a file
f = open("temp.txt", "w")
# write to a file single line
""" # f.write("Hello, World!\n")
# f.write("Welcome to file handling in Python.\n") """
# writing multiple lines to a file
f.writelines(["This is the first line.\n", "This is the second line.\n", "This is the third line.\n"])
# close the file
f.close()

# read a file 
f = open("temp.txt", "r")
# read the entire file
print(f.read()) 
# read a file line by line, repeating the process until the end of the file is reached
""" print(f.readline()) """
# read all lines into a list
""" print(f.readlines()) """
# close the file
f.close()   

# read and write to a file
f= open("temp.txt", "w+")
f.write("This is a new line.\n") 
f.seek(0) # move the file pointer to the beginning of the file
print(f.read()) # this will not print anything without the seek() call because the file pointer is at the end of the file after writing
f.close() #not closing the file will lead to memory leak and data loss, so it is important to close the file after use. but not necessary if we use with statement to open the file, as it will automatically close the file after the block of code is executed.

# append to a file
f=open("temp.txt","a")
f.write("This line is appended to the file.\n") #it will not overwrite the existing content of the file, but will add the new line at the end of the file. if we use "w" mode to open the file, it will overwrite the existing content of the file with the new content. if we use "a" mode to open the file, it will append the new content to the existing content of the file without overwriting it.
f.close()

# append and read a file
f=open("temp.txt","a+")
f.write("This second line is appended to the file.\n")
f.writelines(["This is the third line.\n", "This is the fourth line.\n"])
f.seek(0) # move the file pointer to the beginning of the file
print(f.read()) # this will print the contents of the file
f.close()