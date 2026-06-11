# Crea tu mapa de magnitudes geográficas en KeplerGL

## Descripción

En este ejercicio visualizaremos información georreferenciada relacionada con la actividad sísmica de la erupción del volcán de la Palma en torno a septiembre de 2021.

En este ejercicio vamos a utilizar datos abiertos del Cabildo Insular de La Palma recopilados durante la actividad sísmica anterior y posterior a la erupción volcánica en La Palma en 2021, y que están disponibles aquí:

https://datos.gob.es/es/catalogo/l03380010-terremotos

En este dataset encontramos el registro de cada uno de los puntos en los que se detectó actividad sísmica durante esos días.

Para la creación del mapa nos centraremos en la variable asociada a la actividad sísmica: magnitud, así como la longitud y latitud de cada punto y la fecha y la hora de cada evento.

## Análisis en Python

Python nos permite hacer un sencillo procesado de los datos de entrada para seleccionar el intervalo de tiempo de interés para la visualización en Kepler. Aunque es posible utilizar el fichero original en formato .csv del portal de datos, aquí indicamos una serie de operaciones sencillas para utilizar un conjunto de datos concreto. 

1. Creación de un dataframe
2. Descarte de variables
3. Selección de fechas
4. Exportar en formato .CSV

Las operaciones en detalle se pueden consultar en el notebook adjunto, desplegado en GoogleColab aquí: 

https://colab.research.google.com/drive/1uVdMhhzfMzMxQBLlx2wMpYtZIILgsJ5M?usp=sharing

## Conclusiones y próximos pasos

El mundo de la cartografía siempre ha necesitado de conocimientos previos sobre proyecciones, sistemas de referencia, formatos de datos georreferenciados  y sobre todo la instalación de software específico para crear mapas. Gracias al desarrollo de productos web uno de estos proyectos nos permite crear mapas de forma muy sencilla y puede suponer una herramienta muy potente a la hora de crear mapas sin necesidad de muchos conocimientos previos y con un alto grado de customización.  

A partir de este punto se pueden explorar herramientas más sofisticadas que requieren bien de conocimientos generales, bien de conocimientos de programación para poder realizar mapas con Leaflet o con D3.js, dependiendo de la audiencia y de la aplicación en la cual queremos encuadrar el mapa.  

## Ámbitos de Aplicación

La creación de mapas sencillos tiene muchos campos de aplicación, ya que la cartografía en general resulta ser una de las formas de visualización más claras y populares gracias a su uso desde el origen de la civilización. Los ámbitos propuestos incluyen:

Redacciones de periodismo: reaccionar a eventos concretos tales como catástrofes naturales o grandes bases de datos de eventos georreferenciados puede ser más fácil gracias a herramientas como KeplerGL.

Corporaciones y empresas: localización de volúmenes asociados a puntos concretos de la geografía se puede leer de forma intuitiva con la creación de mapas que pueden resumir grandes cantidades de datos.  
Aplicaciones: Integrar mapas dentro de las aplicaciones suele ayudar tanto en las capas tanto de información como en la de interactividad para explorar el rendimiento y resultado de un producto a diferentes escalas.  
