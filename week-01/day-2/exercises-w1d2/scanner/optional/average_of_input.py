# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4

a, b, c, d, e = input("Please enter 5 integer values: ").split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
avg = (a + b + c + d + e) / 5

print(f"The average is: {avg}")