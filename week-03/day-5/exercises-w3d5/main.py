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

@app.route("/articles")
def articles():
    articles = [
        {
            "content": "Ne istas culpa ha im negat de. Ii perductae evertenda at desuescam. Nudi per ita sui dare ideo sola omne ordo. Sui sex item sane quum. Paucos sicuti tot qui tantae aliquo strata iis tantas. Mo purgantur at affirmans im reddendum co. Pleraque videntur ut ideamque imaginem ha.",
            "seen": ["John", "Jane", "Bob"]
        },
        {
            "content": "Aliud curam seu venti nihil sed istud volui eae qua. Autho ha falsi fidam tangi ut an tactu. Revera per eandem vox coelum videbo nam virtus. Item olim ei se duas ut. Ut mo ut peccato student adorare et diversa. Praecipuis ad conjunctam me percipitur agnoscerem at perfectius respondere. Horum meo porro uno debeo. Fallacem sentiens ha expertus delapsus dubitare ii. Ex ii efficiente et to perspicuae voluptatem arbitrabar.",
            "seen": ["John", "Jane"]
        },
        {
            "content": "Credendi at nequidem exhibere de. Debeo me dicam ex at ferri digna. Coloribus differant disputari vix cogitandi jam stabilire. Perfacile ut reliquiae perfectae ut. Fuisse falsas captum cui volent notior verbis sui. Meam idem nam ope prae isti quia jure hac. Lor durent has secius fronte usu auditu sumpti. Falso nomen aliud vim calor jam alias annos ubi. Movendi sum creatus vim fas majorem attendo propter. Sui videamus uno profecto refutent rom notitiam innumera potuerit.",
            "seen": ["John"]
        },
        {
            "content": "Potui habeo visus ens mea. An vi re continetur me familiarem negationem. Rei inveniri jam viderunt subducam tam imponere jam. Sub cui more ipsi meum.",
            "seen": []
        }
    ]
    return render_template("articles.html", articles = articles)

@app.route("/posts")
def posts():
    authors = [
        {
            "id": 100,
            "name": "John",
            "likes": [
                202,
                200
            ]
        },
        {
            "id": 101,
            "name": "Jane",
            "likes" : [
                200
            ]
        }
    ]

    posts = [
        {
            "id": 200,
            "author": 100,
            "content": "Difficulty on insensible reasonable in. From as went he they."
        },
        {
            "id": 201,
            "author": 100,
            "content": "Preference themselves me as thoroughly partiality considered on in estimating."
        },
        {
            "id": 202,
            "author": 101,
            "content": "In as name to here them deny wise this. As rapid woody my he me which."
        }
    ]

    transformed_posts = []
    like_list = []
    for i in posts:
        for j in authors:
            if i["author"] == j["id"]:
                transformed_posts.append({
                                            "name": j["name"], 
                                            "post_id": i["id"],
                                            "post_content": i["content"]
                                        })
    for i in transformed_posts:
        for j in authors:
            for k in range(len(j["likes"])):
                if i["post_id"] == j["likes"][k]:
                    like_list.append(j["name"])
        i["who_liked"] = like_list
        like_list = []
    
    return render_template("posts.html", posts = transformed_posts)

@app.route("/")
def navigation():
    return render_template("navigation.html")

if __name__ == "__main__":
    app.run()
