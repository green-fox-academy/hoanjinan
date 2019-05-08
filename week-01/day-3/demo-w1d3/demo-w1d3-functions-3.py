#functions 3
a = 1
def printOut():
    print(a)

printOut()

def printOut2():
    a = 2
    print(a)

printOut2()
print(a)

b = 100
#def printOut3():
#    b += 1
#    print(b)

def printOut3():
    global b
    b += 1
    print(b)

printOut3()
print(f"B's value after method call: {b}")

#not a good practice
name = "John"
def greet():
    print(f"Hello {name}")

#functions 3