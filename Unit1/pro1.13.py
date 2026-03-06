'''Write a program to make use of map(), filter() and reduce() functions with context to lambda functions.'''
from functools import reduce

# Sample list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1. map() with lambda → square each number
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

# 2. filter() with lambda → keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# 3. reduce() with lambda → sum of all numbers
total = reduce(lambda a, b: a + b, numbers)
print("Sum of all numbers:", total)
