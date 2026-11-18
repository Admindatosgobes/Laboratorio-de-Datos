# De las secciones censales a los códigos postales: análisis de instalaciones deportivas

## Descripción

Este repositorio contiene tanto los datos como el **código necesario para la realización del ejercicio** de datos referente al uso de datos de secciones censales y su aplicación al análisis de la distribución de las instalaciones deportivas según los niveles de renta estimados para los códigos postales de la provincia de Sevilla. 

El código para leer, procesar y representar información del Instituto Nacional de Estadística (INE) sobre la renta asociada a cada sección censal, así como la información de la Junta de Andalucía sobre la localización de las instalaciones deportivas en Andalucía, se ha **desarrollado en Python**. 

Además de la lectura y análisis de los datos, se realiza igualmente una **conversión** desde Dataframes de Pandas a ficheros  en formato GeoJSON. Esto permite visualizar, tanto de las características asociadas a las secciones censales como las correspondientes a los códigos postales en otras plataformas diferentes de los notebooks o del propio Python. Se recomienda el **uso de Kepler.gl** para una visualización rápida e intuitiva de las variables de salida de nuestro análisis, tal y como se indica tanto en el notebook de Google Colab como en el propio desarrollo del ejercicio. 

## Objetivos

Los **objetivos a cubrir** por este ejercicio de datos son los siguientes: 

- Lectura de ficheros .txt y .csv 
- Estructuración de los datos en DataFrames de Pandas 
- Filtrado de datos para  seleccionar periodos de tiempo, propiedades  o áreas concretas 
- Conversión de formatos y generación de archivos de salida en formato .geojson 
- Combinación de diferentes Dataframes para la obtención de nuevas métricas  
- Creación de histogramas 

## Estructura de carpetas

En este repositorio se puede encontrar el **notebook de GoogleColab**:

https://colab.research.google.com/drive/1TctZSNeyCl7y9siFxPS6fRg3hc7KP7fJ?usp=sharing

Asimismo, se dispone de una carpeta con los conjuntos de datos necesarios para el desarrollo del ejercicio: 

- Renta por sección censal
- Geometría de los códigos postales de la provincia de Sevilla
- Tramos de vía de las secciones censales en el conjunto del Estado
- Relación de instalaciones deportivas por código postal en Andalucía.

El tamaño de las geometrías asociadas a las secciones censales excede la capacidad de almacenamiento de Github, así que se invita al lector a recurrir a la fuente de tales geometrías en CartoCiudad. 

https://centrodedescargas.cnig.es/CentroDescargas/cartociudad

## Librerias

En el desarrollo de este ejercicio en Python es necesaria la **instalación de las siguientes librerías**: 

- **Pandas**
- **Numpy**
- **Scipy**
- **GeoPandas**
- **Matplotlib**

## Datasets

- **Geometría de las secciones censales** del Instituto Nacional de estadística para el año 2023. https://ine.es/dyngs/DAB/es/index.htm?cid=1389

- **Geometría de los códigos postales** en la provincia de Sevilla. https://centrodedescargas.cnig.es/CentroDescargas/cartociudad

- **Relación de tramos de vía de secciones censales** por código postal, del Instituto Nacional de Estadística. https://www.ine.es/dyngs/DAB/es/index.htm?cid=1390

- **Renta neta media por persona por sección censal** del Instituto Nacional de Estadística.  https://datos.gob.es/es/catalogo/ea0042823-atlas-de-distribucion-de-renta-de-los-hogares-adrh

- **Censo de instalaciones deportivas de Andalucía**, que incluye información sobre su localización -localización por calle, municipio, provincia  y código postal– y tipo de instalación deportivas. https://datos.gob.es/es/catalogo/a01002820-censo-de-instalaciones-deportivas-de-andalucia

## Conclusiones y proximos pasos

Este ejercicio de datos nos permite **vincular una variable asociada** a las secciones censales con el área definida por los códigos postales. Aunque se ha demostrado su utilidad para el caso de las instalaciones deportivas, esta proceso tiene multitud de aplicaciones, empezando por el más **básico análisis electoral**, donde los resultados se ofrecen por secciones censales. 

Otra de las virtudes del ejercicio es el mostrar cómo **cruzar datos de diferentes fuentes a partir de campos comunes**, tal y como se realiza en varias veces en los comandos de Python urtilizados. Esto resulta de gran utilidad cuando manejamos varios conjuntos de datos para analizar un problema concreto y necesitamos **armonizarlos y relacionarlos**. 

Como próxmos pasos se propone:

- **Desarrollar un análisis más detallado** sobre el tipo de deporte que se practica en cada instalación deportiva.  
- **Incorporar al análisis información sobre la promoción del deporte, los planes urbanísticos y otros factores sociales y territoriales** que puedan estar relacionados con la localización de las instalaciones deportivas en las ciudades y municipios. 
- **Explorar otras formas de visualización** para la distribución de instalaciones deportivas por nivel de renta, además de los histogramas, para poder profundizar en el análisis de las características concretas de la ciudad. 


