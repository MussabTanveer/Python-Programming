# Handling the FileNotFoundError Exception

filename = "ali_baba.txt"

# with open(filename) as f_obj:  FileNotFoundError: No such file or directory: 'ali_baba.txt'
#     contents = f_obj.read()

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("Sorry, the file '" + filename + "' does not exist or is missing")

# Analyzing Text
# the string method split() build a list of words from a string

title = "Pride and Prejudice"
print(title.split())

line = "Row, row, row your boat"
print(line.count("row"))  # 2
print(line.lower().count("row"))  # 3

filename = "alice.txt"

try:
    with open(filename, encoding="utf8") as file_obj:  # specify encoding when opening file
        contents = file_obj.read()
except FileNotFoundError:
    print("Sorry, the file '" + filename + "' does not exist.")
else:
    words = contents.split()
    print("The file " + filename + " has about " + str(len(words)) + " words.")

# Working with Multiple Files


def count_words(filename):
    """Count the number of words in a file"""
    try:
        with open(filename, encoding="utf8") as file_obj:  # specify encoding when opening file
            contents = file_obj.read()
    except FileNotFoundError:
        print("Sorry, the file '" + filename + "' does not exist.")
    else:
        words = contents.split()
        print("The file " + filename + " has about " + str(len(words)) + " words.")

filename = "alice.txt"
count_words(filename)

filenames = ["alice.txt", "moby_dick.txt", "sacajawea.txt", "little_women.txt"]
for filename in filenames:
    count_words(filename)

# Failing Silently


def count_words(filename):
    """Count the number of words in a file"""
    try:
        with open(filename, encoding="utf8") as file_obj:  # specify encoding when opening file
            contents = file_obj.read()
    except FileNotFoundError:
        pass  # Python has a pass statement that tells it to do nothing in a block
    else:
        words = contents.split()
        print("The file " + filename + " has about " + str(len(words)) + " words.")

filenames = ["alice.txt", "moby_dick.txt", "sacajawea.txt", "little_women.txt"]
for filename in filenames:
    count_words(filename)
