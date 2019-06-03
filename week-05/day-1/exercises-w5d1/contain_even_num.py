# Given a list with the following items: 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Determine whether it contains even numbers or not using any().
numbers = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

even_numbers = list(map(lambda num: num % 2 == 0, numbers))

print(any(even_numbers))