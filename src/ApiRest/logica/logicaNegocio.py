from logica.db import Database
from model.ModelMedicion import Medicion
from model.ModelUsuario import Usuario
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
        data = self.db.queryStatement("Select * from mediciones")
        return self.devolverMediciones(data)  

    ##/
    ## Metodo que preapra la sentencia SQL para obtener las ultimas mediciones en la BD
    ## @param self: objeto que contiene los propios metodos y atributos de la clase
    ## @param cuantos: numero que indicar el numero de ultimas mediciones que inserteremos
    ## @return res: json con formateado que contendra las mediciones segun el parametro recibido
    ## N->obtenerLasUltimasMediciones->[medicion]
    ##/
    def obtenerLasUltimasMediciones(self,cuantos):
        data = self.db.queryStatement("SELECT * FROM mediciones ORDER BY id DESC LIMIT {}".format(cuantos))
        return self.devolverMediciones(data)


    ##/
    ## Metodo que preapra la sentencia SQL para obtener las mediciones de una fecha concreta
    ## @param self: objeto que contiene los propios metodos y atributos de la clase
    ## @param fecha: dia del que se recogeran todas las fechas
    ## @return res: json con formateado que contendra las mediciones segun el parametro recibido
    ## N->obtenerLasUltimasMediciones->[medicion]
    ##/
    def obtenerTodasMedicionesPorFecha(self,fecha):
        data = self.db.queryStatement("SELECT * FROM mediciones WHERE fecha = '{}' ".format(fecha))
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


    ##/
    ## loginUsuario()
    ## Recibe un email y una contraseña y si estos están en la base de datos devuelve un usuario
    ## @param self: objeto que contiene los propios metodos y atributos de la clase
    ## @param mail: texto que contendrá el correo que se quiere buscar en la bd
    ## @param contrasenya: texto que contendrá la contraseña que se quiere buscar en la bd
    ## @return res: json que contiene el usuario, si el usuario no se encuentra en la base de datos se devolverá  -1
    ## mail:Texto,contrasenya:Texto -> loginUsuario-> Usuario
    ##/
    def loginUsuario(self,mail,contrasenya):
        data = self.db.queryStatement("SELECT * FROM `usuario` WHERE mail LIKE '{}' AND password LIKE '{}'".format(mail,contrasenya))
        print("ESto ---> ")
        if(len(data) == 0):
            return "-1"
        else:
            usuario = Usuario(data["id_usuario"],data["mail"],data["nombre"],data["apellidos"],data["isAutobusero"],data["edad"],data["matricula"],data["telefono"],data["password"])
            return usuario

    ##/
    ## crearUsuario()
    ## Recibe un objeto json con los datos del usuario y lo mete en la base de datos
    ## @param self: objeto que contiene los propios metodos y atributos de la clase
    ## @param usuario: objeto json que contiene los datos del usuario
    ## @return res: entero que indicará el resultado de la operación de la base de datos 
    ##  Json -> crearUsuario -> Z
    ##/
    def crearUsuario(self,usuario):
        data = self.db.queryStatement("SELECT * FROM `usuario` WHERE mail LIKE '{}' AND password LIKE '{}'".format(usuario["mail"],usuario["password"]))
        if(len(data) == 0):

            statement = "INSERT INTO `usuario` (mail,nombre,apellidos,isAutobusero,edad,matricula,telefono,password) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}');".format(
            usuario['mail'],usuario['nombre'],usuario['apellidos'],usuario['isAutobusero'], usuario['edad'], usuario['matricula'], usuario['telefono'], usuario['password'] )
            resTMP = self.db.insertStatement(statement)

            return 1
        else:
            return "-1"

    ##/
    ## editarUsuario()
    ## Recibe un objeto json con los datos del usuario y actualiza algun usuario que tenga en la base de datos
    ## @param self: objeto que contiene los propios metodos y atributos de la clase
    ## @param usuario: objeto json que contiene los datos del usuario
    ## @return res: entero que indicará el resultado de la operación de la base de datos 
    ##  Usuario -> editarUsuario() -> Z
    ##/  

    def editarUsuario(self,usuario):
        statement = "UPDATE `usuario` SET `mail`='{}',`nombre`='{}',`apellidos`='{}',`isAutobusero`='{}',`edad`='{}',`matricula`='{}',`telefono`='{}',`password`='{}' WHERE `id_usuario` = '{}' ".format(
            usuario['mail'],usuario['nombre'],usuario['apellidos'],usuario['isAutobusero'], usuario['edad'], usuario['matricula'], usuario['telefono'], usuario['password'],usuario['id_usuario'])
        resTMP = self.db.insertStatement(statement)
        return 1
    

       
