# Write a program that reads a number from the standard input,
# Then prints "Odd" if the number is odd, or "Even" if it is even.
num = int(input("Please enter an integer number: "))
if num % 2 is 0:
    print("This is an even number.")
else:
    print("This is an odd number.")