# Write a program that stores 3 sides of a cuboid as variables (float)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000

length = int(input("Please input the length: "))
width = int(input("Please input the width: "))
height = int(input("Please input the height: "))

area = length * width + length * height + width * height
vol = length * width * height

print(f"The area is: {area}\nThe volume is: {vol}")