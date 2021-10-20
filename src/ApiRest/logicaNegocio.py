from db import Database
from model.ModelMedicion import Medicion
#-----------------------------------------------------------------------------------
# @author: Juan Carlos Hernandez Ramirez
#Fecha: 14/10/2021
#-----------------------------------------------------------------------------------

class LogicaNegocio:
    def __init__(self, app):
        self.db = Database(app)
    ## Metodo que preapra la sentencia SQL para insertarla en la BD
    ## Devuelve 1 si ha conseguido insetar todas las mediciones, -1 en caso contrario
    def insertMediciones(self,mediciones):
        resContador = 0
        for medicion in mediciones:
            statement = "INSERT INTO mediciones (medicion,fecha,hora,localizacion_lat,localizacion_lon) VALUES ({},'{}','{}',{},{});".format(
            medicion['medicion'],medicion['fecha'],medicion['hora'],medicion['localizacion_lat'], medicion['localizacion_lon'] )
            resTMP = self.db.insertStatement(statement)
            if resTMP==1:
                resContador+=1
        res = -1
        if resContador == len(mediciones):
            res = 1
        return res

    def getTodasLasMediciones(self):
        data = self.db.queryStatemen("Select * from mediciones")
        return self.devolverMediciones(data)  

    def getUltimasMediciones(self,cuantos):
        data = self.db.queryStatemen("SELECT * FROM mediciones ORDER BY id DESC LIMIT {}".format(cuantos))
        return self.devolverMediciones(data)
    
    #Crea los objetos Medicion y los prepara para ser enviados en formato JSON, segun el resultado obtenido en las consultas a la BD
    def devolverMediciones(self,data):
        res = {}
        res['mediciones'] = []
        for row in data:
            res['mediciones'].append(Medicion(row[0],row[1],row[2],row[3],row[4],row[5]).toJson())
        return res
        

