# Storing Data
# store the information users provide in data structures such as lists and dictionaries
# simple way to do this involves storing your data using the json module
# json module allows you to dump simple Python data structures into a file and load the data from that file

import json

# Using json.dump() and json.load()

# use json.dump() to store data
# json.dump() function takes two arguments: a piece of data to store and a file object
# list
numbers = [2, 5, 8, 10, 13]
filename = "numbers.json"
with open(filename, "w") as f_obj:
    json.dump(numbers, f_obj)

# dictionary
admin = {"username": "Admin", "password": "123@password", "age": 20, "field": "information technology"}
filename = "admin_info.json"
with open(filename, "w") as f_obj:
    json.dump(admin, f_obj)

# use json.load() to read data back into memory
# list
filename = "numbers.json"
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)

# dictionary
filename = "admin_info.json"
with open(filename) as f_obj:
    admin = json.load(f_obj)
print(admin)

# Saving and Reading User-Generated Data

username = input("Enter your name: ")
filename = "username.json"
with open(filename, "w") as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you next time, " + username.title() + "!")

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")

# if username.json does not exist, except block prompts for a username and store it in username.json for next time

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("Enter your name: ")
    with open(filename, "w") as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you next time, " + username.title() + "!")
else:
    print("Welcome back, " + username + "!")
