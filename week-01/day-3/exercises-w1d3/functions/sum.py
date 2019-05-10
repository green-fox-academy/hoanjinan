# Write a function called `sum` that returns the sum of numbers from zero to the given parameter

num = int(input("Please enter a integer number: "))

def sum(value):
    sum_num = 0
    for i in range(value + 1):
        sum_num += i
    return sum_num

print(sum(num))

