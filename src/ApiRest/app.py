from flask import Flask,request
from logica.logicaNegocio import LogicaNegocio
from flask_cors import CORS
import json


#-----------------------------------------------------------------------------------
# @author: Juan Carlos Hernandez Ramirez y Sergi
#Fecha: 14/10/2021
#-----------------------------------------------------------------------------------

#Configuracion de la BD
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_mediciones'
CORS(app)
logicaNegocio = LogicaNegocio(app)
##/
## http://{ip_server}/insertMedicionJson
## Peticion que controla la insercion de datos mediante JSON
## @return HTML: html que contiene el resultado obtenido en la insercion exito=1, fallo=-1
## Medicion->insertMedicionJson-> HTML
##/
@app.route('/insertMedicionJson', methods=['POST'])
def insertMedicionJson():
    data=request.get_json()
    res = logicaNegocio.guardarMediciones(data['mediciones'])
    return '''<h1>Resultado:  {} </h1>'''.format(res)

##/
## http://{ip_server}/obtenerTodasLasMediciones
## Peticion que devueve todas las mediciones JSON
## @return json: JSON que contendra todas las mediciones 
## getAllMeasures-> [Medicion]
##/
@app.route('/obtenerTodasLasMediciones')
def obtenerTodasLasMediciones():
    data = logicaNegocio.obtenerTodasLasMediciones()
    return json.dumps(data, indent=4)

##/
## http://{ip_server}/obtenerLasUltimasMediciones
## Peticion que devueve las utlimas mediciones JSON
## @return json: JSON que contendra las ultimas mediciones 
## getLastMeasures-> [Medicion]
##/
@app.route('/obtenerLasUltimasMediciones')
def obtenerLasUltimasMediciones():
    cuantos = request.args.get('cuantos')
    data = logicaNegocio.obtenerLasUltimasMediciones(cuantos)
    return json.dumps(data,indent=4)

##/
## http://{ip_server}/obtenerMedicionesUltimas24h
## Peticion que devueve las medciones de un dia en concreto
## @return json: JSON que contendra las ultimas mediciones 
## getLastMeasures-> [Medicion]
##/
@app.route('/obtenerMedicionesUltimas24h')
def obtenerMedicionesUltimas24h():
    data = logicaNegocio.obtenerMedicionesUltimas24h()
    return json.dumps(data,indent=4)

##/
## http://{ip_server}/obtenerMedicionesConPeriodoPorUsuario
## Peticion que devueve las medciones segun un periodo concreto por usuario.
## El periodo pude ser diario, mensual o semanal 
## @return json: JSON que contendra las ultimas mediciones 
## getLastMeasures-> [Medicion]
##/
@app.route('/obtenerMedicionesConPeriodoPorUsuario')
def obtenerMedicionesConPeriodoPorUsuario():
    periodo = request.args.get('periodo')
    idUsuario = request.args.get('idUsuario')
    data = logicaNegocio.obtenerMedicionesConPeriodoPorUsuario(periodo,idUsuario)
    return json.dumps(data,indent=4)



##/
## http://{ip_server}/loginUsuario
## Peticion que devueve un usuario dependiendo del correo y la contraseña
## @param mail: Correo del usuario que se quiere loguear
## @param contrasenya: Contraseña del usuario que se quiere loguear
## @return json: JSON que contendra el usuario
## mail:Texto,contrasenya:Texto -> loginUsuario -> Usuario
##/
@app.route('/loginUsuario')
def loginUsuario():
    data = request.get_json()
    #print(data)
    res = logicaNegocio.loginUsuario(data["mail"],data["contrasenya"])
    
    return '''<h1>Resultado:  {} </h1>'''.format(res)

##/
## http://{ip_server}/crearUsuario
## Peticion que crea un usuario para la base de datos
## @param Usuario: Objeto Json que contiene los datos del usuario
## Usuario -> crearUsuario -> Z
## @return HTML: html que contiene el resultado obtenido en la insercion exito=1, fallo=-1
##/
@app.route('/crearUsuario', methods=['POST'])
def crearUsuario():
    data = request.get_json()
    #print(data)
    res = logicaNegocio.crearUsuario(data)
    
    return '''<h1>Resultado:  {} </h1>'''.format(res)

##/
## http://{ip_server}/editarUsuario
## Peticion que permite editar un usuario
## @param Usuario: Objeto Json que contiene los datos del usuario
## Usuario -> editarUsuario -> Z
## @return: Entero que indica si todo ha ido bien o no
##/
@app.route('/editarUsuario', methods=['PUT'])
def editarUsuario():
    data = request.get_json()
    #print(data)
    res = logicaNegocio.editarUsuario(data)
    
    return '''<h1>Resultado:  {} </h1>'''.format(res)

## Inicializacion del servidor
if __name__=='__main__':
        app.run(host='0.0.0.0', debug=True)
