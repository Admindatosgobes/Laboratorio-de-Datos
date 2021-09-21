# Laboratorio de Datos #

## [Guía practica de introducción al Análisis Exploratorio de Datos](https://datos.gob.es/es/documentacion/guia-practica-de-introduccion-al-analisis-exploratorio-de-datos)

Antes de realizar un análisis de  datos, con fines estadísticos o predictivos por ejemplo a través de técnicas de machine learning,  es necesario comprender la materia prima con la que vamos a trabajar. Hay que entender y evaluar la  calidad de los datos para así, entre otros aspectos, detectar y tratar los datos atípicos o incorrectos, evitando posibles errores que pudieran repercutir en los resultados del análisis. 
Una forma de llevar a cabo este pre-procesamiento es mediante un **Análisis Exploratorio de Datos (AED)** o **Exploratory Data Analysis (EDA)**.
#### ¿Qué es el Análisis Exploratorio de los Datos?
El AED consiste en aplicar un **conjunto de técnicas estadísticas dirigidas a explorar, describir y resumir la naturaleza de los datos**, de tal forma que podamos garantizar su **objetividad e interoperabilidad**.
Gracias a ello se pueden identificar posibles errores, revelar la presencia de valores atípicos, comprobar la relación entre variables (correlaciones) y su posible redundancia, así como realizar un análisis descriptivo de los datos mediante representaciones gráficas y resúmenes de los aspectos más significativos.
En muchas ocasiones, esta exploración de los datos se descuida y no se lleva a cabo de manera correcta. Por este motivo, desde datos.gob.es hemos elavorado una **guía practica introductorio** que recoge una serie de tareas mínimas para realizar un correcto Análisis Exploratorio de Datos, paso previo y necesario antes de llevar a cabo cualquier tipo de análisis estadístico o predictivo ligado a las técnicas de machine learning. 
#### **¿Qué incluye la guía?**
La guía explica de forma sencilla cuáles son los pasos a seguir para garantizar unos datos consistentes y veraces. Para su elaboración se ha tomado como referencia el análisis exploratorio de datos descrito en el libro [**R for Data Science**](https://r4ds.had.co.nz/) de Wickman y Grolemund (2017) disponible de forma gratuita. Estos pasos son: 
1. Análisis descriptivo, sintetizar la información que proporcional el conjunto de datos, extrayendo sus características más representativas. 
2. Re-ajustar los tipos de las variables, verificar que las variables se han almacenado con el tipo de valor correspondiente. 
3. Detección y tratamiento de datos ausentes. 
4. Detección y tratamiento de datos atípicos. 
5. Análisis de correlación de variables, analizar la relación entre dos o más variables. 

En la guía se explica cada uno de estos pasos y por qué son necesarios. Asimismo, se ilustran de manera práctiva a través de un ejemplo. Para dicho caso práctico, se ha utilizado el  dataset relativo al [registro de la calidad del aire en la Comunidad Autónoma de Castilla y León](https://datos.gob.es/es/catalogo/a07002862-calidad-del-aire-por-dias1) incluido en el [catálogo de datos abiertos de datos.gob.es](https://datos.gob.es/catalogo). El tratamiento se ha llevado a cabo con  herramientas tecnológicas Open Source y gratuitas. En la guía se recoge el código para que los usuarios pueden replicarlo de forma autodidacta siguiendo los pasos indicados.
La guía finaliza con un apartado de recursos adicionales para aquellos que quieran seguir profundizando en la materia.

#### ¿A quién va dirigida?

El público objetivo de la guía es el usuario reutilizador de datos abiertos. Es decir, desarrolladores, emprendedores o incluso periodistas de datos que quieran extraer todo el valor posible de la información con la que trabajan para obtener unos resultados fiables.

Es aconsejable que el usuario tenga nociones básicas del lenguaje de programación R, elegido para ilustrar los ejemplos. No obstante, en el apartado de bibliografía se incluyen recursos para adquirir mayores habilidades en este campo.

En el [informe](https://datos.gob.es/es/documentacion/guia-practica-de-introduccion-al-analisis-exploratorio-de-datos) puedes descargarte los materiales adicionales, así como acceder al **Código** utilizado en el ejemplo. 

*Nota: El código publicado pretende ser una guía para el lector, pero puede requerir de dependencias externas o configuraciones específicas para cada usuario que desee ejecutarlo.*
