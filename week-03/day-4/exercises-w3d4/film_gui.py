from flask import Flask, request, render_template, redirect, url_for
import os, csv, json

app = Flask(__name__)

@app.route("/")
def all_films():
    f = open("/Users/hoanjinan_otoko/Desktop/epam-ds-training/greenfox/hoanjinan/week-03/day-4/exercises-w3d4/films.json", mode = "r", encoding = "utf-8")
    content = json.load(f)
    f.close()
    # title = []
    # year = []
    # genre = []
    # description = []
    # for i in range(len(content)):
    #     title.append(content[i]["title"])
    #     year.append(content[i]["year"])
    #     genre.append(content[i]["genre"])
    #     description.append(content[i]["description"])
    return render_template("film.html", content = content)

@app.route("/edit-film/<film_id>")
def edit_film():
    pass

if __name__ == "__main__":
    app.run()
