from flask import Flask, render_template, request,redirect,url_for
from logicaNegocio import LogicaNegocio
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

logicaNegocio = LogicaNegocio(app) 

##/
## http://{ip_server}/
## Ruta principal de la pagina web que mostrara todas las mediciones
## @return plantillaWeb: genera el codigo html de la pagina web a partir de las medidicones obtenidas en la BD 
## getAllMeasuresWeb-> HTML
##/
@app.route('/')
def getAllMeasuresWeb():
    dataJson = logicaNegocio.obtenerTodasLasMediciones()
    data = dataJson['mediciones']
    return render_template('insert.html', mediciones=data)

##/
## http://{ip_server}/getLastMeasuresWeb
## Ruta principal de la pagina web que mostrara todas las mediciones
## @return plantillaWeb: genera el codigo html de la pagina web a partir de las medidicones obtenidas en la BD 
## getAllMeasuresWeb-> HTML
##/
@app.route('/getLastMeasuresWeb',methods=['POST'])
def ultimas_mediciones_web():
    if request.method == 'POST':
        cuantos = request.form['cuantos']
        if cuantos:
            dataJson = logicaNegocio.obtenerLasUltimasMediciones(cuantos)
            data = dataJson['mediciones']
            return render_template('insert.html', mediciones=data)
        else:
            return redirect(url_for('getAllMeasuresWeb'))

#------------ Metodos API REST ----------

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
## http://{ip_server}/getAllMeasures
## Peticion que devueve todas las mediciones JSON
## @return json: JSON que contendra todas las mediciones 
## getAllMeasures-> [Medicion]
##/
@app.route('/getAllMeasures')
def getAllMeasures():
    data = logicaNegocio.obtenerTodasLasMediciones()
    return json.dumps(data, indent=4)

##/
## http://{ip_server}/getLastMeasures
## Peticion que devueve las utlimas mediciones JSON
## @return json: JSON que contendra las ultimas mediciones 
## getLastMeasures-> [Medicion]
##/
@app.route('/getLastMeasures')
def getLastMeasures():
    cuantos = request.args.get('cuantos')
    data = logicaNegocio.obtenerLasUltimasMediciones(cuantos)
    return json.dumps(data,indent=4)

## Inicializacion del servidor
if __name__=='__main__':
        app.run(host='0.0.0.0', debug=True, port=8080)
