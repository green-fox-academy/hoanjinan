#dictionary
a = {}
phone_numbers = { "Zilan" : "+8612345678901", "Steven" : "+448937589361"}
print(phone_numbers)
print(phone_numbers["Zilan"])

if "Steven" in phone_numbers:
    print(phone_numbers["Steven"])

print("Steven" in phone_numbers)
print(phone_numbers["Steven"])

print(dir(phone_numbers))
#print(help(phone_numbers.fromkeys))

for key in phone_numbers:
    print(key)
    print(phone_numbers[key])
    print(f"{key}'s phone number is: {phone_numbers[key]}")

for key, num in phone_numbers.items():
    print(key, num)
#dictionary