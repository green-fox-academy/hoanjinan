import json

f = open("/Users/hoanjinan_otoko/Desktop/epam-ds-training/greenfox/hoanjinan/week-03/day-4/exercises-w3d4/films.json", mode = "r", encoding = "utf-8")
content = json.load(f)
content_dic = {}
count = 1
for i in content:
    content_dic[count] = {"id": i["id"], "title": i["title"], "year": i["year"], "genre": i["genre"], "description": i["description"]}
    count += 1

print(content_dic)