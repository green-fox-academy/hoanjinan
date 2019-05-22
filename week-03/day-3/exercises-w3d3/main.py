from flask import Flask, request, render_template

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return f"Hello World"

@app.route("/")
def hello_name():
    return render_template("index.html")

@app.route("/film/<filmname>")
def film(filmname):
    return render_template(f"{filmname}")

if __name__ == "__main__":
    app.run()