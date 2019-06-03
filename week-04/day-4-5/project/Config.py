import psycopg2

class Config():
    def __init__(self, host = "localhost", dbname = "project_w4d4", user = "hoanjinan_otoko", password = "hoanjinan_otoko"):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password

    def connect(self):
        return psycopg2.connect(
                host = self.host,
                dbname = self.dbname,
                user = self.user,
                password = self.password
                )