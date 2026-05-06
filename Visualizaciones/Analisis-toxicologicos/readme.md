# Visualización paso a paso: Análisis de los resultados toxicológicos en accidentes de tráfico

## 1. Introducción

Las visualizaciones son representaciones gráficas de datos que permiten comunicar de manera sencilla y efectiva la información ligada a los mismos. Las posibilidades de visualización son muy amplias, desde representaciones básicas, como puede ser un gráfico de líneas, barras o sectores, hasta visualizaciones configuradas sobre cuadros de mando o dashboards interactivos. Las visualizaciones juegan un papel fundamental en la extracción de conclusiones utilizando el lenguaje visual, permitiendo además detectar patrones, tendencias, datos anómalos o proyectar predicciones, entre otras muchas funciones.  

En esta sección de [“Visualizaciones paso a paso”](https://datos.gob.es/es/documentacion/tipo/visualizaciones-paso-paso-3923) estamos presentando periódicamente ejercicios prácticos de visualizaciones de datos abiertos disponibles en  datos.gob.es u otros catálogos similares. En ellos se abordan y describen de manera sencilla las etapas necesarias para obtener los datos, realizar las transformaciones y análisis que resulten pertinentes para, finalmente, la creación de visualizaciones interactivas, de las que podemos extraer información resumida en unas conclusiones finales. En cada uno de estos ejercicios prácticos, se utilizan sencillos desarrollos de código convenientemente documentados, así como herramientas de uso gratuito. Todo el material generado está disponible para su reutilización en el repositorio del laboratorio de datos de Github perteneciente a datos.gob.es.

En este ejercicio práctico, hemos realizado un sencillo desarrollo de código que está convenientemente documentado apoyandonos en herramientas de uso gratuito. 

[Accede al repositorio del laboratorio de datos en Github.](https://github.com/datosgobes/Laboratorio-de-Datos/tree/main/Visualizaciones/Analisis-toxicologicos)

[Ejecuta el código de pre-procesamiento de datos sobre Google Colab.](https://colab.research.google.com/drive/1kj7kK8TidmtO7OzJTzos_V7um5IglmvN?usp=sharing)


## 2. Objetivo

El objetivo principal de este post es mostrar cómo realizar una visualización interactiva partiendo de datos abiertos. Para este ejercicio práctico hemos utilizado un dataset proporcionado por el Ministerio de Justicia que contiene información sobre los resultados toxicológicos realizados en accidentes de tráfico que cruzaremos con los datos que publica la Jefatura Central de Tráfico que contienen el detalle sobre el parque de vehículos matriculados en España.  

A partir de este cruce de datos analizaremos y podremos observar las ratios de resultados toxicológicos positivos en relación con el parque de vehículos matriculados. 

Cabe destacar que el Ministerio de Justicia pone a disposición de los ciudadanos diversos [cuadros de mando](https://datos.justicia.es/analisis-toxicologicos-accidentes-trafico) donde visualizar los datos sobre los resultados toxicológicos realizados en accidentes de tráfico. La diferencia radica en que este ejercicio práctico hace hincapié en la parte didáctica, mostraremos cómo procesar los datos y cómo diseñar y construir las visualizaciones.


## 3. Recursos

### 3.1 Conjuntos de datos
Para este caso práctico se ha utilizado un conjunto de datos proporcionado por el Ministerio de Justicia, el cual contiene información sobre los resultados toxicológicos realizados en accidentes de tráfico. Este conjunto de datos se encuentra en el siguiente repositorio de Github: 

[Conjunto de datos resultados toxicológicos en accidentes](https://github.com/datosgobes/Laboratorio-de-Datos/tree/main/Visualizaciones/Analisis-toxicologicos/Datos-origen) 

También se han utilizado los conjuntos de datos del parque de vehículos matriculados en España. Estos conjuntos de datos son publicados por parte de la Jefatura Central de Tráfico, organismo dependiente del Ministerio del Interior. Se encuentran disponibles en la siguiente página del catálogo de datos de datos.gob.es: 

[Conjuntos de datos parque de vehículos matriculados](https://github.com/datosgobes/Laboratorio-de-Datos/tree/main/Visualizaciones/Analisis-toxicologicos/Datos-origen)

### 3.2 Herramientas
Para la realización de las tareas de preprocesado de los datos se ha utilizado el lenguaje de programación Python escrito sobre un Notebook de Jupyter alojado en el servicio en la nube de Google Colab.

[Google Colab](https://colab.research.google.com/?hl=es) o también llamado Google Colaboratory, es un servicio gratuito en la nube de Google Research que permite programar, ejecutar y compartir código escrito en Python o R desde tu navegador, por lo que no requiere la instalación de ninguna herramienta o configuración.

Para la creación de la visualización interactiva se ha usado la herramienta Google Data Studio.

[Google Data Studio](https://datastudio.google.com/) es una herramienta online que permite realizar gráficos, mapas o tablas que pueden incrustarse en sitios web o exportarse como archivos. Esta herramienta es sencilla de usar y permite múltiples opciones de personalización.

Si quieres conocer más sobre herramientas que puedan ayudarte en el tratamiento y la visualización de datos, puedes recurrir al informe ["Herramientas de procesado y visualización de datos".](https://datos.gob.es/es/documentacion/herramientas-de-procesado-y-visualizacion-de-datos)


## 4. Tratamiento o preparación de los datos

Antes de lanzarnos a construir una visualización efectiva, debemos realizar un tratamiento previo de los datos, prestando especial atención a la obtención de los mismos y validando su contenido, asegurando que se encuentran en el formato adecuado y consistente para su procesamiento y que no contienen errores.  

Los procesos que te describimos a continuación los encontrarás comentados en el Notebook que también podrás ejecutar desde Google Colab.

Como primer paso del proceso es necesario realizar un análisis exploratorio de los datos (EDA) con el fin de interpretar adecuadamente los datos de partida, detectar anomalías, datos ausentes o errores que pudieran afectar a la calidad de los procesos posteriores y resultados. Un tratamiento previo de los datos es esencial para garantizar que los análisis o visualizaciones creados posteriormente a partir de ellos son confiables y consistentes. Si quieres conocer más sobre este proceso puedes recurrir a la ["Guía Práctica de Introducción al Análisis Exploratorio de Datos".](https://datos.gob.es/es/documentacion/guia-practica-de-introduccion-al-analisis-exploratorio-de-datos) 

El siguiente paso a dar es la generación de las tablas de datos preprocesados que usaremos para generar las visualizaciones. Para ello ajustaremos las variables, realizaremos el cruce de datos entre ambos conjuntos y filtraremos o agruparemos según sea conveniente. 

Los pasos que se siguen en este preprocesamiento de los datos son los siguientes: 

1. Importación de librerías 
2. Carga de archivos de datos a utilizar 
3. Detención y tratamiento de datos ausentes (NAs) 
4. Modificación y ajuste de las variables 
5. Generación de tablas con datos preprocesado para las visualizaciones 
6. Almacenamiento de las tablas con los datos preprocesados 

Podrás reproducir este análisis, ya que el código fuente está disponible en nuestra cuenta de GitHub. La forma de proporcionar el código es a través de un documento realizado sobre un Jupyter Notebook que una vez cargado en el entorno de desarrollo podrás ejecutar o modificar de manera sencilla. Debido al carácter divulgativo de este post y favorecer el entendimiento de los lectores no especializados, el código no pretende ser el más eficiente, sino facilitar su comprensión por lo que posiblemente se te ocurrirán muchas formas de optimizar el código propuesto para lograr fines similares. ¡Te animamos a que lo hagas!


## 5. Generación de las visualizaciones

Una vez hemos realizado el preprocesamiento de los datos, vamos con las visualizaciones. Para la realización de estas visualizaciones interactivas se ha usado la herramienta Google Data Studio. Al ser una herramienta online, no es necesario tener instalado un software para interactuar o generar cualquier visualización, pero sí es necesario que las tablas de datos que le proporcionemos estén estructuradas adecuadamente, para ello hemos realizado los pasos anteriores para la preparación de los datos. 

El punto de partida es el planteamiento de una serie de preguntas que la visualización nos ayudará a resolver. Proponemos las siguientes: 

¿Cómo está distribuido el parque de vehículos en España por Comunidades Autónomas ? 

¿Qué tipo de vehículo está implicado en mayor y en menor medida en accidentes de tráfico con resultados toxicológicos positivos?  

¿Dónde se producen más hallazgos toxicológicos en víctimas mortales de accidentes de tráfico? 

¡Vamos a buscar las respuestas viendo los datos! 

### 5.1 Parque de vehículos matriculados por CCAA y por típo de vehículo
Esta representación visual se ha realizado teniendo en cuanta las ratios de los resultados toxicológicos positivos por número de vehículos a nivel nacional. Contabilizamos como resultado positivo cada vez que un sujeto da positivo en el análisis de cada una de las sustancias, es decir, un mismo sujeto puede contabilizar varias veces en el caso de que sus resultados sean positivos para varias sustancias. Para ello se ha generado durante el preprocesamiento de datos la tabla  [“resultados_vehiculos.csv”](https://github.com/datosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Analisis-toxicologicos/Datos-preprocesados/resultados_vehiculos.csv)

Mediante un gráfico de barras apiladas, podemos evaluar los ratios de los resultados toxicológicos positivos por número de vehículos para las distintas sustancias y los distintos tipos de vehículos.

Según se definen en la “Guía de visualización de datos de la Generalitat Catalana”  los gráficos de barras se utilizan cuando se quiere comparar el valor total de la suma de los segmentos que forman cada una de las barras. Al mismo tiempo, ofrecen información sobre cómo son de grandes estos segmentos. 

Cuando las barras apiladas suman un 100%, es decir, que cada barra segmenteada ocupa la altura de la representación, el gráfico se puede considerar un gráfico que permite representar partes de un total.

La tabla aportan la misma información de una forma complementaria. 

Una vez obtenida la visualización, mediante la pestaña desplegable, aparece la opción de filtrar por tipo de sustancia. 

[Ver la visualización en pantalla completa.](https://datastudio.google.com/reporting/36bf9eed-2da2-49d8-b865-e3d81abba6d2/page/idq7C)

### 5.2 Ratio resultados toxicológicos positivos para los distintos tipos de vehículos
Esta representación visual se ha realizado teniendo en cuanta las ratios de los resultados toxicológicos positivos por número de vehículos a nivel nacional. Contabilizamos como resultado positivo cada vez que un sujeto da positivo en el análisis de cada una de las sustancias, es decir, un mismo sujeto puede contabilizar varias veces en el caso de que sus resultados sean positivos para varias sustancias. Para ello se ha generado durante el preprocesamiento de datos la tabla  [“resultados_vehiculos.csv”](https://github.com/datosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Analisis-toxicologicos/Datos-preprocesados/resultados_vehiculos.csv)

Mediante un gráfico de barras apiladas, podemos evaluar los ratios de los resultados toxicológicos positivos por número de vehículos para las distintas sustancias y los distintos tipos de vehículos.

Según se definen en la “Guía de visualización de datos de la Generalitat Catalana”  los gráficos de barras se utilizan cuando se quiere comparar el valor total de la suma de los segmentos que forman cada una de las barras. Al mismo tiempo, ofrecen información sobre cómo son de grandes estos segmentos. 

Cuando las barras apiladas suman un 100%, es decir, que cada barra segmenteada ocupa la altura de la representación, el gráfico se puede considerar un gráfico que permite representar partes de un total.

La tabla aportan la misma información de una forma complementaria. 

Una vez obtenida la visualización, mediante la pestaña desplegable, aparece la opción de filtrar por tipo de sustancia. 

[Ver la visualización en pantalla completa](https://datastudio.google.com/reporting/3d470f69-fc21-449e-adf2-1fe7a4ec3d1b/page/Uck7C)

### 5.3 Ratio resultados toxicológicos positivos para las CCAAs
Esta representación visual se ha realizado teniendo en cuenta las ratios de los resultados toxicológicos positivos por el parque de vehículos de cada CCAA. Contabilizamos como resultado positivo cada vez que un sujeto da positivo en el análisis de cada una de las sustancias, es decir, un mismo sujeto puede contabilizar varias veces en el caso de que sus resultados sean positivos para varias sustancias. Para ello se ha generado durante el preprocesamiento de datos la tabla [“resultados_ccaa.csv”.](https://github.com/datosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Analisis-toxicologicos/Datos-preprocesados/resultados_ccaa.csv)

Hay que remarcar que no tiene por qué coincidir la CCAA de matriculación del vehículo con la CCAA donde se ha registrado el accidente, no obstante, ya que este es un ejercicio didáctico y se presupone que en la mayoría de los casos coinciden, se ha decido partir de la base de que ambos coinciden. 

Mediante un mapa coroplético podemos visualizar que CCAAs son las que poseen las mayores ratios. A la información aportada en la primera visualización sobre este tipo de gráficos, hay que añadir lo siguiente.

Según se define en la “Guía para la representación de gráficos estadísticos del INEI”  los mapas coropléticos o de coropletas son muy utilizados para representar variables relativas, por ejemplo: índices, ratios o porcentajes, entre otro tipo de datos proporcionales.

 La tabla y el gráfico de barras aporta la misma información de una forma complementaria.  

Una vez obtenida la visualización, mediante la pestaña despegable, aparece la opción de filtrar por tipo de sustancia.

[Ver la visualización en pantalla completa](https://datastudio.google.com/reporting/22998dac-e53b-4cde-ba54-cdba6d90822d/page/Fnk7C)


## 6. Conclusiones del estudio

La visualización de datos es uno de los mecanismos más potentes para explotar y analizar el significado implícito de los datos, independientemente del tipo de dato y el grado de conocimiento tecnológico del usuario. Las visualizaciones nos permiten construir significado sobre los datos y la creación de narrativas basadas en la representación gráfica. En el conjunto de representaciones gráficas de datos que acabamos de implementar se puede observar lo siguiente: 

El parque de vehículos de las Comunidades Autónomas de Andalucía, Cataluña y Madrid corresponde a cerca del 50% del total del país. 

Las ratios de resultados toxicológicos positivos más altas se presentan en las motocicletas, siendo del orden de tres veces superior a la siguiente ratio, los turismos, para la mayoría de las sustancias. 

Las ratios de resultados toxicológicos positivos más bajas se presentan en los camiones. 

Los vehículos de dos ruedas (motocicletas y ciclomotores) presentan ratios en "cannabis" superiores a los obtenidos en "cocaina", mientras que los vehículos de cuatro ruedas (turismos, furgonetas y camiones) presentan ratios en "cocaina" superiores a los obtenidos en "cannabis"

La Comunidad Autónoma donde mayor es la ratio para el total de sustancias es La Rioja. 

Cabe destacar que en las visualizaciones tienes la opción de filtrar por tipo de vehículo y tipo de sustancia. Te animamos a lo que lo hagas para sacar conclusiones más específicas sobre la información concreta en la que estés más interesado. 

Esperemos que esta visualización paso a paso te haya resultado útil para el aprendizaje de algunas técnicas muy habituales en el tratamiento y representación de datos abiertos. Volveremos para mostraros nuevas reutilizaciones. ¡Hasta pronto! 
