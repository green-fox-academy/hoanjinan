import json

f = open("/Users/hoanjinan_otoko/Desktop/epam-ds-training/greenfox/hoanjinan/week-03/day-4/exercises-w3d4/films.json", mode = "r", encoding = "utf-8")
content = json.load(f)
f.close()
print(content[1]["id"])