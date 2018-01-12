# Defining a Function


def greet():
    print("Hello!")

greet()

# Passing Information to a Function


def greet(username):
    print("Hello!" + username)

greet("Sam")
greet("Sarah")

# Arguments and Parameters
# The variable username in the definition of greet_user() is an example of a parameter
# The value 'Sam' in greet_user('Sam') is an example of an argument

# Passing arguments

# Positional Arguments
# match each argument in the function call with a parameter in the function definition
# Values matched up this way are called positional arguments


def describe_pet(animal_type, pet_name):
    print("I've a " + animal_type + ".")
    print("It's name is " + pet_name.title())

describe_pet("fish", "dory")

# Multiple Function Calls
describe_pet("dog", "willie")

# Order Matters in Positional arguments
describe_pet("missy", "cat")

# Keyword Arguments
# A keyword argument is a name-value pair that you pass to a function
# When you use keyword arguments, be sure to use the exact names of the parameters in the function’s definition


def describe_pet(animal_type, pet_name):
    print("I've a " + animal_type + ".")
    print("It's name is " + pet_name.title())

describe_pet(animal_type="fish", pet_name="dory")
describe_pet(pet_name="dory", animal_type="fish")
describe_pet("fish", "dory")

# Default Values
""" When you use default values, any parameter with a default value needs to be listed after all the parameters
that don’t have default values. This allows Python to continue interpreting positional arguments correctly"""


def describe_pet(pet_name, animal_type="dog"):
    print("I've a " + animal_type + ".")
    print("It's name is " + pet_name.title())

# Equivalent Function Calls
describe_pet(pet_name="willie")  # OR
describe_pet("willie")  # OR

describe_pet("dory", "fish")  # OR
describe_pet(pet_name="dory", animal_type="fish")  # OR
describe_pet(animal_type="fish", pet_name="dory")  # OR

# Avoiding Argument Errors


def describe_pet(pet_name, animal_type):
    print("I've a " + animal_type + ".")
    print("It's name is " + pet_name.title())

# describe_pet()  # missing 2 required positional arguments: 'pet_name' and 'animal_type'

# Return Values

# Returning a Simple Value


def get_city_country(city, country):
    city_country = city.title() + " is in " + country.title()
    return city_country

place = get_city_country("paris", "france")
print(place)

# Making an Argument Optional


def get_city_country(city, country, population=""):
    if population:
        city_country = city.title() + " is in " + country.title() + " and its population is " + population
        return city_country
    else:
        city_country = city.title() + " is in " + country.title()
        return city_country

place = get_city_country("paris", "france", "2.3 million")
print(place)

place = get_city_country("bangkok", "thailand")
print(place)

# Returning a Dictionary


def build_place(city_name, country_name):
    fav_place = {"city": city_name, "country": country_name}
    return fav_place

place = build_place("paris", "france")
print(place)


def build_place(city_name, country_name, population=""):
    fav_place = {"city": city_name, "country": country_name}
    if population:
        fav_place["population"] = population
    return fav_place

place = build_place("bangkok", "thailand", "8.6 million")
print(place)
place = build_place("london", "united kingdom")
print(place)

# Using a Function with a while Loop


def get_name(first_name, last_name):
    name = first_name.title() + " " + last_name.title()
    return name

while True:
    print("\nPlease tell us your name!")
    print("(enter 'q' anytime to quit)")
    first = input("Enter first name: ")
    if first == "q":
        break
    last = input("Enter last name: ")
    if last == "q":
        break
    full_name = get_name(first, last)
    print("Hello, " + full_name + "!")


# Passing a list


def greet_user(names):
    for name in names:
        print("Hello, " + name.title())

user_names = ["john", "max", "albert", "william"]

greet_user(user_names)

# Modifying a List in a Function
# any changes made to the list inside the function’s body are permanent


def prepare_order(order_food, order_finish):
    while order_food:
        food = order_food.pop()
        print("Preparing food: " + food)
        order_finish.append(food)


def show_order(order_finish):
    print("Your order is ready having following food items:")
    for food in order_finish:
        print(food)

order = ["pizza", "burger", "sandwich", "chow mein", "shashlik"]
ready_food_items = []

prepare_order(order, ready_food_items)
show_order(ready_food_items)
print(order)  # empty list

# Preventing a Function from Modifying a List
# pass the function a copy of the list, not the original

order = ["pizza", "burger", "sandwich", "chow mein", "shashlik"]
ready_food_items = []

prepare_order(order[:], ready_food_items)  # slice notation [:] makes a copy of the list
show_order(ready_food_items)
print(order)  # non empty

# Passing an arbitrary number of arguments
# Python allows a function to collect an arbitrary number of arguments from the calling statement


def make_bouquet(*flowers):  # asterisk in the parameter name tells Python to make an empty tuple
    print(flowers)
    for flower in flowers:
        print("- " + flower)

make_bouquet("rose")
make_bouquet("rose", "tulip", "jasmine")

# Mixing Positional and Arbitrary Arguments
# the parameter that accepts an arbitrary number of arguments must be placed last in the function definition
# Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter


def make_bouquet(size, *flowers):  # asterisk in the parameter name tells Python to make an empty tuple
    print("Making a " + size + " bouquet with following flowers:")
    for flower in flowers:
        print("- " + flower)

make_bouquet("small", "rose")
make_bouquet("large", "rose", "tulip", "jasmine")

# Using Arbitrary Keyword Arguments


def build_patient_profile(first, last, **patient_info):
    profile = {}
    profile["first name"] = first
    profile["last name"] = last
    for key, value in patient_info.items():
        profile[key] = value
    return profile

patient_profile = build_patient_profile("Harry", "James")
print(patient_profile)
patient_profile = build_patient_profile("Max", "William", age=3, test="MRI")
print(patient_profile)

# Storing your Functions in Modules
# storing your functions in a separate file called a module and then importing that module into your main program
# An import statement tells Python to make the code in a module available in the currently running program file

# Styling Functions

"""
descriptive names
use lowercase letters and underscores
comment immediately after the function definition that explains concisely what the function does, use docstring format
no spaces should be used on either side of the equal sign to specify default value for a parameter
same convention should be used for keyword arguments
more than one function in a module, separate each by two blank lines
"""
