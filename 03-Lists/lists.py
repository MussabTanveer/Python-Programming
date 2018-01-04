# create a list
cities = ['San Francisco', 'California', 'Boston', 'New York', 'Miami', 'Chicago']
print(cities)

# access elements in a list
print(cities[0])
print(cities[4].upper())

# access the last element in a list
print(cities[-1])

# access the third last element in a list
print(cities[-3])

# use individual values from list
message = "I live in " + cities[1] + " city."
print(message)

# modify list element
cities[2] = "Mexico"
print(cities)

# add elements to list
# append elements at the end of a list
# append(list_item)
cities.append("San Diego")
print(cities)

# empty list
flowers = []
flowers.append('Rose')
flowers.append('Tulip')
flowers.append('Jasmine')
print(flowers)

# insert elements into a list at any position
# insert(index, list_item)
cities.insert(0, 'Houston')
print(cities)

# remove elements from a list
# remove item using del statement
del cities[5] # del Miami
print(cities)

# remove item using pop() method
popped_city = cities.pop()
print(cities)
print(popped_city)

gpa = [3.71, 3.83, 3.57, 3.95]
print("My last semester GPA was " + str(gpa.pop()))

# pop items from any position in a list
print("My second semester GPA was " + str(gpa.pop(1)))

# remove an item by value
# remove() method deletes only the first occurrence of the value
not_my_city = 'California'
print(cities)
cities.remove(not_my_city)
print(cities)
print("I no longer live in " + not_my_city + " city")

# organize a list
# sort a list permanently with the sort() method
fruits = ['orange', 'banana', 'apple', 'kiwi', 'pineapple', 'mango']
fruits.sort()
print(fruits)

# reverse sort list
fruits.sort(reverse=True)
print(fruits)

# sort a list temporarily with the sorted() function
colors = ['red', 'blue', 'green', 'yellow', 'black', 'white']
print("Here's the original list:")
print(colors)
print("Here's the sorted list:")
print(sorted(colors))
print("Here's the original list again:")
print(colors)

# print a list in reverse order
# reverse() does not sort backward alphabetically; it simply reverses the order of the list
# revert to the original order anytime by applying reverse() again
print("Here's the original list:")
print(colors)
print("Here's the reversed list:")
colors.reverse()
print(colors)

# find the length of a list using len() function
# index is 0-based; length is 1-based
print(len(colors))
