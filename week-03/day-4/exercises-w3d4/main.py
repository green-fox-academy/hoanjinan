from flask import Flask, request, render_template, jsonify, make_response, json

app = Flask(__name__)

@app.route("/api")
def api_root():
    response = jsonify(a = 12, b = 13)
    return response

@app.route("/api", methods = ["POST"])
def api_root_post():
    response = jsonify(apple = 34, key = request.headers["x-api-key"])
    return response

@app.route("/api/films")
def api_film():
    f = open("/Users/hoanjinan_otoko/Desktop/epam-ds-training/greenfox/hoanjinan/week-03/day-4/exercises-w3d4/films.json", mode = "r", encoding = "utf-8")
    content = json.load(f)
    f.close()

    response = jsonify(content)
    return response

@app.route("/api/films/<int:film_id>")
def api_film_select(film_id):
    content_dic = {}
    count = 1

    f = open("/Users/hoanjinan_otoko/Desktop/epam-ds-training/greenfox/hoanjinan/week-03/day-4/exercises-w3d4/films.json", mode = "r", encoding = "utf-8")
    content = json.load(f)
    f.close()

    for i in content:
        content_dic[count] = {"id": i["id"], "title": i["title"], "year": i["year"], "genre": i["genre"], "description": i["description"]}
        count += 1

    response = jsonify(content_dic[film_id])
    return response

@app.route("/api/films/<int:film_id>", methods = ["POST"])
def api_film_post(film_id):
    content_dic = {}
    count = 1
    api_key = "hello"
    key = request.headers["api-key"]

    if api_key == key:
        f = open("/Users/hoanjinan_otoko/Desktop/epam-ds-training/greenfox/hoanjinan/week-03/day-4/exercises-w3d4/films.json", mode = "r", encoding = "utf-8")
        content = json.load(f)
        f.close()

        for i in content:
            content_dic[count] = {"id": i["id"], "title": i["title"], "year": i["year"], "genre": i["genre"], "description": i["description"]}
            count += 1

        response = jsonify(content_dic[film_id])
        return response
    else:
        response = jsonify(error = "Invalid API_KEY")
        response.status_code = 403
        return response

@app.route("/api/films/<int:film_id>", methods = ["PUT"])
def api_film_put(film_id):
    content_dic = {}
    count = 1
    api_key = "hello"
    key = request.headers["api-key"]

    if api_key == key:
        f = open("/Users/hoanjinan_otoko/Desktop/epam-ds-training/greenfox/hoanjinan/week-03/day-4/exercises-w3d4/films.json", mode = "r", encoding = "utf-8")
        content = json.load(f)
        f.close()

        for i in content:
            content_dic[count] = {"id": i["id"], "title": i["title"], "year": i["year"], "genre": i["genre"], "description": i["description"]}
            count += 1

        if film_id in content_dic:
            content_dic[film_id]["title"] = "Harry Potter and the Half-Blood Prince"
            content_dic[film_id]["year"] = 2009
            content_dic[film_id]["description"] = "Harry Potter and the Half-Blood Prince is a 2009 fantasy film directed by David Yates and distributed by Warner Bros. Pictures.[3] It is based on J. K. Rowling's 2005 novel of the same name. The film, which is the sixth instalment in the Harry Potter film series, was written by Steve Kloves and produced by David Heyman and David Barron.[4] The story follows Harry Potter's sixth year at Hogwarts as he receives a mysterious textbook, falls in love, and attempts to retrieve a memory that holds the key to Lord Voldemort's downfall."
            response = jsonify(content_dic[film_id])
            return response
        else:
            response = jsonify(error = f"No film found with {film_id} ID")
            response.status_code = 404
            return response
    else:
        response = jsonify(error = "Invalid API_KEY")
        response.status_code = 403
        return response

# @app.route("/api/films/<int:film_id>", methods = ["DELETE"])
# def api_film_delete(film_id):
#     content_dic = {}
#     count = 1
#     api_key = "hello"
#     key = request.headers["api-key"]

#     if api_key == key:
#         f = open("/Users/hoanjinan_otoko/Desktop/epam-ds-training/greenfox/hoanjinan/week-03/day-4/exercises-w3d4/films.json", mode = "r", encoding = "utf-8")
#         content = json.load(f)
#         f.close()

#         for i in content:
#             content_dic[count] = {"id": i["id"], "title": i["title"], "year": i["year"], "genre": i["genre"], "description": i["description"]}
#             count += 1

#         if film_id in content_dic:
#             response = jsonify(content_dic[film_id])
#             return response
#         else:
#             response = jsonify(error = f"No film found with {film_id} ID")
#             response.status_code = 404
#             return response
#     else:
#         response = jsonify(error = "Invalid API_KEY")
#         response.status_code = 403
#         return response

if __name__ == "__main__":
    app.run()