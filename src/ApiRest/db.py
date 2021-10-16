from flask_mysqldb import MySQL
class Database:
    def __init__(self, app):
        self.mysql = MySQL(app)

    def insertMediciones(self,mediciones):
        for medicion in mediciones:
            db = self.mysql.connection.cursor()
            db.execute("INSERT INTO mediciones (medicion,fecha,hora,localizacion_lat,localizacion_lon) VALUES ({},'{}','{}',{},{});".format(
            medicion['medicion'],medicion['fecha'],medicion['hora'],medicion['localizacion_lat'], medicion['localizacion_lon'] ))
        self.mysql.connection.commit()

    def getTodasLasMediciones(self):
        db = self.mysql.connection.cursor()
        db.execute("Select * from mediciones")
        data = db.fetchall()
        return data

    def getUltimasMediciones(self,cuantos):
        db = self.mysql.connection.cursor()
        db.execute("Select * from mediciones limit {}".format(cuantos))
        data = db.fetchall()
        return data

