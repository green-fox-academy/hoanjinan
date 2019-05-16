# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4

set_times = int(input("Please set how many numbers you want to enter: "))

sum = 0
count = 0
for i in range(set_times):
    num = int(input("Please input an integer number: "))
    sum += num
    count += 1
avg = sum / count
print(f"The average is {avg}")
