product_data = {"Eggs": 200,
                "Milk": 200,
                "Fish": 400,
                "Apples": 150,
                "Bread": 50,
                "Chicken": 550}

def lessThan(data, price):
    for key in data:
        if data[key] < price :
            print(f"{key} is less than {price}.")

def moreThan(data, price):
    for key in data:
        if data[key] > price :
            print(f"{key} is less than {price} and the price of {key} is {data[key]}.")

lessThan(product_data, 201)
moreThan(product_data, 150)