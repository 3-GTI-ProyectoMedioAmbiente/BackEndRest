from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_mediciones'
mysql = MySQL(app)

@app.route('/')
def Index():
    db = mysql.connection.cursor()
    db.execute("Select * from mediciones")
    data = db.fetchall()
    return render_template('insert.html', mediciones=data)

@app.route('/add_medicion',methods=['POST'])
def add_medicion():
    if request.method == 'POST':
        medicion = request.form['medicion']
        db = mysql.connection.cursor()
        db.execute("INSERT INTO mediciones (medicion) VALUES (%s)", [medicion])
        mysql.connection.commit()
        return ('recibido!')

@app.route('/insertMedicionJson', methods=['POST'])
def insertMedicionJson():
    data=request.get_json()
    mediciones = data['mediciones']
    for medicion in mediciones:
        db = mysql.connection.cursor()
        db.execute("INSERT INTO mediciones (medicion,fecha,hora,localizacion_lat,localizacion_lon) VALUES ({},'{}','{}',{},{});".format(
            medicion['medicion'],medicion['fecha'],medicion['hora'],medicion['localizacion_lat'], medicion['localizacion_lon'] ))
       
    mysql.connection.commit()    
    return '''<h1>
    Se han insertado las siguientes filas:  {} </h1>'''.format(db.rowcount)
if __name__=='__main__':
        app.run(debug=True, port=4000)
