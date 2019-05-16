# Write a program that asks for two numbers and prints the bigger one

num1 = int(input("Please input the first number: "))
num2 = int(input("Please input the second number: "))

if num1 > num2:
    print(f"{num1} is bigger!")
else:
    print(f"{num2} is bigger!")