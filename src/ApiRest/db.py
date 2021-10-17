from flask_mysqldb import MySQL
class Database:
    def __init__(self, app):
        self.mysql = MySQL(app)
    
    def insertStatement(self, statement):
        db = self.mysql.connection.cursor()
        db.execute(statement)
        self.mysql.connection.commit()
        return db.rowcount

    def queryStatemen(self,query):
        db = self.mysql.connection.cursor()
        db.execute(query)
        data = db.fetchall()
        return data
