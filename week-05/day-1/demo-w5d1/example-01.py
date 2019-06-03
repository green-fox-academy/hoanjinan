
a = 0

def increment(amount):
    global a
    a = a + 1
    print(a)

def pure_increment(input, amount):
    return input + amount

from collections import namedtuple

Person = namedtuple("Person", "name age")

p1 = Person(name = "John", age = 10)

print(p1)

# Will ERROR
# p2 = Person(naem = "Bob", age = 24)
#p1.name = "Bob"

increment(1)
increment(1)

numbers = [1, 2, 3, 4, 5]

def bigger_than_3(n):
    # if n > 3:
    #     return True
    # else:
    #     return False
    # Better
    return n > 3

print(bigger_than_3(5))
big_numbers = filter(bigger_than_3, numbers)
# Same as def bigger_than_3(n)
bigger_than_3 = lambda n: n > 3
big_numbers = filter(lambda n: n > 3, numbers)
big_even_number = filter(lambda n: None, big_numbers)
numbers = []
print(numbers)

print(next(big_numbers))
print(next(big_numbers))
# ERROR
# print(next(big_numbers))

print(big_numbers)
# For loop Will be empty if print(list(big_numbers)) executed
print(list(big_numbers))
# for n in big_numbers:
#     print(n)

def numbers_return():
    return 1
    return 2
    return 3

print(numbers_return())

def numbers_gen():
    yield 1
    yield 2
    yield 3

g = numbers_gen()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))

def generator():
    i = 0
    while True:
        yield i
        i = i + 1

g2 = generator()

for _ in range(10):
    print(next(g2))