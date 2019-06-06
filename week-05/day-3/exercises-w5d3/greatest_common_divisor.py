# Find the greatest common divisor of two numbers using recursion.

def gcd(n1, n2):
    if n1 > n2:
        if n1 % n2 == 0:
            return n2
        else:
            return gcd(n2, n1 % n2)
    else:
        if n2 % n1 == 0:
            return n1
        else:
            return gcd(n1, n2 % n1)

print(gcd(24, 54))