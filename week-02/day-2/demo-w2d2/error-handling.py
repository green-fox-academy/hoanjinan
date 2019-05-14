drinks = ["cola", "water"]

try:
    index = int(input("Which item would you like to get?"))
    print(drinks[index])
except IndexError:
    print("Please provide a valid index.")
except ValueError:
    print("Please use the index instead of the name.")
finally:
    print("This will always run.")


print("Will it run?")

def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    raise TypeError

print(add("a", "b"))

try:
    print(add("a", "b"))
except TypeError:
    print("You must use integers.")


class MyError(Exception):
    def __init__(self):
        super().__init__()

raise MyError
