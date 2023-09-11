from pymongo.mongo_client import MongoClient # Importa la libreria MongoClient de la biblioteca pymongo, 
    #que se utiliza para establecer una conexión con una base de datos MongoDB.

def conexion(): # Definición de la función conexión, conecta la base de datos de mongo
    uri = "mongodb+srv://hernandezcamila1001:1234@cluster0.pn7altv.mongodb.net/?retryWrites=true&w=majority" # URI= incluye el nombre de usuario, la contraseña y la dirección del servidor, entre otros parámetros
    return MongoClient(uri) # Establece una conexión con la base de datos MongoDB y permite realizar operaciones en la base de datos

#LECTURA
""" Código necesario para crear un read en MongoDB"""
def lecturaDatos(): # Definición de la función lecturaDatos, lee los datos de la base de datos
    client = conexion() # Variable que almacena una instancia de MongoClient, establece la conexión a la base de datos
    db = client.datos_asentamientoSensores # Llama la base de datos "datos_asentamientoSensores" almacenados en mongo, permite hacer operaciones en la bd
    data_list = [] # Variable tipo lista, almacena los datos leidos de la base de datos
    for data_real_bd in db.sensor1.find(): # Inicia un bucle que recorre todos los documentos en la colección "sensor1" de la base de datos seleccionada.
        data_list.append(data_real_bd) # En cada iteración del bucle, se agrega el documento actual a la lista data_list, acumula todos los documentos en la lista.
    return data_list # Devuelve la lista "data_list" que contiene los datos leidos de la base de datos


def lecturaDatos2(): # Definición de la función lecturaDatos, lee los datos de la base de datos
    client = conexion() # Variable que almacena una instancia de MongoClient, establece la conexión a la base de datos
    db = client.datos_asentamientoSensores # Llama la base de datos "datos_asentamientoSensores" almacenados en mongo, permite hacer operaciones en la bd
    data_list2 = [] # Variable tipo lista, almacena los datos leidos de la base de datos
    for data_real_bd in db.sensor2.find(): # Inicia un bucle que recorre todos los documentos en la colección "sensor2" de la base de datos seleccionada.
        data_list2.append(data_real_bd) # En cada iteración del bucle, se agrega el documento actual a la lista data_list, acumula todos los documentos en la lista.
    return data_list2 # Devuelve la lista "data_list" que contiene los datos leidos de la base de datos
