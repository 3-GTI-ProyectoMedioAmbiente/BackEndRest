from flask import Flask,request
from logica.logicaNegocio import LogicaNegocio
from flask_cors import CORS

import json


#-----------------------------------------------------------------------------------
# @author: Juan Carlos Hernandez Ramirez
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
## http://{ip_server}/obtenerTodasMedicionesPorFecha
## Peticion que devueve las medciones de un dia en concreto
## @return json: JSON que contendra las ultimas mediciones 
## getLastMeasures-> [Medicion]
##/
@app.route('/obtenerTodasMedicionesPorFecha')
def obtenerTodasMedicionesPorFecha():
    fecha = request.args.get('fecha')
    data = logicaNegocio.obtenerTodasMedicionesPorFecha(fecha)
    return json.dumps(data,indent=4)


##/
## http://{ip_server}/loginUsuario
## Peticion que devueve un usuario dependiendo del correo y la contraseña
## @return json: JSON que contendra el usuario
## mail:Texto,contrasenya:Texto -> loginUsuario -> Usuario
##/
@app.route('/loginUsuario')
def loginUsuario():
    data = request.get_json()
    #print(data)
    res = logicaNegocio.loginUsuario(data["mail"],data["contrasenya"])
    
    return '''<h1>Resultado:  {} </h1>'''.format(res)

## Inicializacion del servidor
if __name__=='__main__':
        app.run(host='0.0.0.0', debug=True)
