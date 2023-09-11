""" Se importa desde distintas carpetas funciones y variables que se hayan creado ahí.  """
from Data.data import * # Desde la carpeta "Data" se importan todos los códigos del archivo "data".
from BD.baseDatos import * # Desde la carpeta "BD" se importan todos los códigos del archivo "baseDatos".
from sklearn.linear_model import LinearRegression # Se importa la librería "LinearRegression" que es usada para generar regresiones lineales. 
from Gráficas.grafica import * # Desde la carpeta "BD" se importan todos los códigos del archivo "grafica".
import pandas as pd # Se importa la biblioteca "pandas" que se encarga del análisis y manipulación de datos.

""" Análisis de datos (Sensor 1) """

""" Se llama a la función “dataTeorico()” que comprende dos valores, los cuales van a ser asignados a las variables 
"dataTeoricoEsfuerzo" y "dataTeoricoDeformacion", donde la infomación viene siendo importada de "Data.data". """
dataTeoricoEsfuerzo, dataTeoricoDeformacion = dataTeorico() 

""" Modelo de regresión """

data_list = lecturaDatos() # Se define la variable "data_list" que comprende la función "lecturaDatos(), llamada desde "BD.baseDatos".
data_real = pd.DataFrame(data_list) # Se define la variable "data_real" que crea una base de datos de la información suministrada en la variable "data_list".
data_real_fit = data_real
X = data_real_fit['Esfuerzo (kN)'].values.reshape(-1, 1)
y = data_real_fit['Deformación (mm)'].values.reshape(-1, 1)
x_lim = data_real['Esfuerzo (kN)'].iloc[-1]
y_lim = data_real['Deformación (mm)'].iloc[-1]
model = LinearRegression()
model.fit(X, y)
prediction = round(model.predict(np.array([3000]).reshape(-1, 1))[0][0],1)
print('La predicción a 3000 kN es de: ', prediction ,'mm')


dataRealEsfuerzo = data_real['Esfuerzo (kN)']
dataRealDeformacion = data_real['Deformación (mm)']

#realizamos la lectura de las gráficas
gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion)
gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion)
gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model)


# Sensor 2

dataTeoricoEsfuerzo, dataTeoricoDeformacion = dataTeorico()

#Datos de la base de datos y realizamos el modelo
data_list2 = lecturaDatos2()
data_real2 = pd.DataFrame(data_list2)
data_real_fit = data_real2
X = data_real_fit['Esfuerzo (kN)'].values.reshape(-1, 1)
y = data_real_fit['Deformación (mm)'].values.reshape(-1, 1)
x_lim = data_real['Esfuerzo (kN)'].iloc[-1]
y_lim = data_real['Deformación (mm)'].iloc[-1]
model = LinearRegression()
model.fit(X, y)
prediction = round(model.predict(np.array([3000]).reshape(-1, 1))[0][0],1)
print('La predicción a 3000 kN es de: ', prediction ,'mm')


dataRealEsfuerzo = data_real2['Esfuerzo (kN)']
dataRealDeformacion = data_real2['Deformación (mm)']

#realizamos la lectura de las gráficas
gr_sin_prediccion2(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion)
gr_con_prediccion2(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion)
gr_con_prediccion2_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model)
