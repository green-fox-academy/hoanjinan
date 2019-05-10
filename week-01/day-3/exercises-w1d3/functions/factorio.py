# - Create a function called `factorio`
#   that returns it's input's factorial

num = int(input("Please enter a integer number: "))

def factorio(value):
    fact = 1
    # print(fact)
    for i in range(value):
        fact *= i + 1
        # print(i)
        # print(fact)
    return fact

print(factorio(num))