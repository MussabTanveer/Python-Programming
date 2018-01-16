# Reading from a File

# Reading an Entire File

# explicitly open and close file
pi_file = open("pi_digits.txt")
print(pi_file)
print(pi_file.read())
pi_file.close()

# keyword 'with' closes the file once access to it is no longer needed
with open("pi_digits.txt") as file_object:
    # read() method to read the entire contents of the file
    contents = file_object.read()
    print(contents)
    # blank line at the end of o/p appears b/c read() returns an empty string when it reaches end of file
    # to remove the extra blank line, you can use rstrip() in the print statement
    print(contents.rstrip())

# File Paths
# relative file path tells Python to look for a given location relative to directory where currently running program file is stored

with open("text_files\data.txt") as my_data_file:
    contents = my_data_file.read()
    print(contents)

# absolute file path tells Python exactly where the file is on computer regardless of where the program that’s being executed is stored
# use double backward slash

file_path = "C:\\PyWork\\LearnPythonBasics\\10-FilesAndExceptions\\text_files\data.txt"
with open(file_path) as my_data_file:
    contents = my_data_file.read()
    print(contents)

# Reading Line by Line

filename = "pi_digits.txt"
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Making a List of Lines from a File
# when you use with, the file object returned by open() is only available inside the with block
# to retain access to a file’s contents outside the with block, store the file’s lines in a list inside the block

filename = "pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# Working with a File’s Contents

filename = "pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# Python reads from a text file, it interprets all text in the file as a string
# to read in a number and work with that value, convert it to an integer using int() fn or a float using float() fn

# Large Files: One Million Digits

filename = "pi_million_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "....")  # print first 50 decimal places
print(len(pi_string))

# Is Your Birthday Contained in Pi?

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
