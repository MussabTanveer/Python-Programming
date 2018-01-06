# loop through an entire list
pets = ['cat', 'dog', 'chick', 'parrot', 'rabbit']
for pet in pets:
    print(pet)

# do more work within a for loop
for pet in pets:
    print(pet.title() + " is a friendly pet.")
    print("Everyone loves them!")

# do something after a for loop
print("That's all we have right now :)")

# Python uses indentation to determine when one line of code is connected to the line above it.
# The colon at the end of a for statement tells Python to interpret the next line as the start of a loop.

# making numerical lists

# using the range() function
# range(1,5) prints only the numbers 1 through 4 as a result of the off-by-one behavior
for value in range(1, 5):
    print(value)

# using range() to make a list of numbers using the list() function
numbers = list(range(1, 6))
print(numbers)

# to skip numbers in a given range
# list the even numbers between 1 and 10
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# list of the first 10 square numbers
# two asterisks (**) represent exponents
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

# simple statistics with a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
minimum = min(digits)
maximum = max(digits)
sum_digits = sum(digits)
print(minimum)
print(maximum)
print(sum_digits)

# List Comprehensions
cubes = [value**3 for value in range(1, 11)]
print(cubes)

# working with part of a list
players = ['messi', 'ronaldo', 'neymar', 'zlatan', 'ramos', 'xavi']
print(players[0:3])
print(players[2:5])
# omit first index means start at index 0
print(players[:4])
# omit second index means slice till end of a list
print(players[3:])
# slice last 3 items
print(players[-3:])

# loop through a slice
print("Top 3 players:")
for player in players[:3]:
    print(player.title())

# copy a list
my_sweets = ['chocolate', 'marshmallow', 'cake', 'ice cream']
# copy all my sweets to my friend's sweets list
friends_sweets = my_sweets[:]
my_sweets.append('custard')
friends_sweets.append('pudding')
print("These are my favorite sweets:")
print(my_sweets)
print("These are my friend's favorite sweets:")
print(friends_sweets)

# the statement below is wrong as both variables point to the same list
friends_sweets = my_sweets

# tuples
# tuples allow to create list of items that cannot change

# define a tuple
# use parentheses instead of square brackets
coordinates = (5, 9)
# access elements of tuple
print(coordinates[0])
print(coordinates[1])

# coordinates[0] = 7 not allowed

# loop through all values in a tuple
print("Original Coordinates:")
for coordinate in coordinates:
    print(coordinate)

# write over a tuple
# redefine the entire tuple
coordinates = (30, 45)
print("Modified Coordinates:")
for coordinate in coordinates:
    print(coordinate)
