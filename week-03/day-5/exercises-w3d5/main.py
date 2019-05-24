from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/greeting")
def random_lang():
    greet = ["Hello", "Hola", "Bonjour", "Guten Tag", "你好", "こんにちは"]
    name = ["Zilan", "John", "Payne", "Simon", "Steven", "Levi"]
    random_greet = random.choice(greet)
    random_name = random.choice(name)
    return render_template("random_lang.html", random_greet = random_greet, name = random_name)

@app.route("/products")
def products():
    products = [
        ("Milk", 3.59123),
        ("Bread", 2.96332),
        ("Rice", 0.64111)
    ]

    return render_template("products.html", products = products)



if __name__ == "__main__":
    app.run()
