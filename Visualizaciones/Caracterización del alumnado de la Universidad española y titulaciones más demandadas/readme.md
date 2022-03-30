
# Caracterización del alumnado de la Universidad española y titulaciones más demandadas

## Objetivo

El objetivo principal de este post es aprender a realizar una visualización interactiva partiendo de datos abiertos. Para este ejercicio práctico hemos escogido conjuntos de datos que contienen información relevante sobre el alumnado de la universidad española a lo largo de los últimos años. A partir de estos datos observaremos las **características que presenta el alumnado de la universidad española y cuáles son los estudios más demandados.** 

## Recursos 

### Conjuntos de datos 
Para este caso práctico se han seleccionado conjuntos de datos publicados por el [Ministerio de Universidades](https://www.universidades.gob.es), que recoge series temporales de datos con diferentes desagregaciones que facilitan el análisis de las características que presenta el alumnado de la universidad española. Estos datos se encuentran disponibles en el [catálogo de datos de datos.gob.es](https://datos.gob.es/es/catalogo?_publisher_display_name_limit=0&publisher_display_name=Ministerio+de+Universidades) y en el propio [catálogo de datos del Ministerio de Universidades](https://www.universidades.gob.es/portal/site/universidades/menuitem.a9621cf716a24d251662c810026041a0/?vgnextoid=42d6372673680710VgnVCM1000001d04140aRCRD). Concretamente los datasets que usaremos son: 
-	[Matriculados por tipo de modalidad de la universidad, sexo, zona de nacionalidad y ámbito de estudio](https://datos.gob.es/es/catalogo/e05073401-estudiantes-matriculados-en-doctorado-resultados-por-comunidad-autonoma-matriculados-por-tipo-y-modalidad-de-la-universidad-sexo-zona-de-nacionalidad-y-ambito-de-estudio) y [Matriculados por tipo y modalidad dela universidad, sexo, grupo de edad y ámbito de estudio para estudiantes de doctorado por Comunidad autónoma desde el curso 2015-2016 hasta 2020-2021](https://datos.gob.es/es/catalogo/e05073401-estudiantes-matriculados-en-doctorado-resultados-por-comunidad-autonoma-matriculados-por-tipo-y-modalidad-de-la-universidad-sexo-grupo-de-edad-y-ambito-de-estudio).
-	Matriculados por tipo de modalidad de la universidad, sexo, zona de nacionalidad y ámbito de estudio y Matriculados por tipo y modalidad dela universidad, sexo, grupo de edad y ámbito de estudio para estudiantes de máster por Comunidad autónoma desde el curso 2015-2016 hasta 2020-2021.
-	Matriculados por tipo de modalidad de la universidad, sexo, zona de nacionalidad y ámbito de estudio y Matriculados por tipo y modalidad dela universidad, sexo, grupo de edad y ámbito de estudio para estudiantes de grado por Comunidad Autónoma desde el curso 2015-2016 hasta 2020-2021. 
-	Matriculaciones por cada una de las titulaciones impartidas por las universidades españolas que se encuentra publicado en la sección de Estadísticas de la página oficial del Ministerio de Universidades.   

### Herramientas
Para la realización de este análisis (entorno de trabajo, programación) se ha utilizado el lenguaje de programación R desde el servicio cloud de [Google Colab](https://colab.research.google.com/?hl=es), que está basado en Notebooks de Jupyter. 

> Google Colab o también llamado Google Colaboratory, es un servicio en la nube de Google Research que permite programar, ejecutar y compartir código escrito en Python o R desde tu navegador, por lo que no requiere configuración. Este servicio es gratuito y está alojado en Jupyter Notebook. 

Para la creación de la visualización interactiva se ha usado la herramienta [Datawrapper](https://www.datawrapper.de/). 

> Datawrapper es una herramienta online que permite realizar gráficos, mapas o tablas que pueden incrustarse en línea o exportarse como PNG, PDF o SVG. Esta herramienta es muy sencilla de usar y permite múltiples opciones de personalización. 

Si quieres conocer más sobre herramientas que puedan ayudarte en el tratamiento y la visualización de datos, puedes recurrir al informe [“Herramientas de procesado y visualización de datos”](https://datos.gob.es/es/documentacion/herramientas-de-procesado-y-visualizacion-de-datos). 


## Preprocesamiento de datos

Como primer paso del proceso es necesario realizar un análisis exploratorio de los datos (EDA) con el fin de interpretar adecuadamente los datos de partida, detectar anomalías, datos ausentes o errores que pudieran afectar a la calidad de los procesos posteriores y resultados, además de tralizar las tareas de transformación y preparación de las variables necesarias. Un tratamiento previo de los datos es esencial para garantizar que los análisis o visualizaciones creados posteriormente a partir de ellos son confiables y consistentes. Si quieres conocer más sobre este proceso puedes recurrir a la [Guía Práctica de Introducción al Análisis Exploratorio de Datos](https://datos.gob.es/es/documentacion/guia-practica-de-introduccion-al-analisis-exploratorio-de-datos). 

Los pasos que se siguen en esta fase de preprocesamiento son los siguientes:

1.   Instalación y carga de librerías
2.   Carga de datos
3.   Cambio de nombre a las variables
4.   Creación de tablas de trabajo
5.   Conversión de varias variables en na única con diferentes factores 
6.   Transformación de variables 
7.   Detección y tratamiento de datos perdidos 
8.   Creación de nuevas variables 
9.   Resumen de la tabla
10.  Guardar las tablas de trabajo 

Podrás reproducir este análisis, ya que el código fuente está disponible en nuestra cuenta de GitHub. La forma de proporcionar el código es a través de un documento realizado sobre un Jupyter Notebook que una vez cargado en el entorno de desarrollo podrás ejecutar o modificar de manera sencilla. Debido al carácter divulgativo de este post y con el fin de favorecer el aprendizaje de lectores no especializados, el código no pretende ser el más eficiente, sino facilitar su comprensión por lo que posiblemente se te ocurrirán muchas formas de optimizar el código propuesto para lograr fines similares. ¡Te animamos a que lo hagas!

Puedes seguir los pasos y ejecutar el código fuente sobre este [notebook en Google Colab](https://colab.research.google.com/github/Admindatosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Caracterizaci%C3%B3n%20del%20alumnado%20de%20la%20Universidad%20espa%C3%B1ola%20y%20titulaciones%20m%C3%A1s%20demandadas/C%C3%B3digo/C%C3%B3difo_fuente.IPY)

## Visualizaciones de datos

* Serie temporal de las matriculaciones en las universidades españolas desde el curso 2015-2016 hasta 2020-2021, desagregado por sexo. Este gráfico lo hemos realizado para las matriculaciones de Grado, Master y Doctorado. 

|[![Serie matriculaciones Doctorado](https://github.com/Admindatosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Caracterizaci%C3%B3n%20del%20alumnado%20de%20la%20Universidad%20espa%C3%B1ola%20y%20titulaciones%20m%C3%A1s%20demandadas/Imagenes/Serie_doctorado.png)](https://datawrapper.dwcdn.net/PEdj6/1/)|[![Serie matriculaciones Máster](https://github.com/Admindatosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Caracterizaci%C3%B3n%20del%20alumnado%20de%20la%20Universidad%20espa%C3%B1ola%20y%20titulaciones%20m%C3%A1s%20demandadas/Imagenes/Serie%20Master.png)](https://datawrapper.dwcdn.net/XDNcL/1/)|[![Serie matriculaciones Grado](https://github.com/Admindatosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Caracterizaci%C3%B3n%20del%20alumnado%20de%20la%20Universidad%20espa%C3%B1ola%20y%20titulaciones%20m%C3%A1s%20demandadas/Imagenes/Serie_grado.png)](https://datawrapper.dwcdn.net/tBkIx/1/)

* Mapa de las universidades españolas georreferenciadas, donde se muestra el número de matriculados que presentan cada una de ellas. 
* 
[![Matriculaciones en cada Universidad española](https://github.com/Admindatosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Caracterizaci%C3%B3n%20del%20alumnado%20de%20la%20Universidad%20espa%C3%B1ola%20y%20titulaciones%20m%C3%A1s%20demandadas/Imagenes/Matriculaciones_universidades_mapa.png)](https://datawrapper.dwcdn.net/zsX4s/1/)


