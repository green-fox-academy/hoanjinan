list_money = [500, 1000, 1250, 175, 800, 120]

def sum(money):
    sum = 0
    for i in range(len(money)):
        sum += money[i]
    return sum

def greatest(money):
    reserved_money = 0
    for i in range(len(money)):
        current_val = money[i]
        if reserved_money < current_val:
            reserved_money = current_val
    return reserved_money

def cheapest(money):
    reserved_money = money[0]
    for i in range(len(money)):
        current_val = money[i]
        if reserved_money > current_val:
            reserved_money = current_val
    return reserved_money

def average(money):
    avg = sum(money) / len(money)
    return round(avg, 2)

print(sum(list_money))
print(greatest(list_money))
print(cheapest(list_money))
print(average(list_money))
