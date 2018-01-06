# S = {x² : x in {0 ... 9}}
S = [value**2 for value in range(0, 10)]
print(S)

# V = (1, 2, 4, 8, ..., 2¹²)
V = [2**power for power in range(0, 13)]
print(V)

# M = {x | x in S and x even}
M = [value for value in S if value % 2 == 0]
print(M)

# convert Celsius values into Fahrenheit
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [(9/5)*c+32 for c in Celsius]
print(Fahrenheit)

# list comprehension to create Pythagorean triples
pythagorean_triples = [(x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y, 30) if x**2 + y**2 == z**2]
print(pythagorean_triples)

# cross product or Cartesian product
colours = ["red", "green", "yellow", "blue"]
things = ["house", "car", "tree"]
coloured_things = [(x, y) for x in colours for y in things]
print(coloured_things)

# covert this to list comprehension
# new_things = []
# for ITEM in old_things:
#     if condition_based_on(ITEM):
#         new_things.append("something with " + ITEM)
# answer
# new_things = ["something with " + ITEM for ITEM in old_things if condition_based_on(ITEM)]

numbers = [1, 2, 3, 4, 5]

# doubled_odds = []
# for n in numbers:
#     if n % 2 == 1:
#         doubled_odds.append(n * 2)

doubled_odds = [n*2 for n in numbers if n % 2 == 1]
print(doubled_odds)


import math

# simplest primality test is trial division: Given an input number n,
# check whether any prime integer m from 2 to √n evenly divides n (the division leaves no remainder)
# if n is divisible by any m then n is composite, otherwise it is prime.
# using basic loops and conditions
num = int(input("Enter any number to find if it is a prime number: "))
flag = True
for i in range(2, int(math.sqrt(num))+1):
    if num % i == 0:
        flag = False
        break
if flag:
    print(str(num) + " is prime")
else:
    print(str(num) + " is composite")

# using list comprehension
# compute prime numbers from 2 to 20
# Use all to check all elements (from 2 upto √i) met conditions
primes = [i for i in range(2, 21) if all(i % j != 0 for j in range(2, int(math.sqrt(i))+1))]
print(primes)


# strings
string = "The quick brown fox jumps over the lazy dog."
words = string.split()
print(words)
word_upper_lower_len = [[w.upper(), w.lower(), len(w)] for w in words]  # lists in list
print(word_upper_lower_len)

# Dictionary comprehension
# flipped = {value: key for key, value in original.items()}
