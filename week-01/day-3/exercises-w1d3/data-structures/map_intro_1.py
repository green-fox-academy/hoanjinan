key_value = {}

if len(key_value) == 0:
    print("The map is empty")
else:
    print("The map contains sth")

key_value.update({97: "a", 98: "b", 99: "c", 65: "A", 66: "B", 67: "C"})

print(len(key_value))
if len(key_value) == 0:
    print("The map is empty")
else:
    print("The map contains sth")

for key in key_value:
    print(key)

for i in key_value:
    value = key_value[i]
    print(value)

key_value.update({68: "D"})
print(len(key_value))
print(key_value.get(99))
key_value.pop(97)

for key, value in key_value.items():
    print(key, value)

if 100 in key_value:
    print("Yes")
else:
    print("No")

key_value = {}
print(len(key_value))