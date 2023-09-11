import pandas as pd # Se importa la biblioteca "pandas" que se encarga del análisis y manipulación de datos.

# Importar datos del csv
# Nombra una variable que contiene una tabla, extraida desde la dirección indicada
data_teorico = pd.read_csv(r"C:\Users\Usuario\OneDrive\Escritorio\Clase 1\Actividad4\Data\Data ingeniero.csv")

#Código general
def dataTeorico(): # Define la función dataTeorico
    dataTeoricoEsfuerzo = data_teorico['Esfuerzo[kN]'] # Creación de variable, se le asigna el valor de la columna Esfuerzo de la variable data_teorico
    dataTeoricoDeformacion = data_teorico['Deformacion[mm]'] # Creación de variable, se le asigna el valor de la columna Deformación de la variable data_teorico
    return dataTeoricoEsfuerzo, dataTeoricoDeformacion # Devuelve dos valores: dataTeoricoEsfuerzo y dataTeoricoDeformacion


