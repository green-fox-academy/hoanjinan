#functions 4
numbers = [1, 2, 3]
def addOne(arr):
    arr.append(4)
    print(f"Inside the function: {arr}")

addOne(numbers)
print(f"Outside of the function: {numbers}")


a = 10
def addTwo(number):
    number += 1
    print(f"Inside the function: {number}")

addTwo(a)
print(f"Outside the function: {a}")
#functions 4