# Visualiza las zonas de sombra del eclipse

## Descripción

El baile celestial de los astros en el sistema solar ofrece cada cierto tiempo espectáculos únicos y singulares, como toda la secuencia de eclipses totales que tendrán lugar en la península ibérica durante los próximos tres años. Durante un eclipse total la Luna se interpone entre la Tierra y el Sol, ocultando al astro rey y proyectando durante unos minutos una sombra sobre una parte de la superficie terrestre.

El eclipse total previsto para el 12 de Agosto de 2026 tiene estimado su comienzo hacia las 20h30 horas (GMT+01:00), cubriendo de penumbra desde Galicia hasta las islas Baleares a lo largo de la hora y media prevista de duración del eclipse.

El Centro Nacional de Información Geográfica (CNIG) ha puesto a disposición del público un dataset que ofrece un amplio espectro de información astronómica relativa a los eclipses que se van a producir sobre la península ibérica durante los próximos tres años.

Estos datasets incluyen la visibilidad por el propio relieve del terreno a la hora del eclipse, la duración del eclipse en cada punto de la geografía española, el nivel de oscurecimiento o la elevación del Sol en el punto máximo del eclipse, así como la sombra proyectada por la Luna en su trayecto por delante del Sol.

En este ejercicio accederemos al dataset del CNIG y abriremos los ficheros tipo .TIF y .GPKG con toda la información relativa al eclipse, y en concreto todo lo relacionado con las zonas de sombra, tanto en lo referente a la visibilidad por efecto del relieve en la península como en lo que respecta a la zona de sombra en sí debido al eclipse total.

Una vez hayamos accedido a los datos delimitaremos nuestro análisis a una zona concreta sobre la visibilidad por relieve, recortaremos los datos originales con el perímetro de un municipio, exportaremos el resultado en formato GeoJSON y haciendo uso de éste seremos capaces de crear todo tipo de mapas con diversas herramientas muy útiles e intuitivas tales como KeplerGL, GoogleEarth, Leaflet o D3.js.

## Análisis en Python

El análisis en Python comprende dos ejercicios. En el primero realizaremos: 

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
- Exportar en formato geojson
- Mapa del resultado 

## Conclusiones y próximos pasos 

Este ejercicio de datos nos permite pasar de un formato de datos de entornos profesionales de sistemas de información geográfica a otros formatos más manejables para poder crear nuestros propios mapas, bien con la ayuda de aplicaciones populares como KeplerGL o GoogleEarth, bien con librerías de Javascript para su integración en proyectos web.  

Asimismo, hemos visto cómo con unas pocas líneas de código podemos manipular los datos de entrada para focalizar sobre regiones de interés, seleccionar intervalos temporales determinados o customizar mapas a nuestro gusto y elección.  

Los pasos siguientes que se proponen abarcan:  

- Explorar los formatos NetCDF o KML/KMZ, también georreferenciados, para tener un mayor control y dominio sobre los formatos de datos más populares en cartografía y análisis geoespacial.  

- Comparar las características astronómicas del eclipse de 2026 con los de 2027 y 2028, también disponibles en la base de datos del CNIG disponible en el portal de datos abiertos.  

- Representar las variables que no se han mostrado en este ejercicio como las efemérides o la duración, elevación, azimut, etc... de los cuerpos celestes implicados en el eclipse.  


## Ámbitos de aplicación

El resultado de este ejercicio de visualización de datos aplica y apela a los siguientes ámbitos del análisis de datos:  

- Periodístico: para la divulgación de la información precisa referente a los eclipses de 2026, 2027 y 2028, tanto en lo referente a lo estrictamente ciudadano respecto a los lugares desde los cuales se puede ver el eclipse o la extensión de la zona de sombra a cada instante.  

- Científico: una vez los datos son accesibles se pueden explorar todas las variables astronómicas incluidas en el lote del CNIG y hacer un retrato del fenómeno astronómico mucho más completo que el descrito aquí.  

- Analítico: el ejercicio se ha ceñido a la visualización más tradicional en base a mapas y cartografías. Explorar otras formas de visualización con un conjunto de datos tan atractivo puede incentivar la creatividad y la innovación a la hora de representar este tipo de eventos.  
