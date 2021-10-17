from flask import Flask, render_template, request,redirect,url_for
from logicaNegocio import LogicaNegocio
import json

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_mediciones'

logicaNegocio = LogicaNegocio(app) 

@app.route('/')
def getAllMeasuresWeb():
    dataJson = logicaNegocio.getTodasLasMediciones()
    data = dataJson['mediciones']
    return render_template('insert.html', mediciones=data)

@app.route('/getLastMeasuresWeb',methods=['POST'])
def ultimas_mediciones_web():
    if request.method == 'POST':
        cuantos = request.form['cuantos']
        if cuantos:
            data = logicaNegocio.getUltimasMediciones(cuantos)
            return render_template('insert.html', mediciones=data)
        else:
            return redirect(url_for('getAllMeasuresWeb'))

#Metodos rest
@app.route('/insertMedicionJson', methods=['POST'])
def insertMedicionJson():
    data=request.get_json()
    res = logicaNegocio.insertMediciones(data['mediciones'])
    return '''<h1>Resultado:  {} </h1>'''.format(res)

@app.route('/getAllMeasures')
def getAllMeasures():
    data = logicaNegocio.getTodasLasMediciones()
    return json.dumps(data, indent=4)

@app.route('/getLastMeasures')
def getLastMeasures():
    cuantos = request.args.get('cuantos')
    data = logicaNegocio.getUltimasMediciones(cuantos)
    return json.dumps(data,indent=4)


if __name__=='__main__':
        app.run(debug=True, port=4000)
