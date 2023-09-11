from pymongo.mongo_client import MongoClient

def conexion(): 
    uri = "mongodb+srv://hernandezcamila1001:1234@cluster0.pn7altv.mongodb.net/?retryWrites=true&w=majority"
    return MongoClient(uri) 

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
