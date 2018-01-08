# example
cars = ['audi', 'bmw', 'bugatti', 'bentley', 'acura']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# conditional tests
# checking for equality
fruit = 'apple'
print(fruit == 'apple')
fruit = 'banana'
print(fruit == 'apple')

# testing case sensitive
flower = 'Rose'
print(flower == 'rose')

# solution is to use case method
print(flower.lower() == 'rose')

# checking for inequality
requested_icecream = 'chocolate'
if requested_icecream != 'vanilla':
    print("Hold the vanilla ice-cream!")

# numerical comparisons
age = 16
print(age == 18)
print(age != 18)
print(age < 18)
print(age <= 18)
print(age > 18)
print(age >= 18)

# checking multiple conditions
# use and to check multiple conditions
age1 = 22
age2 = 17
print(age1 >= 18 and age2 >= 18)
age2 = 21
print(age1 >= 18 and age2 >= 18)

# use or to check multiple conditions
age1 = 22
age2 = 17
print(age1 >= 18 or age2 >= 18)
age1 = 16
print(age1 >= 18 or age2 >= 18)

# check whether a value is in a list
# use the keyword in
desserts = ['custard', 'cake', 'pudding', 'ice cream']
print('cake' in desserts)
print('doughnut' in desserts)

# check whether a value is not in a list
# use the keyword not in
passwords = ['dragon', 'shadow', 'sunshine', 'starwars']
password_entered = 'freedom'
if password_entered not in passwords:
    print("Incorrect Password!")

# boolean expressions
item_found = True
item_found = False

# if statements
# Simple if Statements
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# if-else Statements
test = "Pass"
if test == "Fail":
    print("You've failed the test")
else:
    print("You've passed the test")

# The if-elif-else Chain
age = 12
if age < 4:
    ticket_cost = 0
elif age < 18:
    ticket_cost = 5
else:
    ticket_cost = 10
print("Your ticket cost is $" + str(ticket_cost))

# Using Multiple elif Blocks
age = 12
if age < 4:
    ticket_cost = 0
elif age < 18:
    ticket_cost = 5
elif age < 35:
    ticket_cost = 10
else:
    ticket_cost = 15
print("Your ticket cost is $" + str(ticket_cost))

# Omitting the else Block
age = 40
if age < 4:
    ticket_cost = 0
elif age < 18:
    ticket_cost = 5
elif age >= 18:
    ticket_cost = 10
print("Your ticket cost is $" + str(ticket_cost))

# Testing Multiple Conditions
order = ["pizza", "burger", "soft drink"]
if "sandwich" in order:
    print("Ordering sandwich")
if "burger" in order:
    print("Ordering burger")
if "soft drink" in order:
    print("Ordering soft drink")
print("Finished ordering")

# Using if Statements with Lists
# Checking for Special Items
requested_flowers = ["rose", "tulip", "jasmine"]
for requested_flower in requested_flowers:
    if requested_flower == "tulip":
        print("Sorry, we don't have tulips!")
    else:
        print(requested_flower.title() + " added to bouquet")

# Checking That a List Is Not Empty
requested_flowers = []
if requested_flowers:
    for requested_flower in requested_flowers:
        print(requested_flower.title() + " added to bouquet")
    print("Finished making bouquet!")
else:
    print("Please choose some flowers")

# Using Multiple Lists
available_flowers = ["rose", "sunflower", "jasmine", "lilly"]
requested_flowers = ["rose", "tulip", "jasmine"]
for requested_flower in requested_flowers:
    if requested_flower in available_flowers:
        print(requested_flower.title() + " added to bouquet")
    else:
        print("Sorry, we don't have " + requested_flower.title())
print("Finished making bouquet!")

# Styling your if Statements
# PEP 8: use a single space around comparison operators
if age < 4:
    print("You're too young!")
if age<4:
    print("You're too young!")
