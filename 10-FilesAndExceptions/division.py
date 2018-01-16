# Exceptions
# exceptions are handled with try-except blocks
# if don’t handle the exception, the program will halt and show a traceback

# Handling the ZeroDivisionError Exception

# print(5 / 0) ZeroDivisionError: division by zero

# Using try-except Blocks
# tell Python to try running some code, and you tell it what to do if the code results in a particular kind of exception

try:
    print(5 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# Using Exceptions to Prevent Crashes
# division calculator

print("\nEnter two numbers to divide")
print("(Press 'q' anytime to quit)")

while True:
    dividend = input("\nEnter dividend: ")
    if dividend == "q":
        break
    divisor = input("Enter divisor: ")
    if divisor == "q":
        break
    try:
        quotient = int(dividend) / int(divisor)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(quotient)
