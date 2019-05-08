product_data = {"Eggs": 200,
                "Milk": 200,
                "Fish": 400,
                "Apples": 150,
                "Bread": 50,
                "Chicken": 550}

def price(data, name):
    return data[name]

def highest_price(data):
    reserved_key = ""
    reserved_value = 0
    for key, value in data.items():
        if reserved_value < value:
            reserved_value = value
            reserved_key = key
    return reserved_key

def average(data):
    sum = 0
    for key in data:
        sum += data[key]
    return round(sum / len(product_data), 2)

def counter(data, price):
    count = 0
    for key in data:
        if data[key] < 300:
            count += 1
    return count

def exactly(data, price):
    count = len(data) - 1
    for key in data:
        if price == data[key]:
            return f"Yes!  You can buy {key} by using exactly {price}!"
        elif count == 0:
            return f"Sorry, you can buy northing using exactly {price}."
        count -= 1

def cheapest(data):
    reserved_key = next(iter(data.keys()))
    reserved_value = next(iter(data.values()))
    for key, value in data.items():
        if reserved_value > value:
            reserved_value = value
            reserved_key = key
    return reserved_key

print(price(product_data, "Fish"))
print(highest_price(product_data))
print(average(product_data))
print(counter(product_data, 300))
print(exactly(product_data, 125))
print(cheapest(product_data))
