from flask import Flask, request, render_template
import os, csv

app = Flask(__name__)

@app.route("/exercise/")
def exercise():
    return render_template("exercise-05.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/film/<filmname>")
def film(filmname):
    return render_template(f"{filmname}")

@app.route("/read/")
def read():
    title = os.path.splitext("hp1.txt")[0]
    f = open("hp1.txt", "r")
    heading = f.readline()
    content = f.readlines()
    f.close()
    return render_template("film.html", title = title, heading = heading, content = content[0])

@app.route("/query/")
def query():
    dic = {}
    value_list = []
    name_list = []
    price_list = []
    qty_list = []

    f = open("/Users/hoanjinan_otoko/Desktop/epam-ds-training/greenfox/hoanjinan/week-03/day-3/exercises-w3d3/products.csv", "r")
    content = csv.reader(f, delimiter = ";")

    for i in content:
        value_list.append(i)

    for i in range(1, len(value_list)):
        name_list.append(value_list[i][1])
        price_list.append(value_list[i][2])
        qty_list.append(value_list[i][3])

    for i in range(len(name_list)):
        dic[f"{name_list[i]}"] = [price_list[i], qty_list[i]]
    
    item_name = request.args.get('item')
    # fail = "The item is not in the list."

    if item_name not in dic:
        return render_template("query.html")
    else:
        result = dic[item_name]
        return render_template("query.html", price = f"The price is: {result[0]}", qty = f"The quantity is: {result[1]}")

if __name__ == "__main__":
    app.run()