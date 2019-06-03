from DataRetrive import DataRetrive
from Config import Config
import psycopg2, sys

connection = Config().connect()

user_id = []

user_id = DataRetrive("gfa-team-thanks.json").retrive_user(user_id)
user_id = DataRetrive("gfa-team-random.json").retrive_user(user_id)

message_id = []
user_id_m = []
message = []
channel = []

message_id, user_id_m, message, channel = DataRetrive("gfa-team-thanks.json").retrive_message(message_id, user_id_m, message, channel, "Thanks")
message_id, user_id_m, message, channel = DataRetrive("gfa-team-random.json").retrive_message(message_id, user_id_m, message, channel, "Random")
user_id_r = []
message_id_r = []
reaction = []

user_id_r, message_id_r, reaction = DataRetrive("gfa-team-thanks.json").retrive_reaction(user_id_r, message_id_r, reaction)
user_id_r, message_id_r, reaction = DataRetrive("gfa-team-random.json").retrive_reaction(user_id_r, message_id_r, reaction)

message_id_mtns = []
user_id_mtns = []

message_id_mtns, user_id_mtns = DataRetrive("gfa-team-thanks.json").retrive_mentions(message_id_mtns, user_id_mtns)
message_id_mtns, user_id_mtns = DataRetrive("gfa-team-random.json").retrive_mentions(message_id_mtns, user_id_mtns)


create_table = """CREATE TABLE %(table_name)s (%(entity)s);"""
insert_users = """INSERT INTO users (user_id) VALUES(%(user_id)s);"""
insert_messages = """INSERT INTO messages(message_id, user_id, message, channel)
                        VALUES(
                            %(message_id)s,
                            %(user_id_m)s,
                            %(message)s,
                            %(channel)s
                        );"""
insert_reactions = """INSERT INTO reactions(user_id, message_id, reaction)
                        VALUES(
                            %(user_id_r)s,
                            %(message_id_r)s,
                            %(reaction)s
                        );"""

insert_mentions = """INSERT INTO mentions(message_id, user_id)
                        VALUES(
                            %(message_id_mtns)s,
                            %(user_id_mtns)s
                            );"""

cursor = connection.cursor()
if sys.argv[1] == "-f":
    if sys.argv[2] == "users":
        for i in user_id:
            cursor.execute(insert_users, {"user_id": i})
    elif sys.argv[2] == "messages":
        for i in range(len(message_id)):
            cursor.execute(insert_messages, {
                "message_id": message_id[i],
                "user_id_m": user_id_m[i],
                "message": message[i],
                "channel": channel[i]
            })
    elif sys.argv[2] == "reactions":
        for i in range(len(user_id_r)):
            for j in range(len(user_id_r[i])):
                if message_id_r[i] in message_id:
                    cursor.execute(insert_reactions, {
                    "user_id_r": user_id_r[i][j],
                    "message_id_r": message_id_r[i],
                    "reaction": reaction[i]
                })
                
    elif sys.argv[2] == "mentions":
        for i in range(len(message_id_mtns)):
            for j in range(len(user_id_mtns[i])):
                if user_id_mtns[i][j] in user_id:
                    cursor.execute(insert_mentions, {
                    "message_id_mtns": message_id_mtns[i],
                    "user_id_mtns": user_id_mtns[i][j]
                })


connection.commit()
cursor.close()
connection.close()