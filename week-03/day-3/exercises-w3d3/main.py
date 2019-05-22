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

# @app.route("/query/")
# def query():
    

if __name__ == "__main__":
    app.run()