#functions 1
def hello():
    print(f"Hello!")

print(hello)
hello()
print(hello())


def greet(name):
    print(f"Nice to meet you!  {name}")

print(greet)

firstname = "Zilan"
greet(firstname)

greet("John")


def calculate(operation = "sum", comment = "No comment", *args, **kwargs):
    print(operation)
    print(comment)
    print(args)
    print(kwargs)

calculate("sum", 1, 2, 3, 4)
calculate("divide")
calculate(comment = "This is a comment.", name = "Zilan")
#functions 1