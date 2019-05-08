a = ["Apple", "Avocado", "Blueberries", "Durian", "Lychee"]
b = a.copy()
if "Durian" in a:
    print("Yes")
    b.remove("Durian")
else:
    print("No")
a.append("Kiwifruit")
if len(a) > len(b):
    print("List a is bigger")
elif len(a) < len(b):
    print("List b is bigger")
else:
    print("They have the same size")

if "Avocado" not in a:
    print("The item is not in the list")
else:
    print(a.index("Avocado"))

if "Durian" not in b:
    print("The item is not in the list")
else:
    print(b.index("Durian"))

c = ["Passion Fruit", "Pummelo"]
b.extend(c)
print(b)
print(a)
print(a[2])