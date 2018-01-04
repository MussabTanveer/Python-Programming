# variable
message = "Hello World!"
print(message)

# change value of variable
message = "Hello Python World!"
print(message)

# strings

# single or double quotes inside strings
message = 'I told my friend, "Python is my favorite language!"'
print(message)
message = "The language 'Python' is named after Monty Python, not the snake."
print(message)
message = "One of Python's strengths is its diverse community."
print(message)

# string change case methods
name = "JoHn DoE"
print(name.title())
print(name.capitalize())
print(name.upper())
print(name.lower())

# concatenating strings
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

# whitespace in strings
print(first_name + "\t" + last_name)
print("Person Name:\n" + full_name)
print("FLowers:\n\tRose\n\tLilly\n\tJasmine\n\tTulip")

# stripping whitespace
language = "python   "
print("I love " + language.rstrip() + " language!")
language = "   python"
print("I love " + language.lstrip() + " language!")
language = "   python   "
print("I love " + language.strip() + " language!")

# numbers

# integers
# add
print(2 + 3)
# subtract
print(3 - 2)
# multiply
print(2 * 3)
# divide
print(3 / 2)
# exponent
print(3 ** 2)
print(10 ** 6)
# DMAS rule
print(2 + 3 * 4)
# parenthesis
print((2 + 3) * 4)

# floats
# add
print(0.2 + 0.3)
# multiply
print(2 * 0.3)
# arbitrary decimal places
print(0.3 - 0.2)
print(0.2 + 0.1)

# use integers within strings
# str() function
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

# comments
# this is a single line comment
'''
this
is a
multi
line
comment
'''