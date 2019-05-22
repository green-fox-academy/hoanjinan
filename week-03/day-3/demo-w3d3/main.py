from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")

def hello_world():
    return f"hello world"

@app.route("/<username>")
def hello_name(username):
    return render_template("index.html", name = username)

@app.route("/cat")
def cat():
    return f"How are you {request.args.get('name', 'anonymus')}?"

if __name__ == "__main__":
    app.run()