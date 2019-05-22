import csv

dic = {}
value_list = []
name_list = []
price_list = []
qty_list = []

f = open("/Users/hoanjinan_otoko/Desktop/epam-ds-training/greenfox/hoanjinan/week-03/day-3/exercises-w3d3/products.csv", "r")
content = csv.reader(f, delimiter = ";")

for i in content:
    # dic[f"{i[0]}"] = [i[1], i[2], i[3]]
    value_list.append(i)

for i in range(1, len(value_list)):
    name_list.append(value_list[i][1])
    price_list.append(value_list[i][2])
    qty_list.append(value_list[i][3])

for i in range(len(name_list)):
    dic[f"{name_list[i]}"] = [price_list[i], qty_list[i]]


# print(value_list)
# print(name_list)
# print(price_list)
# print(qty_list)
print(dic)
result = dic["display"]
print(result)