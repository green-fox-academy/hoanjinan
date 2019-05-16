# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was

num = int(input("Please input an integer number: "))

for i in range(1, num + 1):
    if i < (num + 2) / 2:
        print(" " * (num - i) + "*" * i + "*" * (i - 1))
        # print(i)
    else:
        print(" " * (i - 1) + "*" * (num + 1 - i) + "*" * (num - i))
        # print(i)