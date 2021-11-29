from flask_mysqldb import MySQL
#-----------------------------------------------------------------------------------
# @author: Juan Carlos Hernandez Ramirez
# Fecha: 14/10/2021
# Nombre:db.py
# Descripcion: Clase que controla la logica para conectarse 
#-----------------------------------------------------------------------------------

class Database:
    
    ##/
    ## Constructor
    ## @param self: objeto que contiene los propios metods y atributos de la clase
    ## @param app: Clase base que contiene la configuracion de la BD (nombre BD, user,password....)
    ##/
    def __init__(self, app):
        self.mysql = MySQL(app)

    ##/
    ## Metodo que realiza una insercion en la BD (segun la sentencia recibida)
    ## @param self: objeto que contiene los propios metods de la clase
    ## @param statement: string que contenra la sentencia a ejecutar en la BD
    ## @return N: entero que indicara el numero de las filas tras haber insertado los nuevos datos
    ## Texto->insertStatement->N
    ##/
    def insertStatement(self, statement):
        db = self.mysql.connection.cursor()
        db.execute(statement)
        self.mysql.connection.commit()
        return db.rowcount

    ##/
    ## Metodo que realiza una consulta en la BD (segun la sentencia recibida)
    ## @param self: objeto que contiene los propios metods de la clase
    ## @param query: string que contenra la consulta a ejecutar en la BD
    ## @return data: Array con los datos obtenidos en la consulta
    ## Texto->queryStatemen->[Data]
    ##/
    def queryStatement(self,query):
        db = self.mysql.connection.cursor()
        db.execute(query)
        data = db.fetchall()
        return data
