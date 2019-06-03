from Config import Config
import psycopg2

class Query():
    def __init__(self):
        self.connection = Config().connect()
        self.cursor = self.connection.cursor()

    def query(self, sql_query):
        query_para = sql_query
        self.cursor.execute(query_para)
        result = self.cursor.fetchall()
        self.cursor.close()
        self.connection.close()
        return result