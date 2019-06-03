# Given a list with the following items: 1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14
# Calculate the sum of the even numbers which are below or equal to 10.
from functools import reduce

numbers = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

sum_num = reduce(lambda a, b: a + b, filter(lambda num: num % 2 == 0 and num <= 10, numbers))

print(sum_num)