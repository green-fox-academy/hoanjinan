# Given a list with the following items: 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Create a new list which contains only the even numbers.

numbers = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

even_numbers = filter(lambda even: even % 2 == 0, numbers)

print(list(even_numbers))