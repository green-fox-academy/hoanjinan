oliver = set(["Laptop", "Notebook", "Pen", "Sunglasses", "Hand sanitizer"])
ethan = set(["Sunglasses", "Notebook", "Phone"])
mia = set(["Laptop", "Sunglasses", "Hand sanitizer"])

print(oliver.intersection(ethan))
print(oliver.difference(mia)) #oliver - mia
print(oliver.intersection(ethan.intersection(mia)))