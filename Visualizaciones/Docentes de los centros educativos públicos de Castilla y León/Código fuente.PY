#DOCENTES DE LOS CENTROS PÚBLICOS DE CASTILLA Y LEÓN

"""
Pasos que se seguirán en este código
1. Carga de datos. 
2. Crear tablas de datos de trabajo. 
3. Transformación de tipos de variables.
4. Generación del archivo de entrada para Elastic con los datos transformados. 
 
"""

#Tratamiento de datos

# Instalación y carga de librerías. 
# Importamos las librerías de Python necesarias para la carga y tratamiento de datos


import pandas as pd  # Proporciona herramientas de análisis y manipulación de 
                     # datos de alto rendimiento
import csv as csv # Librería que permite cargar datasets en formato csv


#1. Carga y limpieza de datos

# Carga de datasets 

"""
Cargamos los datasets, debemos indicarle el "delimiter" que en este caso es, que 
el dataset presenta una cabecera en la primera fila con "header" y debemos 
indicarle el comando "encoding" para que entienda adecuadamente el formato UTF-8.
 
Para ello debemos descargar los conjuntos de datos de GitHub y colocarlos en tu 
directorio de trabajo. 

Plantillas jurídicas de los centros educativos públicos de Castilla y León de todos 
los cuerpos de profesorado, a excepción de maestros.

"""


# Plantillas jurídicas de los centros educativos públicos de Castilla y León de todos 
# los cuerpos de profesorado, a excepción de maestros.

file = "Conjuntos de datos/PLANTILLA_PES_Y_OTROS_CUERPOS.csv"
docentes = pd.read_csv(file,
                   delimiter=';', 
                   header=0, 
                   encoding ='latin-1'
                  )
docentes.head(3)

# Dataset de las matriculaciones de alumnos en centros educativos durante el curso 
# académico 2019-2020

with open('Conjuntos de datos/alumnos.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('Conjuntos de datos/matriculaciones.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)
        
alumnos = pd.read_csv("Conjuntos de datos/matriculaciones.csv",
                   delimiter=',',
                   names=["Municipio", "Matriculaciones"],
                   encoding ='latin-1'
                  )
alumnos.head(1)     



# En la Columna 'Municipio' del dataset de alumnos, tenemos tanto el código del
# municipio como el nombre del mismo, por tanto debemos dividir esta columna en dos.  

separado = alumnos["Municipio"].str.split(" ", n=1, expand=True)
alumnos['Codigo_municipio'] = separado[0]
alumnos['Municipio'] = separado [1]
alumnos.head(1)

print('El número de filas y de columnas del dataset de docentes es:', docentes.shape)
print('Los nombres de las columnas del dataset de docentes son:', docentes.columns)

print('El número de filas y de columnas del dataset de alumnos es:', alumnos.shape)
print('Los nombres de las columnas del dataset de alumnos son:', alumnos.columns)

# Muchas de las columnas presentan nombres con espacios. Esto puede ser un problema 
# a la hora de trabajar con estas variables, para evitarlos procedemos a cambiar los 
# nombres de las variables. 

docentes.columns = ['Codigo_centro', 'Denominacion_centro', 'Provincia', 
                'Municipio', 'Localidad', "Codigo_cuerpo", 
                'Denominacion_cuerpo', 'Codigo_especialidad', 
                'Denominacion_especialidad', 'Plantilla']
docentes.columns

# 2. Crear tablas de datos de trabajo

# Una vez que tenemos ambas tablas, con las variables adecuadas, creamos una nueva 
# tabla uniendo ambos conjuntos de datos. La variable de unión será "Localidad" en el 
# dataset de docentes y  "Municipio" en el conjunto de datos de alumnos.

docentes_alumnos = pd.merge(docentes, alumnos, left_on = 'Localidad', right_on = "Municipio")
docentes_alumnos.head(5)

print('Número de filas y columnas:', docentes_alumnos.shape)
print('Los nombres de las columnas son:', docentes_alumnos.columns)

# Resumen de la tabla

docentes_alumnos.info()

# 3. Transformación de tipos de variables.

docentes_alumnos.Codigo_centro = docentes_alumnos.Codigo_centro.astype("object")
docentes_alumnos.Codigo_cuerpo = docentes_alumnos.Codigo_cuerpo.astype("object")
docentes_alumnos.Codigo_especialidad = docentes_alumnos.Codigo_especialidad.astype("object")

# Resumen de las variables núméricas

docentes_alumnos.describe()

# 4. Generación del archivo de entrada para Elastic con los datos transformados.

#Una vez que tenemos el dataset con las variables que nos interesa graficar, lo  
# guardaremos en una carpeta de nuestra elección para usarlo en otras herramientas 
# de análisis o visualización. Lo guardaremos en formato csv UTF8 
# (Formato de Transformación Unicode) para que los caracteres sean identificados de 
# manera correcta por cualquier herramienta. 

df = pd.DataFrame(docentes_alumnos)
filename = 'docentes_alumnos.csv'
df.to_csv(filename, index=False, encoding='utf-8')

df = pd.DataFrame(alumnos)
filename = 'alumnos'
df.to_csv(filename, index = False, encoding = 'utf-8') 

