import re

regular_ex = r"^([^\+36]{3}|[^0036]{4})[\d]+$"
m = re.compile(regular_ex)

num1 = "+3636204732746"
num2 = "0036703811288"
num3 = "+85288765309"
num4 = "0085283674091"
num5 = "+278463903648578"
num6 = "00264850483764950"

print(m.match(num1))
print(m.match(num2))
print(m.match(num3))
print(m.match(num4))
print(m.match(num5))
print(m.match(num6))