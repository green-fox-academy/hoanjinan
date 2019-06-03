# Given a list with the following items: 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Create a new list which contains the numbers if their squared value is above 20.

numbers = 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14

above_20 = filter(lambda num: num ** 2 > 20, numbers)

print(list(above_20))