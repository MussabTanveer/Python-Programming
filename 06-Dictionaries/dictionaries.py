# A Simple Dictionary
person = {"name": "Max", "age": 10}
print(person["name"])
print(person["age"])

# Working with Dictionaries
# Accessing Values in a Dictionary
person = {"name": "Max", "age": 10}
print("Name: " + person["name"] + "\nAge: " + str(person["age"]))

# Adding New Key-Value Pairs
person = {"name": "Max", "age": 10}
print(person)
person["email"] = "abc@yahoo.com"
person["gender"] = "male"
print(person)

# Starting with an Empty Dictionary
person = {}
person["name"] = "John"
person["age"] = 5
print(person)

# Modifying Values in a Dictionary
flower = {"color": "red"}
print("The flower color is " + flower["color"])
flower["color"] = "yellow"
print("The flower color is now " + flower["color"])

# Removing Key-Value Pairs
# deleted key-value pair is removed permanently
car = {"color": "blue", "model": 2009}
print(car)
del car["model"]
print(car)

# A Dictionary of Similar Objects
favourite_ice_cream = {
    "john": "vanilla",
    "mark": "chocolate",
    "kevin": "mango",
    "george": "strawberry",
}
print("Kevin's favorite ice cream is " + favourite_ice_cream["kevin"])

# Looping through a Dictionary
# Looping Through All Key-Value Pairs
user = {
    "username": "mark",
    "password": "tower",
    "age": 20,
}
print(user)
for k, v in user.items():
    print("Key: " + k + "\nValue: " + str(v))

# Looping Through All the Keys in a Dictionary
favourite_ice_cream = {
    "john": "vanilla",
    "mark": "chocolate",
    "kevin": "mango",
    "george": "strawberry",
}
for name in favourite_ice_cream.keys():
    print(name.title())
if "oliver" not in favourite_ice_cream.keys():
    print("Oliver please tell your favorite ice cream!")

# Looping Through a Dictionary’s Keys in Order
favourite_ice_cream = {
    "john": "vanilla",
    "mark": "chocolate",
    "kevin": "mango",
    "george": "strawberry",
}
for name in sorted(favourite_ice_cream.keys()):
    print(name.title() + ", everybody knows your favorite ice cream")

# Looping Through All Values in a Dictionary
# repetitions repeated
favourite_ice_cream = {
    "john": "vanilla",
    "mark": "chocolate",
    "kevin": "mango",
    "george": "vanilla",
}
print("Favorite ice creams:")
for ice_cream in favourite_ice_cream.values():
    print(ice_cream.title())
# repetitions repeat once
favourite_ice_cream = {
    "john": "vanilla",
    "mark": "chocolate",
    "kevin": "mango",
    "george": "vanilla",
}
print("Favorite ice creams:")
for ice_cream in set(favourite_ice_cream.values()):
    print(ice_cream.title())

# Nesting
# A List of Dictionaries
person_1 = {"name": "Alfred", "age": 30}
person_2 = {"name": "Bob", "age": 35}
person_3 = {"name": "Calvin", "age": 40}
persons = [person_1, person_2, person_3]
for person in persons:
    print(person)

# A List in a Dictionary
flower = {
    "name": "rose",
    "colors": ["red", "yellow", "pink"]
}
print("Flower: " + flower["name"])
print("Colors: ")
for color in flower["colors"]:
    print(color)

myDictionary = {23: "hello",
                True: 45,
                4.5: False,
                "myData": [6, 6, 4, 3, 7, 8]
                }
print(myDictionary["myData"])

# A Dictionary in a Dictionary
students = {
    "max": {
        "name": "Kevin Max",
        "class": 4,
        "age": 6
    },
    "doe": {
        "name": "John Doe",
        "class": 5,
        "age": 7
    },
    "percy": {
        "name": "James Percy",
        "class": 6,
        "age": 8
    }
}

for name, student_info in students.items():
    print("Name: " + name)
    print("Class: " + str(student_info['class']))
    print("Age: " + str(student_info['age']))

# OR

person_1 = {"name": "Alfred", "age": 30}
person_2 = {"name": "Bob", "age": 35}
person_3 = {"name": "Calvin", "age": 40}
persons = {
    "p1": person_1,
    "p2": person_2,
    "p3": person_3
}
for p, person in persons.items():
    print(p)
    print(person["name"])
    print(person["age"])
