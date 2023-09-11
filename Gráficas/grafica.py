import matplotlib.pyplot as plt # Importación de biblioteca de visualización que se utiliza para crear gráficos y visualizaciones de datos
import numpy as np #  Importación de biblioteca que proporciona soporte para matrices multidimensionales y operaciones matemáticas de alto rendimiento

# Sensor 1
# Define la función "gr_con_prediccion", que guarda los arguemntos como limites en 'x' y 'y'y otros argumentos
def gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion):
    
    plt.figure(figsize=(15, 6)) # Crea una nueva figura de gráfico con un tamaño específico de 15 unidades de ancho y 6 unidades de alto.
    plt.plot(dataTeoricoEsfuerzo, dataTeoricoDeformacion) # Traza una línea que conecta los puntos definidos por dataTeoricoEsfuerzo en el eje x y dataTeoricoDeformacion en el eje y
    plt.scatter(dataRealEsfuerzo, dataRealDeformacion, color='red') # Se utiliza para crear un diagrama de dispersión (scatter plot) en una visualización gráfica, con trazo rojo
    plt.xlabel('Esfuerzo [kN]') # Etiqueta el eje x con la leyenda 'Esfuerzo [kN]' 
    plt.ylabel('Deformación [mm]') # Etiqueta el eje y con la leyenda 'Deformación [mm]'
    plt.title('Gráfica 2: teórico versus real [ZOOM] (Sensor 1)') # Se le asigna un nombre al titulo de la gráfica
    plt.xlim(0, x_lim) # Establece los límites del gráfico en los ejes x, limitando la visualización de los datos dentro de los valores indicados
    plt.ylim(0, y_lim) # Establece los límites del gráfico en los ejes y, limitando la visualización de los datos dentro de los valores indicados
    plt.grid() # Agrega cuadricula al gráfico
    plt.gca().invert_yaxis() # Invierte el eje y del gráfico para que los valores más bajos estén en la parte superior y los valores más altos en la parte inferior
    plt.show() # Muestra el diagrama de dispersión basico de los puntos generados

def gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model):
  plt.figure(figsize=(15, 6))
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion)
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red')
  plt.plot(np.linspace(0,1000).reshape(-1,1),model.predict(np.linspace(0,1000).reshape(-1,1)),'m')
  plt.scatter(3000 , prediction, color='green')
  plt.xlabel('Esfuerzo [kN]')
  plt.ylabel('Deformación [mm]')
  plt.title('Gráfica 3: Predicción a una carga de 3000 kN (Sensor 1)')
  plt.xlim(0, 3000)
  plt.ylim(0, 45)
  plt.grid()
  plt.gca().invert_yaxis()
  plt.show()

def gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion):
  plt.figure(figsize=(15, 6))
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion)
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red')
  plt.xlabel('Esfuerzo [kN]')
  plt.ylabel('Deformación [mm]')
  plt.title('Gráfica 1: teórico versus real (Sensor 1)')
  plt.grid()
  plt.gca().invert_yaxis()
  plt.show()


# Sensor 2

def gr_con_prediccion2(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion):
    
    
    plt.figure(figsize=(15, 6))
    plt.plot(dataTeoricoEsfuerzo, dataTeoricoDeformacion)
    plt.scatter(dataRealEsfuerzo, dataRealDeformacion, color='red')
    plt.xlabel('Esfuerzo [kN]')
    plt.ylabel('Deformación [mm]')
    plt.title('Gráfica 2: teórico versus real [ZOOM] (Sensor 2)')
    plt.xlim(0, x_lim)
    plt.ylim(0, y_lim)
    plt.grid()
    plt.gca().invert_yaxis()
    plt.show()

def gr_con_prediccion2_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model):
  plt.figure(figsize=(15, 6))
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion)
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red')
  plt.plot(np.linspace(0,1000).reshape(-1,1),model.predict(np.linspace(0,1000).reshape(-1,1)),'m')
  plt.scatter(3000 , prediction, color='green')
  plt.xlabel('Esfuerzo [kN]')
  plt.ylabel('Deformación [mm]')
  plt.title('Gráfica 3: Predicción a una carga de 3000 kN (Sensor 2)')
  plt.xlim(0, 3000)
  plt.ylim(0, 45)
  plt.grid()
  plt.gca().invert_yaxis()
  plt.show()

def gr_sin_prediccion2(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion):
  plt.figure(figsize=(15, 6))
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion)
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red')
  plt.xlabel('Esfuerzo [kN]')
  plt.ylabel('Deformación [mm]')
  plt.title('Gráfica 1: teórico versus real (Sensor 2)')
  plt.grid()
  plt.gca().invert_yaxis()
  plt.show()
