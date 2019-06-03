# Create a function called foreach which can take an iterable and an other function. Apply the function for all the elements in the iterable.
def multiply(a):
    return a * 2

def foreach(iterable, function):
    for i in iterable:
        function(i)

a = [1, 2, 3, 4, 5]

print(foreach(a, multiply))