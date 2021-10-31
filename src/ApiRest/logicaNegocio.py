from db import Database
from model.ModelMedicion import Medicion
#-----------------------------------------------------------------------------------
# @author: Juan Carlos Hernandez Ramirez
# Fecha: 14/10/2021
#-----------------------------------------------------------------------------------

class LogicaNegocio:

    ##/
    ## Constructor
    ## @param self: objeto que contiene los propios metods y atributos de la clase
    ## @param app: Clase base que contiene la configuracion de la BD (nombre BD, user,password....)
    ##/
    def __init__(self, app):
        self.db = Database(app)
    ##/
    ## Metodo que preapra la sentencia SQL para insertarla datos en la BD
    ## Devuelve 1 si ha conseguido insetar todas las mediciones, -1 en caso contrario
    ## @param self: objeto que contiene los propios metods de la clase
    ## @param mediciones: lista de mdiciones que se insetaran en la BD
    ## @return res: entero que indicara el resultado de la opreacion en la BD
    ## [medicion]->guardarMediciones->Z
    ##/
    def guardarMediciones(self,mediciones):
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

    ##/
    ## Metodo que preapra la sentencia SQL para obtener todas las mediciones en la BD
    ## @param self: objeto que contiene los propios metodos y atributos de la clase
    ## @return res: json con formateado que contendra todas las mediciones
    ## obtenerTodasLasMediciones->[medicion]
    ##/
    def obtenerTodasLasMediciones(self):
        data = self.db.queryStatemen("Select * from mediciones")
        return self.devolverMediciones(data)  

    ##/
    ## Metodo que preapra la sentencia SQL para obtener las ultimas mediciones en la BD
    ## @param self: objeto que contiene los propios metodos y atributos de la clase
    ## @param cuantos: numero que indicar el numero de ultimas mediciones que inserteremos
    ## @return res: json con formateado que contendra las mediciones segun el parametro recibido
    ## N->obtenerLasUltimasMediciones->[medicion]
    ##/
    def obtenerLasUltimasMediciones(self,cuantos):
        data = self.db.queryStatemen("SELECT * FROM mediciones ORDER BY id DESC LIMIT {}".format(cuantos))
        return self.devolverMediciones(data)

    ##/
    ## Crea los objetos Medicion y los prepara para ser enviados en formato JSON, segun el resultado obtenido en las consultas a la BD
    ## @param self: objeto que contiene los propios metodos y atributos de la clase
    ## @param data: Array que contendra los datos obtnedidos en la BD
    ## @return res: json formateado que contendra las mediciones
    ## [Medicion]->obtenerLasUltimasMediciones->JSON
    ##/
    def devolverMediciones(self,data):
        res = {}
        res['mediciones'] = []
        for row in data:
            res['mediciones'].append(Medicion(row[0],row[1],row[2],row[3],row[4],row[5]).toJson())
        return res