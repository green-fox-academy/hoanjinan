#functions 2
def add(a, b):
    print(a + b)

def add2(a, b):
    return a + b

add(1, 2)
result = add2(1, 2)
print(add2(1, 2))
print(result)

def future():
    pass

for i in range(5):
    pass

def returnNorthing():
    return None
    return 1 #will not execute under the first return

def getHeight(name):
    if (name == "Zilan"):
        return 1.75
    elif (name == "Bob"):
        return 1.70
#if not zilan or bob, it will return none
#functions 2