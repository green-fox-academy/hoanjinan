product_price = {
    "Milk": 1.07,
    "Rice": 1.59,
    "Eggs": 3.14,
    "Cheese": 12.60,
    "Chicken Breasts": 9.40,
    "Apples": 2.31,
    "Tomato": 2.58,
    "Potato": 1.75,
    "Onion": 1.10,
}

bob_list = {
    "Milk": 3,
    "Rice": 2,
    "Eggs": 2,
    "Cheese": 1,
    "Chicken Breasts": 4,
    "Apples": 1,
    "Tomato": 2,
    "Potato": 1,
}

alice_list = {
    "Rice": 1,
    "Eggs": 5,
    "Chicken Breasts": 2,
    "Apples": 1,
    "Tomato": 10,
}

# sum_bob = 0
# for key in product_price:
#     if key in bob_list:
#         print(f"{product_price[key]} and {bob_list[key]}")
#         sum_bob += product_price[key] * bob_list[key]


#for x, y in product_price:
#    pass

#set(product_price) & set(bob_list)

def sum_pay(product_price, shop_list):
    sum_total = 0
    for key in product_price:
        if key in shop_list:
            print(f"{product_price[key]} and {shop_list[key]}")
            sum_total += product_price[key] * shop_list[key]
    return sum_total

sum_bob = sum_pay(product_price, bob_list)
print(f"Bob pays: {sum_bob}")

sum_alice = sum_pay(product_price, alice_list)
print(f"Bob pays: {sum_alice}")

def compare(bob_list, alice_list, key):
    if key in bob_list and key in alice_list:
        if bob_list[key] > alice_list[key]:
            print(f"Bob buys more {key}")
        else:
            print(f"Alice buys more {key}")
    else:
        print("The input value is not in the list")

compare(bob_list, alice_list, "Rice")
compare(bob_list, alice_list, "Potato")


if len(bob_list) > len(alice_list):
    print("Bob buys more different products.")
else:
    print("Alice buys more different products.")

pieces_bob = 0
pieces_alice = 0
for key in bob_list:
    pieces_bob += bob_list[key]

for key in alice_list:
    pieces_alice += alice_list[key]

if pieces_bob > pieces_alice:
    print("Bob buys more products!")
else:
    print("Alice buys more products!")