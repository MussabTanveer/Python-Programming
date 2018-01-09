# while Loops
# The while Loop in Action
count = 1
while count <= 5:
    print(count)
    count += 1

# Letting the User Choose When to Quit
msg = ""
while msg != "Q":
    msg = input("Enter anything to print back otherwise enter 'Q' to end program: ")
    if msg != "Q":
        print(msg)

# Using a Flag
active = True
while active:
    msg = input("Enter anything to print back otherwise enter 'Q' to end program: ")
    if msg == "Q":
        active = False
    else:
        print(msg)

# Using break to Exit a Loop
# use the break statement in any of Python’s loops to exit loop
while True:
    msg = input("Enter anything to print back otherwise enter 'Q' to end program: ")
    if msg == "Q":
        break
    else:
        print(msg)

# Using continue in a Loop
# use the continue statement to return to the beginning of the loop
# print odd numbers in range 1 to 10
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)

# Avoiding Infinite Loops
# This loop runs forever
# x = 1
# while x <= 5:
#     print(x)

# Using while Loop with Lists & Dictionaries
# Moving Items from One List to Another
menu = ["burger", "sandwich", "pizza", "macaroni"]
order = []
while menu:
    current_menu = menu.pop()
    print("Do you want to order " + current_menu.title() + "?")
    ans = input("Press 'Y' to order or 'N' to cancel this item: ")
    if ans == 'Y':
        order.append(current_menu.title())

print("Ordered food items are: ")
for o in order:
    print(o)

# Removing All Instances of Specific Values from a List
flowers = ["rose", "lilly", "tulip", "rose", "lilly", "rose"]
while "rose" in flowers:
    flowers.remove("rose")

print(flowers)

# Filling a Dictionary with User Input
fav_ice_cream = {}
while True:
    name = input("Enter your name: ")
    ice_cream = input("Enter your favorite ice cream: ")
    fav_ice_cream[name] = ice_cream
    ans = input("Add another record? (Y/N)")
    if ans == "N":
        break

print("Favorite ice creams of users:")
for n, i in fav_ice_cream.items():
    print(n + "'s favorite ice cream is " + i)
