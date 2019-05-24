@app.route("/weather")
def get_weather():
    return render_template("weather.html", weather = "Good", display = True, numbers = [1, 2, 3, 4])