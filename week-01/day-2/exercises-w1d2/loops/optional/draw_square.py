# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%%
# %    %
# %    %
# %    %
# %    %
# %%%%%%
#
# The square should have as many lines as the number was

num = int(input("Please input an integer number: "))

for i in range(1, num + 1):
    if i == 1 or i == num:
        print("%" * num)
    else:
        print("%" + " " * (num - 2) + "%")