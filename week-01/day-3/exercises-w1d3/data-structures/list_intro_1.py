name = []
print(len(name))
name.append("William")

if len(name) == 0:
    print("The list is empty")
else:
    print("The list contains sth")

name.append("John")
name.append("Amanda")
print(len(name))

print(name[2])

for i in range(len(name)):
    print(name[i])

for i in range(len(name)):
    print(str(i + 1) + ". " + name[i])

name.pop(1)

name.reverse()
for i in range(len(name)):
    print(name[i])

name = []

if len(name) == 0:
    print("The list is empty")
else:
    print("The list contains sth")