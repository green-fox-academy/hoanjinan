# Create a program that asks for two numbers
# If the second number is not bigger than the first one it should print:
# "The second number should be bigger"
#
# If it is bigger it should count from the first number to the second by one
# 
# example:
#
# first number: 3, second number: 6, should print:
#
# 3
# 4
# 5
first_num = int(input("Please enter the first number: "))
second_num = int(input("Please enter the second number: "))

if first_num < second_num:
    for i in range(first_num, second_num):
        print(i)
else:
    print("The second number should be bigger")