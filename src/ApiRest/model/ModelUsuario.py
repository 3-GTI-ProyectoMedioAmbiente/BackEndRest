import json
#
#    ModelUsuario.py
#    Autor: Sergi Sirvent Sempere
#    Fecha: 12/2021
#    Este archivo se encarga de contener el modelo de la clase usuario
#

class Usuario:

    ##/
    ## Constructor
    ## @param self: objeto que contiene los propios metods y atributos de la clase
    ## @return json: Objeto Json que tendra el objeto Usuario en formato JSON
    ## toJson()->json
    ##/
    def __init__(self,id,mail,nombre,apellidos,isAutobusero,edad,matricula,telefono,password,id_sensor):
        self.id = id
        self.mail = mail
        self.nombre = nombre
        self.apellidos = apellidos
        self.isAutobusero = isAutobusero
        self.edad = edad
        self.matricula = matricula
        self.telefono = telefono
        self.password = password
        self.id_sensor = id_sensor
    
    ##/
    ##toJson()
    ## Metodo que genera un objeto JSON a partir de los atributos de la clase
    ## @param self: objeto que contiene los propios metods de la clase
    ## @return json: Objeto Json que tendra el objeto Usuario en formato JSON
    ## toJson()->json
    ##/
    def toJson(self):
        json = {
            "id": self.id,
            "mail": self.mail,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "isAutobusero": self.isAutobusero,
            "edad": self.edad,
            "matricula": self.matricula,
            "telefono": self.telefono,
            "password": self.password,
            "id_sensor":self.id_sensor
            }
        return json

