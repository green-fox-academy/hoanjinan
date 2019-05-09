import re

regular_ex = r"^((\+36)|(00\s36))\s[0-9]{2}\s[0-9]{3}\s[0-9]{4}$"
m = re.compile(regular_ex)

num1 = "+36 20 473 2746"
num2 = "+36 30 217 4912"
num3 = "00 36 70 381 1288"
num4 = "00 36 31 471 2818"
num5 = "+36 20 3173 4717"
num6 = "+36 102 237 1121"
num7 = "+49 20 483 1273"
num8 = "36 70 381 2183"

print(m.match(num1))
print(m.match(num2))
print(m.match(num3))
print(m.match(num4))
print(m.match(num5))
print(m.match(num6))
print(m.match(num7))
print(m.match(num8))