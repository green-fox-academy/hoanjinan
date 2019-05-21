def add(a, b):
    return a + b

def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
    #Alternative way of doing that.  may work better if too much numbers.
    # numbers = [a, b, c]
    # holder = numbers[0]
    # for i in range(len(numbers)):
    #     if numbers[i] > holder:
    #         holder = numbers[i]
    # return holder

def median(pool):
    pool.sort()
    if len(pool) % 2 == 0:
        return (pool[int(len(pool) / 2) - 1] + pool[int(len(pool) / 2)]) / 2
    else:
        return pool[int((len(pool) - 1) / 2)]

def is_vovel(char):
    return char in ['a', 'u', 'o', 'e', 'i']

def translate(hungarian):
    teve = hungarian
    for char in teve:
        if is_vovel(char):
            teve = (char+'v'+char).join(teve.split(char))
    return teve
