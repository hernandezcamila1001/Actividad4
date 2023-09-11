""" Se importa la librería MongoClient que permite establecer una conexión con el servidor MongoDB. """
from pymongo.mongo_client import MongoClient

"""Conexión con la base de datos."""
def conexion(): # Se crea la función "conexion" que establece y devuelve una conexión con los datos de MongoDB.
    uri = "mongodb+srv://hernandezcamila1001:1234@cluster0.pn7altv.mongodb.net/?retryWrites=true&w=majority" # URI de conexión.
    return MongoClient(uri) # Se retorna la conexión que se crea con la base de datos de MongoDB.

#READ
""" Código necesario para crear un read en MongoDB"""
def lecturaDatos():
    client = conexion()
    db = client.datos_asentamientoSensores
    data_list = []
    for data_real_bd in db.sensor1.find():
        data_list.append(data_real_bd)
    return data_list 


def lecturaDatos2():
    client = conexion()
    db = client.datos_asentamientoSensores
    data_list2 = []
    for data_real_bd in db.sensor2.find():
        data_list2.append(data_real_bd)
    return data_list2 