# De las secciones censales a los códigos postales: análisis de instalaciones deportivas y nivel de renta en Sevilla 

## Descripción

Este repositorio contiene tanto los datos como el código necesario para la realización del ejercicio de datos del portal de datos abiertos datos.gob.es referente a al uso de datos de secciones censales y su aplicación al cálculo de la distribución de instalaciones deportivas por niveles de renta en la provincia de Sevilla. 

El código se ha desarrollado en Python para leer, procesar y representar información del Instituto Nacional de Estadística (INE) sobre la renta asociada a cada sección censal así como la información de la Junta de Andalucía sobre la localización de las instalaciones deportivas en Andalucía. 

Además de la lectura y análisis de los datos, se realiza igualmente una conversión de datos, desde datagframes de Pandas a ficheros de salida en formato .geojson, para la visualización tanto de las características asociadas a las secciones censales como aquellas asociadas a los códigos postales en otras plataformas diferentes de los notebooks o del propio Python. Se recomienda el uso de Kepler.gl para una visualización rápida e intuitiva de las variables de salida de nuestro análisis tal y como se indica tanto en el notebook de Google Colab como en el propio desarrollo del ejercicio. 

## Objetivos

Los objetivos a cubrir por este ejercicio de datos son los siguientes: 

- Lectura de ficheros .txt y .csv
- Estructuración en dataframes de Pandas
- Filtrado de datos para poder seleccionar periodos de tiempo de interés o propiedades concretas así como áreas concretas
- Conversión de formatos y salida en formato .geojson
- Cruzar tablas para asociar valores a aquellas columnas comunes de tablas diferentes.
- Creación de histogramas
- Creación de diagramas de tarta

## Estructura de carpetas

En este repositorio se puede encontrar el notebook de GoogleColab:

https://colab.research.google.com/drive/1TctZSNeyCl7y9siFxPS6fRg3hc7KP7fJ?usp=sharing

Así como una carpeta con datos útiles para el desarrollo del ejercicio: 

- Renta por sección censal
- Geometría de los códigos postales de la provincia de Sevilla
- Tramos de vía de las secciones censales en el conjunto del Estado
- Relación de instalaciones deportivas por código postal en Andalucía.

El tamaño de las geometrías asociadas a las secciones censales excede la capacidad de almacenamiento de Github, así que se invita al lector a recurrir a la fuente de tales geometrías en cartociudad. 

https://centrodedescargas.cnig.es/CentroDescargas/cartociudad

## Librerias

En el desarrollo de este ejercicio en Python es necesaria la instalación de las siguientes librerías: 

- Pandas
- Numpy
- Scipy
- Geopandas
- Matplotlib

## Datasets

- Geometría de las secciones censales del Instituto Nacional de estadística para el año 2023. https://ine.es/dyngs/DAB/es/index.htm?cid=1389

- Geometría de los códigos postales en la provincia de Sevilla. https://centrodedescargas.cnig.es/CentroDescargas/cartociudad

- Relación de tramos de vía de secciones censales por código postal, del Instituto Nacional de Estadística. https://www.ine.es/dyngs/DAB/es/index.htm?cid=1390

- Renta neta media por persona por sección censal del Instituto Nacional de Estadística.  https://datos.gob.es/es/catalogo/ea0042823-atlas-de-distribucion-de-renta-de-los-hogares-adrh

- Censo de instalaciones deportivas de Andalucía, que incluye información sobre su localización -localización por calle, municipio, provincia  y código postal– y tipo de instalación deportivas. https://datos.gob.es/es/catalogo/a01002820-censo-de-instalaciones-deportivas-de-andalucia

## Conclusiones y proximos pasos

Este ejercicio de datos nos permite vincular una variable asociada a las secciones censales con el área definida por los códigos postales. Aunque se ha demostrado su utilidad para el caso de las instalaciones deportivas esta proceso tiene multitud de aplicaciones, empezando por el más básico análisis electoral, donde los resultados se ofrecen por secciones censales. 

Otra de las virtudes del ejercicio es el de cruzar datos de diferentes fuentes para poder relacionarlos con una sola línea de código, tal y como se muestra varias veces en los comandos utilizados en Python para este ejercicio. Esto resulta de gran utilidad cuando manejamos varios conjuntos de datos para analizar un problema concreto y necesitamos armonizar y relacionar esos conjuntos de datos. 

Como próxmos pasos se propone:

- Desarrollar un análisis más refinado sobre el tipo de deporte que se practica en cada instalación deportiva. Los casos de baloncesto o pádel eran sencillos de representar aunque no tan claros de interpretar. Otros deportes atienden a descripciones más complejas en la base de datos de forma que necesitan un tratamiento de texto más sofisticado que el presentado aquí.

- Incorporar a las hipótesis formuladas conocimiento sobre la promoción del deporte, los planes urbanísticos y toda la sociología del comportamiento que lleva a la instalación última de centros deportivos en las ciudades y pueblos. Las hipótesis aquí planteadas responden más a mostrar un ejemplo de uso de las secciones censales y códigos postales sin mayores ambiciones en el ámbito que se ha tratado.

- Explorar otras formas de visualización para la distribución de instalaciones deportivas por nivel de renta, más allá de un histograma para poder refinar el análisis y la atención sobre características concretas de la ciudad en comnbinación con otros conjuntos de datos urbanos. 


