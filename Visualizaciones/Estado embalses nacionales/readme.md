# Análisis del estado y evolución de los embalses de agua nacionales

## Introducción

Las visualizaciones son representaciones gráficas de datos que permiten comunicar de manera sencilla y efectiva la información ligada a los mismos. Las posibilidades de visualización son muy amplias, desde representaciones básicas, como puede ser un gráfico de líneas, barras o sectores, hasta visualizaciones configuradas sobre cuadros de mando o dashboards interactivos. Las visualizaciones juegan un papel fundamental en la extracción de conclusiones a partir de información visual, permitiendo además detectar patrones, tendencias, datos anómalos o proyectar predicciones, entre otras muchas funciones. 
Antes de lanzarnos a construir una visualización efectiva, debemos realizar un tratamiento previo de los datos, prestando especial atención a la obtención de los mismos y validando su contenido, asegurando que se encuentran en el formato adecuado y consistente para su procesamiento y no contienen errores. Un tratamiento previo de los datos es primordial para realizar cualquier tarea relacionada con el análisis de datos y la realización de visualizaciones efectivas.
En la sección “Visualizaciones paso a paso” estamos presentando periódicamente ejercicios prácticos de visualizaciones de datos abiertos que están disponibles en el catálogo datos.gob.es u otros catálogos similares. En ellos abordamos y describimos de manera sencilla las etapas necesarias para obtener los datos, realizar las transformaciones y análisis que resulten pertinentes para, finalmente, crear visualizaciones interactivas, de las que podemos extraer información en forma de conclusiones finales.
En este ejercicio práctico, hemos realizado un sencillo desarrollo de código que está convenientemente documentado apoyandonos en herramientas de uso gratuito. 

## Objetivos
El objetivo principal de este post es aprender a realizar una visualización interactiva partiendo de datos abiertos. Para este ejercicio práctico hemos escogido conjuntos de datos que contienen información relevante sobre los embalses nacionales. A partir de estos datos realizaremos el análisis de su estado y de su evolución temporal en los últimos años.

### Conjuntos de datos 
Para este caso práctico se han seleccionado conjuntos de datos publicados por el Ministerio para la Transición Ecológica y el Reto Demográfico, que dentro del boletín hidrológico recoge series temporales de datos sobre él volumen de agua embalsada de los últimos años para todos los embalses nacionales con una capacidad superior a 5hm3. Estos datos se encuentran disponibles en el Catálogo de datos de datos.gob.es, concretamente:https://datos.gob.es/es/catalogo/e05068001-boletin-hidrologico-semanal 
También se ha seleccionado un conjunto de datos geoespaciales. Durante su búsqueda, se han encontrado dos posibles archivos con datos de entrada, el que contiene las áreas geográficas correspondientes a los embalses de España y el que contiene las presas que incluye su geoposicionamiento como un punto geográfico. Aunque evidentemente no son lo mismo, embalses y presas guardan relación y para simplificar este ejercicio práctico optamos por utilizar el archivo que contiene la relación de presas de España. Inventario de presas disponible en: https://www.mapama.gob.es/ide/metadatos/index.html?srv=metadata.show&uuid=4f218701-1004-4b15-93b1-298551ae9446 , concretamente: https://www.miteco.gob.es/es/cartografia-y-sig/ide/descargas/egis_presa_geoetrs89_tcm30-175857.zip
Este conjunto de datos contiene geolocalizadas (Latitud, Longitud) las presas de toda España con independencia de su titularidad. Se entiende por presa, aquellas estructuras artificiales que, limitando en todo o en parte el contorno de un recinto enclavado en el terreno, esté destinada al almacenamiento de agua dentro del mismo. 

Para generar los puntos geográficos de interés se realiza un procesamiento mediante la herramienta QGIS, cuyos pasos son los siguientes: descargar el archivo ZIP, cargarlo en QGIS y guardarlo como CSV incluyendo la geometría de cada elemento como dos campos que especifican su posición como un punto geográfico (Latitud y Longitud). 

También se he realizado un filtrado para quedarnos con los datos correspondientes a las presas de los embalses que tengan una capacidad mayor a 5hm3

### Herramientas
Para la realización del preprocesamiento de los datos se ha utilizado el lenguaje de programación R desde el servicio cloud de [Google Colab](https://colab.research.google.com/?hl=es), que permite la ejecución de [Notebooks de Jupyter](https://jupyter.org/). 

> Google Colab o también llamado Google Colaboratory, es un servicio gratuito en la nube de Google Research que permite programar, ejecutar y compartir código escrito en Python o R desde tu navegador, por lo que no requiere la instalación de ninguna herramienta o configuración. 

Para la creación de la visualización interactiva se ha usado la herramienta [Datawrapper](https://www.datawrapper.de/). 

> Datawrapper es una herramienta online que permite realizar gráficos, mapas o tablas que pueden incrustarse en línea o exportarse como PNG, PDF o SVG. Esta herramienta es muy sencilla de usar y permite múltiples opciones de personalización. 

Si quieres conocer más sobre herramientas que puedan ayudarte en el tratamiento y la visualización de datos, puedes recurrir al informe [“Herramientas de procesado y visualización de datos”](https://datos.gob.es/es/documentacion/herramientas-de-procesado-y-visualizacion-de-datos). 


## Preprocesamiento de datos

Como primer paso del proceso es necesario realizar un análisis exploratorio de los datos (EDA) con el fin de interpretar adecuadamente los datos de partida, detectar anomalías, datos ausentes o errores que pudieran afectar a la calidad de los procesos posteriores y resultados, además de realizar las tareas de transformación y preparación de las variables necesarias. Un tratamiento previo de los datos es esencial para garantizar que los análisis o visualizaciones creados posteriormente a partir de ellos son confiables y consistentes. Si quieres conocer más sobre este proceso puedes recurrir a la [Guía Práctica de Introducción al Análisis Exploratorio de Datos](https://datos.gob.es/es/documentacion/guia-practica-de-introduccion-al-analisis-exploratorio-de-datos). 

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

Para abordar el proceso de diseño del conjunto de representaciones visuales de los datos, el primer paso es plantearnos las preguntas que queremos resolver. Proponemos las siguientes:

* ¿Cómo se está distribuyendo el número de hombres y mujeres entre los alumnos matriculados de Grado, Máster y Doctorado a lo largo de los últimos cursos?

Si nos centramos en el último curso 2020-2021:

*	¿Cuáles son las ramas de enseñanza más demandadas en las universidades españolas? ¿Y las titulaciones? 
*	¿Cuáles son las universidades con mayor número de matriculaciones y donde se ubican? 
*	¿En qué rangos de edad se encuentra el alumnado universitario de Grado? 
*	¿Cuál es la nacionalidad de los estudiantes de Grado de las universidades españolas?

¡Vamos a buscar las respuestas viendo los datos!

### Distribución de las matriculaciones en las universidades españolas desde el curso 2015-2016 hasta 2020-2021, desagregado por sexo y nivel académico. 

Esta representación visual la hemos realizado teniendo en cuenta las matriculaciones de Grado, Master y Doctorado. Una vez que hemos subido la tabla de datos a Datawrapper (conjunto de datos "Matriculaciones_NivelAcademico"), hemos seleccionado el tipo de gráfico a realizar, en este caso un diagrama de barras apiladas (stacked bars) para poder reflejar por cada curso y sexo, las personas matriculadas en cada nivel académico. De esta forma podemos ver, además, el global de estudiantes matriculados por curso. A continuación, hemos seleccionado el tipo de variable a representar (Matriculaciones) y las variables de desagregación (Sexo y Curso). Una vez obtenido el gráfico, podemos modificar de forma muy sencilla la apariencia, modificando los colores, la descripción y la información que muestra cada eje, entre otras características. 

[![Serie matriculaciones sexo y nivel académico](https://github.com/Admindatosgobes/Laboratorio-de-Datos/raw/main/Visualizaciones/Caracterizaci%C3%B3n%20del%20alumnado%20de%20la%20Universidad%20espa%C3%B1ola%20y%20titulaciones%20m%C3%A1s%20demandadas/Imagenes/Serie-matriculaciones-por-sexo-y-curso-en-las-universidades.png)](https://datawrapper.dwcdn.net/tBkIx/6/)

Para responder a las siguientes preguntas, nos centraremos en el alumnado de grado y en el curso 2020-2021, no obstante, las siguientes representaciones visuales pueden ser replicadas para el alumnado de Máster y Doctorado y para los diferentes cursos. 

### Mapa de las universidades españolas georreferenciadas, donde se muestra el número de matriculados que presentan cada una de ellas. 

Para la realización del mapa hemos utilizado un listado de las [universidades españolas georreferenciadas](https://opendata.esri.es/datasets/ComunidadSIG::universidades-de-espa%C3%B1a/about) publicado por el [Portal de Datos Abiertos de Esri España](https://opendata.esri.es/). Una vez descargados los datos de las distintas áreas geográficas en formato GeoJSON, los transformamos en Excel, para poder realizar una unión entre el datasets de las universidades georreferenciadas y el dataset que presenta el número de matriculados por cada universidad que previamente hemos preprocesado. Para ello hemos utilizado la función [BUSCARV()](https://support.microsoft.com/es-es/office/funci%C3%B3n-buscarv-0bbc8083-26fe-4963-8ab8-93a18ad188a1) de Excel quenos permitira localizar determinados elementos en un rango de celdas de una tabla. 

Antes de subir el conjunto de datos a Datawrapper, debemos seleccionar la capa que muestra el mapa de España dividido en provincias que nos proporciona la propia herramienta. Concretamente, hemos seleccionado la opción "Spain>>Provinces(2018)". Seguidamente procedemos a incorporar el conjunto de datos "Universidades", antes generado, (este conjunto de datos se adjunta en la carpeta de conjuntos de datos de GitHub para esta visualización paso a paso), indicando que columnas contienen los valores de las variables Latitud y Longitud. 

A partir de este punto, Datawrapper ha generado un mapa en el que se muestran las ubicaciones de cada una de las universidades. Ahora podemos modificar el mapa según nuestras preferencias y ajustes. En este caso, haremos que el tamaño de los puntos y el color dependa del número de matriculaciones que presente cada universidad. Además, para que estos datos se muestren, en la pestaña “Annotate”, en la sección “Tooltips”, debemos indicarle las variables o el texto que deseemos que aparezca. 

[![Matriculaciones en cada Universidad española](https://github.com/Admindatosgobes/Laboratorio-de-Datos/raw/main/Visualizaciones/Caracterizaci%C3%B3n%20del%20alumnado%20de%20la%20Universidad%20espa%C3%B1ola%20y%20titulaciones%20m%C3%A1s%20demandadas/Imagenes/Matriculaciones_universidades_mapa.png)](https://datawrapper.dwcdn.net/zsX4s/1/)

### Ranking de matriculaciones por titulación

Para esta representación gráfica utilizamos el objeto visual de Datawrapper tabla (Table) y el conjunto de datos "Titulaciones_totales" para mostrar el número de matriculaciones que presenta cada una de las titulaciones impartidas durante el curso 2020-2021. Dado que el número de titulaciones es muy extenso, la herramienta nos ofrece la posibilidad de incluir un buscador que permite filtrar los resultados.

[![Ranking de titulaciones](https://github.com/Admindatosgobes/Laboratorio-de-Datos/raw/main/Visualizaciones/Caracterizaci%C3%B3n%20del%20alumnado%20de%20la%20Universidad%20espa%C3%B1ola%20y%20titulaciones%20m%C3%A1s%20demandadas/Imagenes/Ranking-titulaciones.png)](https://datawrapper.dwcdn.net/ZDC2x/1/)

### Distribución de matriculaciones por rama de enseñanza

Para esta representación visual, hemos utilizado el conjunto de datos "Matriculaciones_Rama_Grado" y seleccionado gráficos de sectores (Pie Chart), donde hemos representado el número de matriculaciones según sexo en cada una de las ramas de enseñanza en las cuales se dividen las titulaciones impartidas por las universidades (Ciencias Sociales y Jurídicas, Ciencias de la Salud, Artes y Humanidades, Ingeniería y Arquitectura y Ciencias). Al igual que en el resto de gráficos, podemos modificar el color del gráfico, en este caso en función de la rama de enseñanza. 

[![Matriculados por rama de enseñanza](https://github.com/Admindatosgobes/Laboratorio-de-Datos/raw/main/Visualizaciones/Caracterizaci%C3%B3n%20del%20alumnado%20de%20la%20Universidad%20espa%C3%B1ola%20y%20titulaciones%20m%C3%A1s%20demandadas/Imagenes/Matriculaciones-de-grado-por-rama.png)](https://www.datawrapper.de/_/0SXGq/)

### Matriculaciones de Grado por edad y nacionalidad

Para la realización de estas dos representaciones de datos visuales utilizamos diagramas de barras (Bar Chart), donde mostramos la distribución de matriculaciones en el primero, desagregada por sexo y nacionalidad, utilizaremos el conjunto de datos "Matriculaciones_Grado_nacionalidad" y en el segundo, desagregada por sexo y edad, utilizando el conjunto de datos "Matriculaciones_Grado_edad". Al igual que los visuales anteriores, la herramienta facilita de forma sencilla la modificación de las características que presentan los gráficos. 

[![Matriculados por sexo y nacionalidad](https://github.com/Admindatosgobes/Laboratorio-de-Datos/raw/main/Visualizaciones/Caracterizaci%C3%B3n%20del%20alumnado%20de%20la%20Universidad%20espa%C3%B1ola%20y%20titulaciones%20m%C3%A1s%20demandadas/Imagenes/Matriculaciones-grado-sexo-nacionalidad.png)](https://www.datawrapper.de/_/CzpEo/)[![Matriculados por sexo y edad](https://github.com/Admindatosgobes/Laboratorio-de-Datos/raw/main/Visualizaciones/Caracterizaci%C3%B3n%20del%20alumnado%20de%20la%20Universidad%20espa%C3%B1ola%20y%20titulaciones%20m%C3%A1s%20demandadas/Imagenes/Matriculaciones-grado-sexo-edad.png)](https://www.datawrapper.de/_/vUmiK/)

## Conclusiones

La visualización de datos es uno de los mecanismos más potentes para **explotar y analizar el significado implícito de los datos, independientemente del tipo de dato y el grado de conocimiento tecnológico del usuario.** Las visualizaciones nos permiten construir significado sobre los datos y la creación de narrativas basadas en la representación gráfica. En el conjunto de representaciones gráficas de datos que acabamos de implamentar se puede observar lo siguiente:

* El número de matriculaciones aumenta a lo largo de los cursos académicos independientemente del nivel académico (Grado, Máster o Doctorado).
* El número de mujeres matriculadas es mayor que el de hombres en Grado y Máster, sin embargo es menor en el caso de las matriculaciones de doctorado, excepto en el curso 2019-2020.
* La mayor concentración de universidades la encontramos en la Comunidad de Madrid, seguido de la Comunidad Autónoma de Cataluña. 
* La universidad que concentra mayor número de matriculaciones durante el curso 2020-2021 es la UNED (Universidad Nacional de Educación a Distancia) con 146.208 matriculaciones, seguida de la Universidad Complutense de Madrid con 57.308 matriculaciones y la Universidad de Sevilla con 52.156. 
* La titulación más demandada el curso 2020-2021 es el Grado en Derecho con 82.552 alumnos a nivel nacional, seguido del Grado de Psicología con 75.738 alumnos y sin apenas diferencia, el Grado en Administración y Dirección de Empresas con 74.284 alumnos. 
* La rama de enseñanza con mayor concentración de alumnos es Ciencias Sociales y Jurídicas, mientras que la menos demandada es la rama de Ciencias. 
* Las nacionalidades que más representación tienen en la universidad española son de la región de la unión europea, seguido de los países de América Latina y Caribe, a expensas de la española.
* El rango de edad entre los 18 y 21 años es el más representado en el alumnado de las universidades españolas. 

Esperemos que esta visualización paso a paso te haya resultado útil para el aprendizaje de algunas técnicas muy habituales en el tratamiento y representación de datos abiertos. Volveremos para mostraros nuevas reutilizaciones. ¡Hasta pronto!
