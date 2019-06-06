# Given a non-negative integer n, return the sum of its digits recursively (without loops).

def sum_digit(n):
    if n / 10 < 1:
        print(n)
        return n
    else:
        print(n)
        return n % 10 + sum_digit(int(n / 10))

print(sum_digit(1267))