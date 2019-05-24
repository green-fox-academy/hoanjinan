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
            
        
print(transformed_posts)