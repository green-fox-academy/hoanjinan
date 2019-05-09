import re

regular_ex = '.+src=\"(.+.png).+'
m = re.compile(regular_ex)

num1 = '<img src="dog.png">'
num2 = '<img alt="Cat picture" src="./images/cat-01.png">'
num3 = '<script src="jquery.js"></script>'

print(m.match(num1).group(1))
print(m.match(num2).group(1))
print(m.match(num3))