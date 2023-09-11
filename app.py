""" Se importa desde distintas carpetas funciones y variables que se hayan creado ahí.  """
from Data.data import * # Desde la carpeta "Data" se importan todos los códigos del archivo "data".
from BD.baseDatos import * # Desde la carpeta "BD" se importan todos los códigos del archivo "baseDatos".
from sklearn.linear_model import LinearRegression
from Gráficas.grafica import *
import pandas as pd

# Sensor 1

dataTeoricoEsfuerzo, dataTeoricoDeformacion = dataTeorico()

#Datos de la base de datos y realizamos el modelo
data_list = lecturaDatos()
data_real = pd.DataFrame(data_list)
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
