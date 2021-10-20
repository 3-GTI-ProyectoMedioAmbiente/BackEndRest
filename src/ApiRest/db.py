from flask_mysqldb import MySQL
#-----------------------------------------------------------------------------------
# @author: Juan Carlos Hernandez Ramirez
#Fecha: 14/10/2021
#-----------------------------------------------------------------------------------

class Database:
    def __init__(self, app):
        self.mysql = MySQL(app)
    ## Metodo que realiza una insercion en la BD
    def insertStatement(self, statement):
        db = self.mysql.connection.cursor()
        db.execute(statement)
        self.mysql.connection.commit()
        return db.rowcount

    ## Metodo que realiza una consulta en la BD
    def queryStatemen(self,query):
        db = self.mysql.connection.cursor()
        db.execute(query)
        data = db.fetchall()
        return data
