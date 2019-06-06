def my_first_recursive(n):
    if n == 0:
        print(n)
    else:
        print(n)
        my_first_recursive(n - 1)

my_first_recursive(5)

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)

def rec_print(arr):
    if len(arr) == 1:
        print(arr[0])
    else:
        print(arr[0])
        rec_print(arr[1:])

rec_print([5, 4, 3, 2, 1])