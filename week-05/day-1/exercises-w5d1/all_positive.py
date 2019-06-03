# Given a list with the following items: 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Determine whether every number is positive or not using all().

numbers = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

positive = list(filter(lambda num: num > 0, numbers))

print(all(positive))