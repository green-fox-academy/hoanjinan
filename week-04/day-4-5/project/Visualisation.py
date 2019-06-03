from Query import Query
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Who sent the most messages to the thanks channel?
query_most_messages = """SELECT user_id AS users, COUNT(user_id) AS user_count FROM messages
                                WHERE channel = 'Thanks'
                                GROUP BY users
                                ORDER BY user_count DESC LIMIT 10;"""
result_most_messages = Query().query(query_most_messages)
# for i in result_most_messages:
#     print(i)
sns.distplot(result_most_messages, bins=10, kde=False, rug=True)
df = pd.DataFrame(result_most_messages, columns=['User', 'User Count'])
df.plot(kind='bar', x='User', y='User Count', figsize=(5, 5))
plt.tight_layout()
plt.show()


# Which emoji is the most common as reaction in the thanks channel?
query_most_emoji = """SELECT reaction, COUNT(reaction) AS emoji_count FROM reactions
                            JOIN messages
                            ON reactions.message_id = messages.message_id
                            WHERE channel = 'Thanks'
                            GROUP BY reaction
                            ORDER BY emoji_count DESC LIMIT 10;"""
result_most_emoji = Query().query(query_most_emoji)
figureObject, axesObject = plt.subplots()
name = []
count = []
for i in result_most_emoji:
    name.append(i[0])
    count.append(i[1])
explodeTuple = (0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
axesObject.pie(count,
                explode = explodeTuple,
                labels=name,
                autopct='%1.2f',
                startangle=90)
                
axesObject.axis('equal')
plt.tight_layout()
plt.show()

# Who reacted to the most messages?
query_react_most_msg = """SELECT user_id AS users, COUNT(user_id) AS reaction_count FROM reactions
                                GROUP BY users
                                ORDER BY reaction_count DESC LIMIT 10;"""
result_react_most_msg = Query().query(query_react_most_msg)
for i in result_react_most_msg:
    print(i)

# Who is the most mentioned person in the thanks channel?
query_most_mentioned = """SELECT mentions.user_id AS users, COUNT(mentions.user_id) AS mention_count FROM mentions
                                JOIN messages
                                ON mentions.message_id = messages.message_id
                                WHERE channel = 'Thanks'
                                GROUP BY users
                                ORDER BY mention_count DESC LIMIT 10;"""
result_most_mentioned = Query().query(query_most_mentioned)
for i in result_most_mentioned:
    print(i)

# Which message got the most reactions in the thanks channel?
query_most_reactions = """SELECT reactions.message_id, COUNT(reactions.message_id) AS reaction_count FROM reactions
                                JOIN messages
                                ON reactions.message_id = messages.message_id
                                WHERE channel = 'Thanks'
                                GROUP BY reactions.message_id
                                ORDER BY reaction_count DESC LIMIT 10;"""
result_most_reactions = Query().query(query_most_reactions)
for i in result_most_reactions:
    print(i)
