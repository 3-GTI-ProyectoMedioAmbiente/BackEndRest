from logica.db import Database
from model.ModelMedicion import Medicion
from model.ModelUsuario import Usuario
import datetime
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
            statement = "INSERT INTO mediciones (medicion,fecha,hora,localizacion_lat,localizacion_lon,id_sensor,id_tipoMedicion) VALUES ({},'{}','{}',{},{},{},{});".format(
            medicion['medicion'],medicion['fecha'],medicion['hora'],medicion['localizacion_lat'], medicion['localizacion_lon'], medicion['id_sensor'], medicion['id_tipoMedicion'])
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
    def obtenerMedicionesUltimas24h(self):
        now = datetime.datetime.now()-datetime.timedelta(hours=24)
        time = now.strftime("%H:%M:%S") 
        yesterdayDate = now.strftime("%Y-%m-%d")
        data = self.db.queryStatement("SELECT * FROM mediciones WHERE concat(fecha,' ',hora)>='{} {}'".format(yesterdayDate,time))
        return self.devolverMediciones(data)

    ##/
    ## Metodo que preapra la sentencia SQL para obtener las mediciones de un perido concrecto por usuario
    ## @param self: objeto que contiene los propios metodos y atributos de la clase
    ## @param periodo: perido del que se quieren coger las medidas
    ## @param idUsuario: Id del usuario del que se sacaran las medidas
    ## @return res: json con formateado que contendra las mediciones segun el parametro recibido
    ## N->obtenerLasUltimasMediciones->[medicion]
    ##/
    def obtenerMedicionesConPeriodoPorUsuario(self, periodo, idUsuario):
        if periodo == "dia":
            now = datetime.datetime.now()-datetime.timedelta(hours=24)
            dateFilter = now.strftime("%Y-%m-%d")

        elif periodo =="semana":
            now = datetime.datetime.now()-datetime.timedelta(days=7)
            dateFilter = now.strftime("%Y-%m-%d")

        elif periodo=="mes":
            now = datetime.datetime.now()-datetime.timedelta(days=30)
            dateFilter = now.strftime("%Y-%m-%d")

        else:
            print("invalidInput")
            return
        time = now.strftime("%H:%M:%S") 
        data = self.db.queryStatement(
            "SELECT m.id, m.medicion, m.fecha, m.hora, m.localizacion_lat, m.localizacion_lon, m.id_sensor, m.id_tipoMedicion "
            +"FROM mediciones m LEFT JOIN sensor s ON m.id_sensor=s.id_sensor LEFT JOIN usuario u ON u.id_usuario=s.id_sensor "
            +"WHERE u.id_usuario='{}' and (fecha>='{}')".format(idUsuario,dateFilter,time))

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
            res['mediciones'].append(Medicion(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]).toJson())
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
        print("Entro a la logica del negocio ---> ")
        if(len(data) == 0):
            return "-1"
        else:
            for row in data:
                print("dataLOgin ---> ")
            
            print(data)
            
            usuario = Usuario(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5].strftime('%Y-%m-%d'),data[0][6],data[0][7],data[0][8],data[0][9]).toJson()
            res = []
            res.append(usuario)
            
            #print(res[0]['mail'])
            return res[0]


    ##/
    ## crearUsuario()
    ## Recibe un objeto json con los datos del usuario y lo mete en la base de datos
    ## @param self: objeto que contiene los propios metodos y atributos de la clase
    ## @param usuario: objeto json que contiene los datos del usuario
    ## @return res: entero que indicará el resultado de la operación de la base de datos 
    ##  Json -> crearUsuario -> Z
    ##/
    def crearUsuario(self,usuario):
        data = self.db.queryStatement("SELECT * FROM `usuario` WHERE mail LIKE '{}'".format(usuario["mail"]))
        if(len(data) == 0):
            print(usuario)
            
            if(usuario['isAutobusero'] == True):
                statement = "INSERT INTO `usuario` (mail,nombre,apellidos,isAutobusero,fechaNacimiento,matricula,telefono,password) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}');".format(
            usuario['mail'],usuario['nombre'],usuario['apellidos'],1, usuario['fechaNacimiento'], usuario['matricula'], usuario['telefono'], usuario['password'] )
            else:
                statement = "INSERT INTO `usuario` (mail,nombre,apellidos,isAutobusero,fechaNacimiento,matricula,telefono,password) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}');".format(
            usuario['mail'],usuario['nombre'],usuario['apellidos'],0, usuario['fechaNacimiento'], usuario['matricula'], usuario['telefono'], usuario['password'] )
            
            
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
        statement = "UPDATE `usuario` SET `nombre`='{}',`mail`='{}',`apellidos`='{}',`edad`='{}',`telefono`='{}',`password`='{}',`id_sensor`='{}' WHERE `id_usuario` = '{}' ".format(
            usuario['nombre'],usuario['mail'],usuario['apellidos'], usuario['fechaNacimiento'], usuario['telefono'], usuario['password'],usuario['id_sensor'],usuario['id_usuario'])
        resTMP = self.db.insertStatement(statement)
        return 1

    
    
    ## Peticion que permite obtener el id del sensor a aprtir de la mac del mismo
    ## @param mac texto que contiene la mac del sensor
    ## texto -> obtenerIdSensorMedianteMac -> Z
    ## @return: Entero que indica la id del sensor (SI AUN NO ESTA VINCULADO)
    ##/
    def obtenerIdSensorMedianteMac(self,mac):
        data = self.db.queryStatement("SELECT s.id_sensor,s.direccion_mac FROM sensor s where NOT EXISTS(Select * from usuario u INNER JOIN sensor s on s.id_sensor = u.id_sensor where s.direccion_mac = '{}') and s.direccion_mac='{}'".format(mac,mac))
        if(len(data) == 0):
            return "-1"
        else:
            res = str(data[0][0])
            return res
    