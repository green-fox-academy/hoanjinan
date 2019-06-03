import json, re

class DataRetrive():
    def __init__(self, path):
        f_json = open(path, mode = "r", encoding = "utf-8")
        self.content = json.load(f_json)
        f_json.close()

    def retrive_user(self, user_list):
        for i in self.content:
            if "user" in i:
                if i["user"] not in user_list:
                    user_list.append(i["user"])
        return user_list

    def retrive_message(self, message_id, user_id, message, channel, channel_name):
        for i in self.content:
            if "ts" in i and "user" in i and "text" in i:
                if i["ts"] not in message_id:
                    message_id.append(i["ts"])
                    user_id.append(i["user"])
                    message.append(i["text"])
                    channel.append(channel_name)
        return message_id, user_id, message, channel

    def retrive_reaction(self, user_id, message_id, reaction):
        for i in self.content:
            if "reactions" in i:
                for j in i["reactions"]:
                    if "users" in j and "ts" in i and "name" in j:
                        # if i["ts"] not in message_id:
                        user_id.append(j["users"])
                        message_id.append(i["ts"])
                        reaction.append(j["name"])
        return user_id, message_id, reaction

    def retrive_mentions(self, message_id, user_id):
        regular_ex = r".+?@(\w+)>"
        m = re.compile(regular_ex)
        for i in self.content:
            if "user" in i and "text" in i and "ts" in i:
                if m.match(i["text"]) is not None:
                    message_id.append(i["ts"])
                    user_id.append(m.findall(i["text"]))
        return message_id, user_id