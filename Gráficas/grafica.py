import matplotlib.pyplot as plt # Importación de biblioteca de visualización que se utiliza para crear gráficos y visualizaciones de datos
import numpy as np #  Importación de biblioteca que proporciona soporte para matrices multidimensionales y operaciones matemáticas de alto rendimiento

# Sensor 1
# Define la función "gr_con_prediccion", que guarda los argumentos como limites en 'x' y 'y'y otros argumentos, cada argumento es una variable que se utilizará dentro de la función.
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

# Define la función "gr_con_prediccion_3000", que guarda los argumentos como prediction,dataTeoricoEsfuerzoy otros argumentos, cada argumento es una variable que se utilizará dentro de la función.
def gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model):
  plt.figure(figsize=(15, 6)) # Crea una nueva figura de gráfico con un tamaño específico de 15 unidades de ancho y 6 unidades de alto.
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) # Traza una línea que conecta los puntos definidos por dataTeoricoEsfuerzo en el eje x y dataTeoricoDeformacion en el eje y
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red') # Se utiliza para crear un diagrama de dispersión (scatter plot) en una visualización gráfica, con trazo rojo
  plt.plot(np.linspace(0,1000).reshape(-1,1),model.predict(np.linspace(0,1000).reshape(-1,1)),'m') 
    """Trazar una serie de puntos en un gráfico, crea una secuencia de números desde 0 hasta 1000, se cambia la forma de la secuencia 
    generada por np.linspace para que tenga una sola columna de datos, se hace una predicción utilizando el modelo de 
    regresion lineal almacenado en la variable model y se especifica el estilo y el color magenta de la línea del gráfico. """
  plt.scatter(3000 , prediction, color='green') # Agrega un punto en el gráfico, con coordenadas (3000 en eje x y el valor de predicción en el ejey), se le asigna el color verde
  plt.xlabel('Esfuerzo [kN]') # Etiqueta el eje x con la leyenda 'Esfuerzo [kN]' 
  plt.ylabel('Deformación [mm]') # Etiqueta el eje y con la leyenda 'Deformación [mm]'
  plt.title('Gráfica 3: Predicción a una carga de 3000 kN (Sensor 1)') # Se le asigna un nombre al titulo de la gráfica
  plt.xlim(0, 3000) # Establece los límites del gráfico en los ejes x, limitando la visualización de los datos dentro de los valores (0, 3000)
  plt.ylim(0, 45) # Establece los límites del gráfico en los ejes x, limitando la visualización de los datos dentro de los valores (0, 45)
  plt.grid() # Agrega cuadricula al gráfico
  plt.gca().invert_yaxis() # Invierte el eje y del gráfico para que los valores más bajos estén en la parte superior y los valores más altos en la parte inferior
  plt.show() # Muestra el diagrama de dispersión basico de los puntos generados

# Define la función "gr_con_prediccion", que guarda los argumentos como dataTeoricoEsfuerzo,dataTeoricoDeformacion y otros argumentos, cada argumento es una variable que se utilizará dentro de la función.
def gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion):
  plt.figure(figsize=(15, 6)) # Crea una nueva figura de gráfico con un tamaño específico de 15 unidades de ancho y 6 unidades de alto.
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) # Traza una línea que conecta los puntos definidos por dataTeoricoEsfuerzo en el eje x y dataTeoricoDeformacion en el eje y
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red') # Se utiliza para crear un diagrama de dispersión (scatter plot) en una visualización gráfica, con trazo rojo
  plt.xlabel('Esfuerzo [kN]') # Etiqueta el eje x con la leyenda 'Esfuerzo [kN]' 
  plt.ylabel('Deformación [mm]') # Etiqueta el eje y con la leyenda 'Deformación [mm]'
  plt.title('Gráfica 1: teórico versus real (Sensor 1)') # Se le asigna un nombre al titulo de la gráfica
  plt.grid() # Agrega cuadricula al gráfico
  plt.gca().invert_yaxis() # Invierte el eje y del gráfico para que los valores más bajos estén en la parte superior y los valores más altos en la parte inferior
  plt.show() # Muestra el diagrama de dispersión basico de los puntos generados


# Sensor 2
# Define la función "gr_con_prediccion", que guarda los argumentos como limites en 'x' y 'y'y otros argumentos, cada argumento es una variable que se utilizará dentro de la función.
def gr_con_prediccion2(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion):
    
    plt.figure(figsize=(15, 6)) # Crea una nueva figura de gráfico con un tamaño específico de 15 unidades de ancho y 6 unidades de alto.
    plt.plot(dataTeoricoEsfuerzo, dataTeoricoDeformacion) # Traza una línea que conecta los puntos definidos por dataTeoricoEsfuerzo en el eje x y dataTeoricoDeformacion en el eje y
    plt.scatter(dataRealEsfuerzo, dataRealDeformacion, color='red') # Se utiliza para crear un diagrama de dispersión (scatter plot) en una visualización gráfica, con trazo rojo
    plt.xlabel('Esfuerzo [kN]') # Etiqueta el eje x con la leyenda 'Esfuerzo [kN]' 
    plt.ylabel('Deformación [mm]') # Etiqueta el eje y con la leyenda 'Deformación [mm]'
    plt.title('Gráfica 2: teórico versus real [ZOOM] (Sensor 2)') # Se le asigna un nombre al titulo de la gráfica
    plt.xlim(0, x_lim) # Establece los límites del gráfico en los ejes x, limitando la visualización de los datos dentro de los valores indicados
    plt.ylim(0, y_lim) # Establece los límites del gráfico en los ejes y, limitando la visualización de los datos dentro de los valores indicados
    plt.grid() # Agrega cuadricula al gráfico
    plt.gca().invert_yaxis() # Invierte el eje y del gráfico para que los valores más bajos estén en la parte superior y los valores más altos en la parte inferior
    plt.show() # Muestra el diagrama de dispersión basico de los puntos generados

# Define la función "gr_con_prediccion_3000", que guarda los argumentos como prediction,dataTeoricoEsfuerzoy otros argumentos, cada argumento es una variable que se utilizará dentro de la función.
def gr_con_prediccion2_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model):
  plt.figure(figsize=(15, 6)) # Crea una nueva figura de gráfico con un tamaño específico de 15 unidades de ancho y 6 unidades de alto.
  plt.plot(dataTeoricoEsfuerzo , dataTeoricoDeformacion) # Traza una línea que conecta los puntos definidos por dataTeoricoEsfuerzo en el eje x y dataTeoricoDeformacion en el eje y
  plt.scatter(dataRealEsfuerzo , dataRealDeformacion, color='red') # Se utiliza para crear un diagrama de dispersión (scatter plot) en una visualización gráfica, con trazo rojo
  plt.plot(np.linspace(0,1000).reshape(-1,1),model.predict(np.linspace(0,1000).reshape(-1,1)),'m')
    """Trazar una serie de puntos en un gráfico, crea una secuencia de números desde 0 hasta 1000, se cambia la forma de la secuencia 
    generada por np.linspace para que tenga una sola columna de datos, se hace una predicción utilizando el modelo de 
    regresion lineal almacenado en la variable model y se especifica el estilo y el color magenta de la línea del gráfico. """
  plt.scatter(3000 , prediction, color='green') #  Agrega un punto en el gráfico, con coordenadas (3000 en eje x y el valor de predicción en el ejey), se le asigna el color verde
  plt.xlabel('Esfuerzo [kN]') # Etiqueta el eje x con la leyenda 'Esfuerzo [kN]' 
  plt.ylabel('Deformación [mm]') # Etiqueta el eje y con la leyenda 'Deformación [mm]'
  plt.title('Gráfica 3: Predicción a una carga de 3000 kN (Sensor 2)') # Se le asigna un nombre al titulo de la gráfica
  plt.xlim(0, 3000) # Establece los límites del gráfico en los ejes x, limitando la visualización de los datos dentro de los valores (0, 3000)
  plt.ylim(0, 45) # Establece los límites del gráfico en los ejes x, limitando la visualización de los datos dentro de los valores (0, 45)
  plt.grid() # Agrega cuadricula al gráfico # Se le asigna un nombre al titulo de la gráfica
  plt.gca().invert_yaxis() # Invierte el eje y del gráfico para que los valores más bajos estén en la parte superior y los valores más altos en la parte inferior
  plt.show() # Muestra el diagrama de dispersión basico de los puntos generados

# Define la función "gr_con_prediccion", que guarda los argumentos como dataTeoricoEsfuerzo,dataTeoricoDeformacion y otros argumentos, cada argumento es una variable que se utilizará dentro de la función.
def gr_sin_prediccion2(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion):
  plt.figure(figsize=(15, 6)) # Crea una nueva figura de gráfico con un tamaño específico de 15 unidades de ancho y 6 unidades de alto.
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) # Traza una línea que conecta los puntos definidos por dataTeoricoEsfuerzo en el eje x y dataTeoricoDeformacion en el eje y
  plt.scatter(dataRealEsfuerzo , dataRealDeformacion, color='red') # Se utiliza para crear un diagrama de dispersión (scatter plot) en una visualización gráfica, con trazo rojo
  plt.xlabel('Esfuerzo [kN]') # Etiqueta el eje x con la leyenda 'Esfuerzo [kN]' 
  plt.ylabel('Deformación [mm]') # Etiqueta el eje y con la leyenda 'Deformación [mm]'
  plt.title('Gráfica 1: teórico versus real (Sensor 2)') # Se le asigna un nombre al titulo de la gráfica
  plt.grid() # Agrega cuadricula al gráfico
  plt.gca().invert_yaxis() # Invierte el eje y del gráfico para que los valores más bajos estén en la parte superior y los valores más altos en la parte inferior
  plt.show() # Muestra el diagrama de dispersión basico de los puntos generados
