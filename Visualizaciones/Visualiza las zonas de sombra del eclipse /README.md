# Visualiza las zonas de sombra del eclipse

## Descripción

En este ejercicio realizamos la lectura y el procesado de ficheros .TIFF y .GPKG para el estudio de las zonas de sombra por relieve y por efecto del propio eclipse sobre la península ibérica con ayuda de Python. Para ello contamos con los datos que ofrece el CNIG para los eclipses solares que se producirán en la península en los próximos tres años y que son accesibles a través del catálogo de datos abiertos del portal datos.gob.es. 

El ejercicio se desarrolla en dos pasos desarrollando código en Python que encontramos en los notebooks correspondientes de Google Colab. Los dos pasos son los siguientes: 

- Zonas de sombra por relieve y orografía del terreno: donde obtendremos tanto las zonas de sombra en toda la península como en un pequeño municipio concreto para explorar todo el espectro de valores de visibilidad.
- Zonas de sombra por efecto del eclipse: donde haremos un recorrido por toda la trayectoria de la sombra sobre la península, deteniéndonos en un instante concreto para ver la forma geométrica de la proyección de la sombra sobre la superficie quasiesférica que es la Tierra.

Por último, obtendremos todos los resultados en formato .geojson para poder crear mapas en otras herramientas diferentes de Python. 

## Objetivos

El análisis en Python comprende varios objetivos, que detallamos para cada uno de los dos notebooks. En el primero realizaremos: 

- Lectura de un fichero TIF
- Cambio de sistema de coordenadas CRS
- Recorte del fichero TIF sobre una zona específica delimitada por un SHP
- Mapeado en Python del resultado
- Exportar el resultado en formato .geojson

En el segundo: 

- Lectura de un fichero .GPKG
- Unión de diferentes polígonos
- Creación de un dataframe
- Identificación de límites
- Inversión del orden de puntos
- Exportar en formato .geojson
- Mapa del resultado 

## Estructura de carpetas

En este repositorio se pueden encontrar los dos notebooks desarrollados en Google Colab para realizar los dos pasos: 

- https://colab.research.google.com/drive/1Zi7RxFQ1xk50BbNY1cBGlpIFEnlTMkvt?usp=sharing
- https://colab.research.google.com/drive/1MXBMYzS5VBkHgsgr4b1G37rLcMjMPyFt?usp=sharing 

Igualmente, en la carpeta Data se pueden encontrar los ficheros del CNIG para el eclipse de 2026 así como la información perimetral de los municipios del País Vasco. 

## Datasets utilizados 

Los datasets utilizados en este ejercicio son los siguientes: 

- **terrain_shadows_2026_3857_COG_DEF_OVERSx6_8704x8192.tif**: fichero donde se describe la visibilidad por relieve en una malla de puntos que cubre la peninsulapenínsula ibérica y la parte occidental del norte de África.
- **eclipse_levels_2026.gpkg**: fichero que contiene la duración, el oscurecimiento máximo y las curvas de penumbra proyectadas desde la Luna sobre la Tierra.  
- **10bands_2026_3857_COG.tiff**: fichero que alberga las efemérides del eclipse, tales como elevación, azimut, salida y puesta de Sol así como inicio y final del eclipse.  

## Librerías

Para poder realizar el ejercicio en Python es necesario tener instaladas previamente las siguientes librerías: 

- **rioxarray**
- **numpy** 
- **matplotlib**
- **geopandas**
- **shapely**
- **rasterio**
- **xarray**

## Conclusiones y próximos pasos 

Este ejercicio de datos nos permite pasar de un formato de datos de entornos profesionales de sistemas de información geográfica a otros formatos más manejables para poder crear nuestros propios mapas.

Asimismo, hemos visto cómo con unas pocas líneas de código podemos manipular los datos de entrada para focalizar sobre regiones de interés, seleccionar intervalos temporales determinados o customizar mapas a nuestro gusto y elección.  

Los pasos siguientes que se proponen abarcan:  

- Explorar los formatos NetCDF o KML/KMZ, también georreferenciados, para tener un mayor control y dominio sobre los formatos de datos más populares en cartografía y análisis geoespacial.  

- Comparar las características astronómicas del eclipse de 2026 con los de 2027 y 2028, también disponibles en la base de datos del CNIG disponible en el portal de datos abiertos.  

- Representar las variables que no se han mostrado en este ejercicio como las efemérides o la duración, elevación, azimut, etc... de los cuerpos celestes implicados en el eclipse.  
