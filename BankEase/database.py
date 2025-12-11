import pymysql

class DB():
    def __init__(self):
            self.mydb = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                database='bank'
            )
            self.cursor = self.mydb.cursor()