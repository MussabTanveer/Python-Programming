# Writing to a File
# Writing to an Empty File
# Modes of opening a file: read mode by default ('r'), write mode ('w'), append mode ('a'), read and write mode ('r+')
# open() function automatically creates the file you’re writing to if it does not already exist
# Python can only write strings to a text file
# To store numerical data in a text file, convert the data to string format first using the str() function.

filename = "programming.txt"

with open(filename, "w") as file_object:
    file_object.write("I love programming!")

# Writing Multiple Lines

with open(filename, "w") as file_object:
    file_object.write("I love programming!\n")
    file_object.write("I love creating new algorithms.\n")

# Appending to a File
# instead of writing over existing content, open the file in append mode

with open(filename, "a") as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
