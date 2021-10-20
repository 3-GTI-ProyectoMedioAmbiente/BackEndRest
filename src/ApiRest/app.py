from flask import Flask, render_template, request,redirect,url_for
from logicaNegocio import LogicaNegocio
import json

#-----------------------------------------------------------------------------------
# @author: Juan Carlos Hernandez Ramirez
#Fecha: 14/10/2021
#-----------------------------------------------------------------------------------
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_mediciones'

logicaNegocio = LogicaNegocio(app) 

## Peticion para gestionar el muestreo de todas las mediciones en la web
@app.route('/')
def getAllMeasuresWeb():
    dataJson = logicaNegocio.getTodasLasMediciones()
    data = dataJson['mediciones']
    return render_template('insert.html', mediciones=data)

## Peticion para gestionar el muestreo de las ultimas mediciones en la web
@app.route('/getLastMeasuresWeb',methods=['POST'])
def ultimas_mediciones_web():
    if request.method == 'POST':
        cuantos = request.form['cuantos']
        if cuantos:
            dataJson = logicaNegocio.getUltimasMediciones(cuantos)
            data = dataJson['mediciones']
            return render_template('insert.html', mediciones=data)
        else:
            return redirect(url_for('getAllMeasuresWeb'))

#------------ Metodos API REST ----------

## Peticion que controla la insercion de datos mediante JSON
@app.route('/insertMedicionJson', methods=['POST'])
def insertMedicionJson():
    data=request.get_json()
    res = logicaNegocio.insertMediciones(data['mediciones'])
    return '''<h1>Resultado:  {} </h1>'''.format(res)

## Peticion que devuelve todas las mediciones mediante en JSON
@app.route('/getAllMeasures')
def getAllMeasures():
    data = logicaNegocio.getTodasLasMediciones()
    return json.dumps(data, indent=4)

## Peticion que devuelve solo las ultimas medidas en JSON, segun lo que se espicifique en la URL
@app.route('/getLastMeasures')
def getLastMeasures():
    cuantos = request.args.get('cuantos')
    data = logicaNegocio.getUltimasMediciones(cuantos)
    return json.dumps(data,indent=4)

## Inicializacion del servidor
if __name__=='__main__':
        app.run(host='0.0.0.0', debug=True, port=8080)
