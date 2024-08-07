# Turismo en España: analizando los flujos de turistas nacionales mediante visualizaciones interactivas 

En este ejercicio, exploraremos los flujos de turistas a nivel nacional, creando visualizaciones de los turistas que se mueven entre las comunidades autónomas (CCAA) y provincias.

## Conjunto de datos 
El conjunto de datos abiertos utilizado contiene información sobre los flujos de turistas en España a nivel de CCAA y provincias, indicando también los valores totales a nivel nacional. El conjunto de datos ha sido publicado por el Instituto Nacional de Estadística, a través de varios tipos de ficheros. Para el presente ejercicio utilizamos únicamente el fichero .csv separado por “;”. Los datos datan de julio de 2019 a marzo de 2024 (a la hora de redactar este ejercicio) y se actualizan mensualmente. 

[Número de turistas por CCAA y provincia de destino desagregados por PROVINCIA de origen](https://datos.gob.es/es/catalogo/ea0010587-numero-de-turistas-por-ccaa-y-provincia-de-destino-desagregados-por-provincia-de-origen-tmov-identificador-api-53267)

## Herramientas analíticas
Para la limpieza de los datos y la creación de las visualizaciones se ha utilizado el lenguaje de programación Python. El código creado para este ejercicio se pone a disposición del lector a través de un notebook de Google Colab.
Las librerías de Python que utilizaremos para llevar a cabo el ejercicio son:
-	[pandas](https://pandas.pydata.org/pandas-docs/stable/index.html) que es una librería que se utiliza para el análisis y manipulación de datos
-	[holoviews](https://holoviews.org/index.html) que es una librería que permite crear visualizaciones interactivas, combinando las funcionalidades de otras librerías como Bokeh y Matplotlib.



