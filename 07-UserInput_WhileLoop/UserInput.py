# input() Function
# How input() Function Works
msg = input("Write anything: ")
print(msg)

# Writing Clear Prompts
name = input("Enter your name: ")
print("Hello, " + name + "!")

prompt = "We're conducting a poll"
prompt += "\nPlease tell us your name: "
name = input(prompt)
print("Hello, " + name + ". Please answer the poll questions.")

# Using int() to Accept Numerical Input
age = input("Enter your age: ")  # return string
age = int(age)  # return number
if age >= 18:
    print("Welcome!")
else:
    print("Stay away!")

# The Modulo Operator
# divides one number by another number and returns the remainder
print(5 % 3)
print(15 % 16)
print(26 % 13)
num = int(input("Please enter a number: "))
if num % 2 == 0:
    print("You entered an even number")
else:
    print("You entered an odd number")
