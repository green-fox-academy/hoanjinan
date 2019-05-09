import re

regular_ex = "^[0-9][0-9]?0?$"
m = re.compile(regular_ex)

num1 = "0"
num2 = "9"
num3 = "55"
num4 = "100"
num5 = "101"
num6 = "-4"

print(m.match(num1))
print(m.match(num2))
print(m.match(num3))
print(m.match(num4))
print(m.match(num5))
print(m.match(num6))