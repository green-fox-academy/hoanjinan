key_value = {"978-1-60309-452-8": "A Letter to Jo", 
             "978-1-60309-459-7": "Lupus",
             "978-1-60309-444-3": "Red Panda and Moon Bear",
             "978-1-60309-461-0": "The Lab"}

for key, value in key_value.items():
    print(f"{value} (ISBN: {key})")

key_value.pop("978-1-60309-444-3")

for key, value in key_value.items():
    print(f"{value} (ISBN: {key})")

for key, value in key_value.items():
    if value == "The Lab":
        reserved_key = key
        break
key_value.pop(reserved_key)

for key, value in key_value.items():
    print(f"{value} (ISBN: {key})")

key_value.update({"978-1-60309-450-4": "They Called Us Enemy",
                  "978-1-60309-453-5": "Why Did We Trust Him?"})
print(key_value)

print("478-0-61159-424-8" in key_value)