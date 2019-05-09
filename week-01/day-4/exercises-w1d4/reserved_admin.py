import re

regular_ex = "[Aa]dmin"
m = re.compile(regular_ex)
upper = "Admin"
lower = "admin"

print(m.match(upper))
print(m.match(lower))