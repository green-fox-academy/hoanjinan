# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was
num = int(input("Please enter an integer number: "))
star = "*"
for i in range(0, num):
    print(star * (i + 1))