import re

regular_ex = r"^([\w\.]+)@greenfox[\w]*?\.[\w]*$"
m = re.compile(regular_ex)

num1 = "john@greenfoxacademy.com"
num2 = "jane.doe@greenfoxacademy.com"
num3 = "jane@greenfox.academy"
num4 = "john@wick.com"
num5 = "jane@citromail.hu"
num6 = "janegreenfoxacademy.com"

print(m.match(num1).groups())
print(m.match(num2).groups())
print(m.match(num3).groups())
print(m.match(num4).groups())
print(m.match(num5).groups())
print(m.match(num6).groups())

#using if statement to check if the content is null
#if null, pass
#if sth, print