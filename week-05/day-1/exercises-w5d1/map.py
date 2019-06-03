def multiply(a):
    return a * 2

def new_map(iterable, function):
    for i in iterable:
        yield function(i)

a = [1, 2, 3, 4, 5]
map_result = new_map(a, multiply)

print(list(map_result))