shopping_list = ["eggs", "milk", "fish", "apples", "bread", "chicken"]

def searchList(item_list, item):
        if item in item_list:
            return f"Yes!  You have {item} on your list!"
        else:
            return f"No, You don't have {item} on your list."

print(searchList(shopping_list, "milk"))
print(searchList(shopping_list, "bannanas"))