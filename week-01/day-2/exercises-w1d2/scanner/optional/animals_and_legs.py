# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The second represents the number of pigs owned by the farmer
# It should print how many legs all the animals have

chickens = int(input("Please input the number of chickens: "))
pigs = int(input("Please input the number of pigs: "))

legs = chickens * 2 + pigs * 4

print(f"There are {legs} legs all the animals have")