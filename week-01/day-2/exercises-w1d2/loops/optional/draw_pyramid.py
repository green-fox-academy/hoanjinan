# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was

num = int(input("Please input an integer number: "))

for i in range(1, num + 1):
    print(" " * (num - i) + "*" * i + "*" * (i - 1))