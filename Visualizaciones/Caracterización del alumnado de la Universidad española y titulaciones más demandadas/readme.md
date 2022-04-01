
# Caracterización del alumnado de la Universidad española y titulaciones más demandadas

## Objetivo

El objetivo principal de este post es aprender a realizar una visualización interactiva partiendo de datos abiertos. Para este ejercicio práctico hemos escogido conjuntos de datos que contienen información relevante sobre el alumnado de la universidad española a lo largo de los últimos años. A partir de estos datos observaremos las **características que presenta el alumnado de la universidad española y cuáles son los estudios más demandados.** 

## Recursos 

### Conjuntos de datos 
Para este caso práctico se han seleccionado conjuntos de datos publicados por el [Ministerio de Universidades](https://www.universidades.gob.es), que recoge series temporales de datos con diferentes desagregaciones que facilitan el análisis de las características que presenta el alumnado de la universidad española. Estos datos se encuentran disponibles en el [catálogo de datos de datos.gob.es](https://datos.gob.es/es/catalogo?_publisher_display_name_limit=0&publisher_display_name=Ministerio+de+Universidades) y en el propio [catálogo de datos del Ministerio de Universidades](https://www.universidades.gob.es/portal/site/universidades/menuitem.a9621cf716a24d251662c810026041a0/?vgnextoid=42d6372673680710VgnVCM1000001d04140aRCRD). Concretamente los datasets que usaremos son: 
-	[Matriculados por tipo de modalidad de la universidad, sexo, zona de nacionalidad y ámbito de estudio](https://datos.gob.es/es/catalogo/e05073401-estudiantes-matriculados-en-doctorado-resultados-por-comunidad-autonoma-matriculados-por-tipo-y-modalidad-de-la-universidad-sexo-zona-de-nacionalidad-y-ambito-de-estudio) y [Matriculados por tipo y modalidad dela universidad, sexo, grupo de edad y ámbito de estudio](https://datos.gob.es/es/catalogo/e05073401-estudiantes-matriculados-en-doctorado-resultados-por-comunidad-autonoma-matriculados-por-tipo-y-modalidad-de-la-universidad-sexo-grupo-de-edad-y-ambito-de-estudio) para **estudiantes de doctorado por Comunidad autónoma** desde el curso 2015-2016 hasta 2020-2021.
-	[Matriculados por tipo de modalidad de la universidad, sexo, zona de nacionalidad y ámbito de estudio](https://datos.gob.es/es/catalogo/e05073401-estudiantes-matriculados-en-master-resultados-por-comunidad-autonoma-matriculados-por-tipo-y-modalidad-de-la-universidad-sexo-zona-de-nacionalidad-y-ambito-de-estudio) y [Matriculados por tipo y modalidad dela universidad, sexo, grupo de edad y ámbito de estudio](https://datos.gob.es/es/catalogo/e05073401-estudiantes-matriculados-en-master-resultados-por-comunidad-autonoma-matriculados-por-tipo-y-modalidad-de-la-universidad-sexo-grupo-de-edad-y-ambito-de-estudio) para **estudiantes de máster por Comunidad autónoma** desde el curso 2015-2016 hasta 2020-2021.
-	[Matriculados por tipo de modalidad de la universidad, sexo, zona de nacionalidad y ámbito de estudio](https://datos.gob.es/es/catalogo/e05073401-estudiantes-matriculados-en-grado-y-ciclo-resultados-por-comunidad-autonoma-matriculados-por-tipo-y-modalidad-de-la-universidad-sexo-zona-de-nacionalidad-y-ambito-de-estudio) y [Matriculados por tipo y modalidad dela universidad, sexo, grupo de edad y ámbito de estudio](https://datos.gob.es/es/catalogo/e05073401-estudiantes-matriculados-en-grado-y-ciclo-resultados-por-comunidad-autonoma-matriculados-por-tipo-y-modalidad-de-la-universidad-sexo-grupo-de-edad-y-campo-de-estudio) para **estudiantes de grado por Comunidad Autónoma** desde el curso 2015-2016 hasta 2020-2021. 
-	[Matriculaciones por cada una de las titulaciones impartidas por las universidades españolas](https://www.universidades.gob.es/stfls/universidades/Estadisticas/ficheros/MatriculadosEEU.xlsx) que se encuentra publicado en la [sección de Estadísticas de la página oficial del Ministerio de Universidades](https://www.universidades.gob.es/portal/site/universidades/menuitem.78fe777017742d34e0acc310026041a0/?vgnextoid=3b80122d36680710VgnVCM1000001d04140aRCRD). El contenido de este dataset abarca desde el curso 2015-2016 al 2020-2021, aunque para este último curso los datos son provisionales.     

### Herramientas
Para la realización del preprocesamiento de los datos se ha utilizado el lenguaje de programación R desde el servicio cloud de [Google Colab](https://colab.research.google.com/?hl=es), que permite la ejecución de [Notebooks de Jupyter](https://jupyter.org/). 

> Google Colab o también llamado Google Colaboratory, es un servicio gratuito en la nube de Google Research que permite programar, ejecutar y compartir código escrito en Python o R desde tu navegador, por lo que no requiere la instalación de ninguna herramienta o configuración. 

Para la creación de la visualización interactiva se ha usado la herramienta [Datawrapper](https://www.datawrapper.de/). 

> Datawrapper es una herramienta online que permite realizar gráficos, mapas o tablas que pueden incrustarse en línea o exportarse como PNG, PDF o SVG. Esta herramienta es muy sencilla de usar y permite múltiples opciones de personalización. 

Si quieres conocer más sobre herramientas que puedan ayudarte en el tratamiento y la visualización de datos, puedes recurrir al informe [“Herramientas de procesado y visualización de datos”](https://datos.gob.es/es/documentacion/herramientas-de-procesado-y-visualizacion-de-datos). 


## Preprocesamiento de datos

Como primer paso del proceso es necesario realizar un análisis exploratorio de los datos (EDA) con el fin de interpretar adecuadamente los datos de partida, detectar anomalías, datos ausentes o errores que pudieran afectar a la calidad de los procesos posteriores y resultados, además de tralizar las tareas de transformación y preparación de las variables necesarias. Un tratamiento previo de los datos es esencial para garantizar que los análisis o visualizaciones creados posteriormente a partir de ellos son confiables y consistentes. Si quieres conocer más sobre este proceso puedes recurrir a la [Guía Práctica de Introducción al Análisis Exploratorio de Datos](https://datos.gob.es/es/documentacion/guia-practica-de-introduccion-al-analisis-exploratorio-de-datos). 

Los pasos que se siguen en esta fase de preprocesamiento son los siguientes:

1. Instalación y carga de librerías
2. Carga de archivos de datos de origen
3. Creación de tablas de trabajo
4. Ajuste del nombre de algunas variables
5. Agrupación de varias variables en una única con diferentes factores
6. Tansformación de variables
7. Detección y tratamiento de datos ausentes (NAs)
8. Creación de nuevas variables calculadas
9. Resumen de las tablas transformadas
10. Preparación de datos para su representación visual
11. Almacenamiento de archivos con las tablas de datos preprocesados

Podrás reproducir este análisis, ya que el código fuente está disponible en este repositorio de GitHub. La forma de proporcionar el código es a través de un documento realizado sobre un Jupyter Notebook que una vez cargado en el entorno de desarrollo podrás ejecutar o modificar de manera sencilla. Debido al carácter divulgativo de este post y con el fin de favorecer el aprendizaje de lectores no especializados, el código no pretende ser el más eficiente, sino facilitar su comprensión por lo que posiblemente se te ocurrirán muchas formas de optimizar el código propuesto para lograr fines similares. ¡Te animamos a que lo hagas!

Puedes seguir los pasos y ejecutar el código fuente sobre este [notebook en Google Colab](https://colab.research.google.com/github/Admindatosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Caracterizaci%C3%B3n%20del%20alumnado%20de%20la%20Universidad%20espa%C3%B1ola%20y%20titulaciones%20m%C3%A1s%20demandadas/C%C3%B3digo/C%C3%B3difo_fuente.IPY)

## Visualizaciones de datos

Una vez realizado el preprocesamiento de los datos, vamos con la visualización. Para la realización de esta visualización interactiva usamos la herramienta Datawrapper en su versión gratuita. Se trata de una herramienta muy sencilla con especial aplicación en el periodismo de datos que te animamos a utilizar. Al ser una herramienta online, no es necesario tener instalado un software para interactuar o generar cualquier visualización, pero sí es necesario que la tabla de datos que le proporcionemos este estructurada adecuadamente. 

Para abordar el proceso de diseño del conjunto de represetaciones visuales de los datos, el primer paso es plantearnos las preguntas que queremos resolver. Proponemos la siguientes:

* ¿Cómo se está distribuyendo el número de hombres y mujeres entre los alumnos matriculados de Grado, Máster y Doctorado a lo largo de los últimos cursos?

Si nos centramos en el último curso 2020-2021:

*	¿Cuáles son las ramas de enseñanza más demandadas en las universidades españolas? ¿Y las titulaciones? 
*	¿Cuáles son las universidades con mayor número de matriculaciones y donde se ubican? 
*	¿En qué rangos de edad se encuentra el alumnado universitario de Grado? 
*	¿Cuál es la nacionalidad de los estudiantes de Grado de las universidades españolas?

¡Vamos a buscar las respuestas viendo los datos!

## Distribución de las matriculaciones en las universidades españolas desde el curso 2015-2016 hasta 2020-2021, desagregado por sexo y nivel académico. 

Esta representación visual la hemos realizado teniendo en cuenta las matriculaciones de Grado, Master y Doctorado. Una vez que hemos subido la tabla de datos a Datawrapper, hemos seleccionado el tipo de gráfico a realizar, en este caso un diagrama de barras apiladas (stacked bars) para poder reflejar por cada curso y sexo, las personas matriculadas en cada nivel académico. De esta forma podemos ver, además, el global de estudiantes matriculados por curso. A continuación, hemos seleccionado el tipo de variable a representar (Matriculaciones) y las variables de desagregación (Sexo y Curso). Una vez obtenido el gráfico, podemos modificar de forma muy sencilla la apariencia, modificando los colores, la descripción y la información que muestra cada eje, entre otras características. 

[![Serie matriculaciones sexo y nivel académico](https://github.com/Admindatosgobes/Laboratorio-de-Datos/raw/main/Visualizaciones/Caracterizaci%C3%B3n%20del%20alumnado%20de%20la%20Universidad%20espa%C3%B1ola%20y%20titulaciones%20m%C3%A1s%20demandadas/Imagenes/Serie-matriculaciones-por-sexo-y-curso-en-las-universidades.png)](https://datawrapper.dwcdn.net/tBkIx/6/)

Para responder a las siguientes preguntas, nos centraremos en el alumnado de grado y en el curso 2020-2021, no obstante, las siguientes representaciones visuales pueden ser replicadas para el alumnado de Máster y Doctorado y para los diferentes cursos. 

## Mapa de las universidades españolas georreferenciadas, donde se muestra el número de matriculados que presentan cada una de ellas. 

Para la realización del mapa hemos utilizado un listado de las [universidades españolas georreferenciadas](https://opendata.esri.es/datasets/ComunidadSIG::universidades-de-espa%C3%B1a/about) publicado por el [Portal de Datos Abiertos de Esri España](https://opendata.esri.es/). Una vez descargados los datos de las distintas áreas geográficas en formato GeoJSON, los transformamos en Excel, para poder realizar una unión entre el datasets de las universidades georreferenciadas y el dataset que presenta el número de matriculados por cada universidad que previamente hemos preprocesado. Para ello hemos utilizado la función [BUSCARV()](https://support.microsoft.com/es-es/office/funci%C3%B3n-buscarv-0bbc8083-26fe-4963-8ab8-93a18ad188a1) de Excel quenos permitira localizar determinados elementos en un rango de celdas de una tabla. 

Antes de subir el conjunto de datos a Datawrapper, debemos seleccionar la capa que muestra el mapa de España dividido en provincias que nos proporciona la propia herramienta. Concretamente, hemos seleccionado la opción "Spain>>Provinces(2018)". Seguidamente procedemos a incorporar el conjunto de datos generado (este conjunto de datos se adjunta en la carpeta de conjuntos de datos de GitHub para esta visualización paso a paso), indicando que columnas contienen los valores de las variables Latitud y Longitud. 

A partir de este punto, Datawrapper  ha generado un mapa en el que se muestran las ubicaciones de cada una de las universidades. Ahora podemos modificar el mapa según nuestras preferencias y ajustes. En este caso, haremos que el tamaño de los puntos y el color dependa del número de matriculaciones que presente cada universidad. Además, para que estos datos se muestren, en la pestaña “Annotate”, en la sección “Tooltips”, debemos indicarle las variables o el texto que deseemos que aparezca. 

[![Matriculaciones en cada Universidad española](https://github.com/Admindatosgobes/Laboratorio-de-Datos/raw/main/Visualizaciones/Caracterizaci%C3%B3n%20del%20alumnado%20de%20la%20Universidad%20espa%C3%B1ola%20y%20titulaciones%20m%C3%A1s%20demandadas/Imagenes/Matriculaciones_universidades_mapa.png)](https://datawrapper.dwcdn.net/zsX4s/1/)

## Ranking de matriculaciones por titulación

Para esta representación gráfica utilizamos el objeto visual de Datawrapper tabla (Table) que muestra el número de matriculaciones que presenta cada una de las titulaciones impartidas durante el curso 2020-2021. Dado que el número de titulaciones es muy extenso, la herramienta nos ofrece la posibilidad de incluir un buscador que permite filtrar los resultados.

[![Ranking de titulaciones](https://github.com/Admindatosgobes/Laboratorio-de-Datos/raw/main/Visualizaciones/Caracterizaci%C3%B3n%20del%20alumnado%20de%20la%20Universidad%20espa%C3%B1ola%20y%20titulaciones%20m%C3%A1s%20demandadas/Imagenes/Ranking-titulaciones.png)](https://datawrapper.dwcdn.net/ZDC2x/1/)

## Distribución de matriculaciones por rama de enseñanza

Para esta representación visual, hemos seleccionado gráficos de sectores (Pie Chart), donde hemos representado el % de matriculaciones según sexo en cada una de las ramas de enseñanza en las cuales se dividen las titulaciones impartidas por las universidades (Ciencias Sociales y Jurídicas, Ciencias de la Salud, Artes y Humanidades, Ingeniería y Arquitectura y Ciencias). Al igual que en el resto de gráficos, podemos modificar el color del gráfico, en este caso en función de la rama de enseñanza. 

[![Matriculados por rama de enseñanza](https://github.com/Admindatosgobes/Laboratorio-de-Datos/raw/main/Visualizaciones/Caracterizaci%C3%B3n%20del%20alumnado%20de%20la%20Universidad%20espa%C3%B1ola%20y%20titulaciones%20m%C3%A1s%20demandadas/Imagenes/Matriculaciones-de-grado-por-rama.png)](https://www.datawrapper.de/_/0SXGq/)


