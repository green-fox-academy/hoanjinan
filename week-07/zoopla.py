from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/zoopia")
def zoopla():
    data = pd.read_csv("listing.csv", index_col = 0)
    property_type = data["property_type"].notna().unique().tolist()
    return render_template("zoopla.html", property_type = property_type)

@app.route("/")
def navigation():
    return render_template("navigation.html")

if __name__ == "__main__":
    app.run()
