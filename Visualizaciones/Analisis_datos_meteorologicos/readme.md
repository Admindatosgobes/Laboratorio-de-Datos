# Análisis de datos meteorológicos registrados en los últimos años

## 1. Introducción
Las visualizaciones son representaciones gráficas de datos que permiten comunicar de manera sencilla y efectiva la información ligada a los mismos. Las posibilidades de visualización son muy amplias, desde representaciones básicas, como puede ser un gráfico de líneas, barras o sectores, hasta visualizaciones configuradas sobre cuadros de mando o dashboards interactivos. Las visualizaciones juegan un papel fundamental en la extracción de conclusiones utilizando el lenguaje visual, permitiendo además detectar patrones, tendencias, datos anómalos o proyectar predicciones, entre otras muchas funciones.  

En esta sección de [“Visualizaciones paso a paso”](https://datos.gob.es/es/documentacion/tipo/visualizaciones-paso-paso-3923) estamos presentando periódicamente ejercicios prácticos de visualizaciones de datos abiertos disponibles en  datos.gob.es u otros catálogos similares. En ellos se abordan y describen de manera sencilla las etapas necesarias para obtener los datos, realizar las transformaciones y análisis que resulten pertinentes para, finalmente, la creación de visualizaciones interactivas, de las que podemos extraer información resumida en unas conclusiones finales. En cada uno de estos ejercicios prácticos, se utilizan sencillos desarrollos de código convenientemente documentados, así como herramientas de uso gratuito. Todo el material generado está disponible para su reutilización en el repositorio del [laboratorio de datos de Github](https://github.com/datosgobes/Laboratorio-de-Datos/tree/main/Visualizaciones/Analisis_datos_meteorologicos) perteneciente a datos.gob.es.

## 2. Objetivo
El objetivo principal de este ejercicio es hacer un análisis de los datos meteorológicos recogidos en varias estaciones durante los últimos años. Para realizar este análisis utilizaremos distintas visualizaciones generadas mediante la librería “ggplot2” del lenguaje de programación “R” 

De todas las estaciones meteorológicas españolas, hemos decidido analizar dos de ellas, una en la provincia más fría del país (Burgos) y otra en la provincia más cálida del país (Córdoba), según los datos de la AEMET. Se buscarán patrones y tendencias en los distintos registros entre los años 1990 y 2020 con la finalizad de entender la evolución meteorológica sufrida en este periodo de tiempo. 

Una vez analizados los datos, podremos contestar a preguntas como las que se muestran a continuación: 
¿Cuál es la tendencia en la evolución de las temperaturas en los últimos años? 
¿Cuál es la tendencia en la evolución de las precipitaciones en los últimos años? 
¿Qué estación meteorológica (Burgos o Córdoba) presenta una mayor variación de los datos climatológicos en estos últimos años? 
¿Qué grado de correlación hay entre las distintas variables climatológicas registradas? 

Estas, y muchas otras preguntas pueden ser resueltas mediante el uso de herramientas como ggplot2 que facilitan la interpretación de los datos mediante visualizaciones interactivas.

## 3. Recursos
### 3.1 Conjunto de datos
Los conjuntos de datos contienen distinta información meteorológica de interés para las dos estaciones en cuestión desglosados por año. Dentro del centro de descargas de la AEMET, podremos descárgalos, previa solicitud de la clave API, en el apartado “climatologías mensuales/anuales”. De las estaciones meteorológicas existentes, hemos seleccionado dos de las que obtendremos los datos: Burgos aeropuerto (2331) y Córdoba aeropuerto (5402) 

Cabe destacar, que, junto a los conjuntos de datos, también podremos descargar sus metadatos, los cuales son de especial importancia a la hora de identificar las distintas variables registradas en los conjuntos de datos. Estos conjuntos de datos también se encuentran disponibles en el repositorio [laboratorio de datos de Github](https://github.com/datosgobes/Laboratorio-de-Datos/tree/main/Visualizaciones/Analisis_datos_meteorologicos)

### 3.2 Herramientas
Para la realización de las tareas de preprocesado de los datos se ha utilizado el lenguaje de programación R escrito sobre un Notebook de Jupyter alojado en el servicio en la nube de [Google Colab](https://colab.research.google.com/?hl=es).

"Google Colab" o, también llamado Google Colaboratory, es un servicio en la nube de Google Research que permite programar, ejecutar y compartir código escrito en Python o R sobre un Jupyter Notebook desde tu navegador, por lo que no requiere configuración. Este servicio es gratuito.

Para la creación de las visualizaciones se ha usado la librería [ggplot2](https://ggplot2.tidyverse.org/).

"ggplot2" es un paquete de visualización de datos para el lenguaje de programación R. Se centra en la construcción de gráficos a partir de capas de elementos estéticos, geométricos y estadísticos. ggplot2 ofrece una amplia gama de gráficos estadísticos de alta calidad, incluyendo gráficos de barras, gráficos de líneas, diagramas de dispersión, gráficos de caja y bigotes, y muchos otros  

Si quieres conocer más sobre herramientas que puedan ayudarte en el tratamiento y la visualización de datos, puedes recurrir al informe "Herramientas de procesado y visualización de datos".

## 4. Tratamiento o preparación de los datos
Los procesos que te describimos a continuación los encontrarás comentados en el [Notebook](https://colab.research.google.com/drive/1YQurWKgZXEj8uj69YHtDOa1Vv7KpAAKy) que también podrás ejecutar desde Google Colab. 

Antes de lanzarnos a construir una visualización efectiva, debemos realizar un tratamiento previo de los datos, prestando especial atención a la obtención de los mismos y validando su contenido, asegurando que se encuentran en el formato adecuado y consistente para su procesamiento y que no contienen errores.  

Como primer paso del proceso, una vez importadas las librerías necesarias y cargados los conjuntos de datos, es necesario realizar un análisis exploratorio de los datos (EDA) con el fin de interpretar adecuadamente los datos de partida, detectar anomalías, datos ausentes o errores que pudieran afectar a la calidad de los procesos posteriores y resultados. Si quieres conocer más sobre este proceso puedes recurrir a la Guía Práctica de Introducción al Análisis Exploratorio de Datos.  

El siguiente paso a dar es generar las tablas de datos preprocesadas que usaremos en las visualizaciones. Para ello, filtraremos los conjuntos de datos iniciales y calcularemos los valores que sean necesarios y de interés para el análisis realizado en este ejercicio. 

Una vez terminado el preprocesamiento, obtendremos las tablas de datos “datos_graficas_C” y “datos_graficas_B” las cuales utilizaremos en el siguiente apartado del Notebook para generar las visualizaciones.  

La estructura del Notebook en la que se realizan los pasos previamente descritos junto a comentarios explicativos de cada uno de ellos, es la siguiente: 

1. Instalación y carga de librerías
2. Carga de los conjuntos de datos
3. Análisis exploratorio de datos (EDA)
4. Preparación de las tablas de datos
5. Visualizaciones
6. Guardado de gráficos

Podrás reproducir este análisis, ya que el código fuente está disponible en nuestra cuenta de GitHub. La forma de proporcionar el código es a través de un documento realizado sobre un Jupyter Notebook que una vez cargado en el entorno de desarrollo podrás ejecutar o modificar de manera sencilla. Debido al carácter divulgativo de este post y de cara a favorecer el entendimiento de los lectores no especializados, el código no pretende ser el más eficiente, sino facilitar su comprensión por lo que posiblemente se te ocurrirán muchas formas de optimizar el código propuesto para lograr fines similares. ¡Te animamos a que lo hagas! 

## 5. Visualizaciones
Diversos tipos de visualizaciones y gráficos se han realizado con la finalidad de extraer información sobre las tablas de datos preprocesadas y responder a las preguntas iniciales planteadas en este ejercicio. Como se ha mencionado previamente, se ha utilizado el paquete “ggplot2” de R para realizar las visualizaciones.  

El paquete "ggplot2" es una biblioteca de visualización de datos en el lenguaje de programación R. Fue desarrollado por Hadley Wickham y es parte del conjunto de herramientas del paquete "tidyverse". El paquete "ggplot2" está construido en torno al concepto de "gramática de gráficos", que es un marco teórico para construir gráficos mediante la combinación de elementos básicos de la visualización de datos como capas, escalas, leyendas, anotaciones y temas. Esto permite crear visualizaciones de datos complejas y personalizadas, con un código más limpio y estructurado. 

Si quieres tener una visión a modo resumen de las posibilidades de visualizaciones con ggplot2, consulta la siguiente [“cheatsheet”](https://github.com/rstudio/cheatsheets/blob/main/data-visualization.pdf). También puedes obtener información más en detalle en el siguiente ["manual de uso"](https://ggplot2-book.org/).

En la siguiente [carpeta](https://github.com/datosgobes/Laboratorio-de-Datos/tree/main/Visualizaciones/Analisis_datos_meteorologicos/Visualizaciones) encontrarás todas las visualizaciones generadas que se comentan en los siguientes apartados.

## 5.1 Gráficos de líneas
Los gráficos de líneas son una representación gráfica de datos que utiliza puntos conectados por líneas para mostrar la evolución de una variable en una dimensión continua, como el tiempo. Los valores de la variable se representan en el eje vertical y la dimensión continua en el eje horizontal. Los gráficos de líneas son útiles para visualizar tendencias, comparar evoluciones y detectar patrones. 

A continuación, podemos visualizar varios gráficos de líneas con la evolución temporal de los valores de temperaturas medias, mínimas y máximas de las dos estaciones meteorológicas analizadas (Córdoba y Burgos). Sobre estos gráficos, hemos introducido líneas de tendencia para poder observar de forma visual y sencilla su evolución. 

Para poder comparar las evoluciones, no solamente de manera visual mediante las líneas de tendencia graficadas, sino también de manera numérica, obtenemos los coeficientes de pendiente de la recta de tendencia, es decir, el cambio en la variable respuesta (tm_ mes, tm_min, tm_max) por cada unidad de cambio en la variable predictora (año). 

Coeficiente de pendiente temperatura media Córdoba: 0.036 
Coeficiente de pendiente temperatura media Burgos: 0.025 
Coeficiente de pendiente temperatura mínima Córdoba: 0.020 
Coeficiente de pendiente temperatura mínima Burgos: 0.020 
Coeficiente de pendiente temperatura máxima Córdoba: 0.051 
Coeficiente de pendiente temperatura máxima Burgos: 0.030 

Podemos interpretar que cuanto mayor es este valor, más abrupta es la subida de temperatura media en cada periodo observado. 

Por últimos, hemos creado un gráfico de líneas para cada estación meteorológica, en el que visualizamos de forma conjunta la evolución de las temperaturas medias, mínimas y máximas a lo largo de los años.
Las principales conclusiones obtenidas de las visualizaciones de este apartado son: 

Las temperaturas medias, mínimas y máximas anuales registradas en Córdoba y Burgos tienen una tendencia en aumento. 
El aumento más significativo se observa en la evolución de las temperaturas máximas de Córdoba​ (coeficiente de pendiente = 0.051) 
El aumento más tenue se observa en la evolución de las temperaturas mínimas, tanto de Córdoba cómo de Burgos (coeficiente de pendiente = 0.020) 


## 5.2 Gráficos de barras
os gráficos de barras son una representación gráfica de datos que utiliza barras rectangulares para mostrar la magnitud de una variable en diferentes categorías o grupos. La altura o longitud de las barras representa la cantidad o frecuencia de la variable y las categorías se representan en el eje horizontal. Los gráficos de barras son útiles para comparar la magnitud de diferentes categorías y para visualizar diferencias entre ellas. 

Hemos generado dos gráficos de barras con los datos correspondientes a la precipitación total acumulada por año para las distintas estaciones meteorológicas.
Al igual que en el apartado anterior, graficamos la línea de tendencia y calculamos el coeficiente de pendiente. 

Coeficiente de pendiente precipitaciones acumuladas Córdoba: -2.97 
Coeficiente de pendiente precipitaciones acumuladas Burgos: -0.36 

Las principales conclusiones obtenidas de las visualizaciones de este apartado son: 

Las precipitaciones acumuladas anuales tienen una tendencia en descenso tanto para Córdoba como para Burgos. 
La tendencia de descenso es mayor para Córdoba (coeficiente = -2.97), siendo más moderada para Burgos (coeficiente = -0.36) 

## 5.3 Histogramas
Los histogramas son una representación gráfica de una distribución de frecuencia de datos numéricos en un intervalo de valores. El eje horizontal representa los valores de los datos divididos en intervalos, llamados "bin", y el eje vertical representa la frecuencia o la cantidad de datos que se encuentran en cada "bin". Los histogramas son útiles para identificar patrones en los datos, como su distribución, dispersión, simetría o sesgo. 

Hemos generado dos histogramas con las distribuciones de los datos correspondientes a la precipitación total acumulada por año para las distintas estaciones meteorológicas, siendo los intervalos elegidos de 50 mm3. 

Las principales conclusiones obtenidas de las visualizaciones de este apartado son: 

Los registros de precipitación acumulada anual en Burgos presentan una distribución cercana a una distribución normal y simétrica. 
Los registros de precipitación acumulada anual en Córdoba no presentan una distribución simétrica. 

## 5.4 Diagramas de cajas y bigotes
os diagramas de cajas y bigotes, son una representación gráfica de la distribución de un conjunto de datos numéricos. Estos gráficos representan la mediana, el rango intercuartílico y los valores mínimo y máximo de los datos. La caja del gráfico representa el rango intercuartílico, es decir, el rango entre el primer y tercer cuartil de los datos. Los puntos fuera de la caja, llamados valores atípicos, pueden indicar valores extremos o datos anómalos. Los diagramas de cajas son útiles para comparar distribuciones y detectar valores extremos en los datos. 

Hemos generado un gráfico con los diagramas de cajas correspondientes a los datos de precipitaciones acumuladas de las estaciones meteorológicas. 

De cara a entender el gráfico, hay que destacar los siguientes puntos: 

Los límites de la caja indican el primer y el tercer cuartil (Q1 y Q3), que dejan por debajo de cada uno, el 25% y el 75% de los datos respectivamente.   
La línea horizontal dentro de la caja es la mediana (equivalente al segundo cuartil Q2), que deja por debajo la mitad de los datos.  
Los límites de los bigotes son los valores extremos, es decir, el valor mínimo y el valor máximo de la serie de datos. 
Los puntos fuera de los bigotes son los valores atípicos (outliers) 

Las principales conclusiones obtenidas de la visualización de este apartado son: 

Ambas distribuciones presentan 3 valores extremos, siendo significativos los de Córdoba con valores superiores a 1000 mm3. 
Los registros de Córdoba tienen una mayor variabilidad que los de Burgos, los cuales se presentan más estables. 

## 5.5 Gráficos de sectores
Un gráfico de sectores es un tipo de gráfico circular que representa proporciones o porcentajes de un todo. Se compone de varias secciones o sectores, donde cada sector representa una proporción de la totalidad del conjunto. El tamaño del sector se determina en función de la proporción que representa, y se expresa en forma de ángulo o porcentaje. Es una herramienta útil para visualizar la distribución relativa de las diferentes partes de un conjunto y facilita la comparación visual de las proporciones entre los distintos grupos. 

Hemos generamos dos gráficos de sectores (polares). El primero de ellos con el número de días que los valores superan los 30º en Córdoba y el segundo de ellos con el número de días que los valores bajan de los 0º en Burgos. 

Para la realización de estos gráficos, hemos agrupado la suma del número de días anteriormente descrito en seis grupos, correspondientes a periodos de 5 años desde 1990 hasta el 2020. 

Las principales conclusiones obtenidas de las visualizaciones de este apartado son: 

Se da un aumento del 31,9% en el total de días anuales con temperaturas superiores a 30º en Córdoba para el periodo comprendido entre el 2015-2020 respecto al periodo 1990-1995. 
Se da un aumento del 33,5% en el total de días anuales con temperaturas superiores a 30º en Burgos para el periodo comprendido entre el 2015-2020 respecto al periodo 1990-1995. 

## 5.6 Gráficos de sectores
Los gráficos de dispersión son una herramienta de visualización de datos que representan la relación entre dos variables numéricas mediante la ubicación de puntos en un plano cartesiano. Cada punto representa un par de valores de las dos variables y su posición en el gráfico indica cómo se relacionan entre sí. Los gráficos de dispersión se utilizan comúnmente para identificar patrones y tendencias en los datos, así como para detectar cualquier posible correlación entre las variables. Estos gráficos también pueden ayudar a identificar valores atípicos o datos que no encajan con la tendencia general. 

Hemos generado dos gráficas de dispersión en las que se comparan los valores de temperaturas medias máximas y medias mínimas buscando tendencias de correlación entre ambas para los valores cada estación meteorológica.

Para poder analizar las correlaciones, no solamente de manera visual mediante las gráficas, sino también de manera numérica, obtenemos los coeficientes de correlación de Pearson. Este coeficiente es una medida estadística que indica el grado de asociación lineal entre dos variables cuantitativas. Se utiliza para evaluar si existe una relación lineal positiva (ambas variables aumentan o disminuyen simultáneamente a un ritmo constante), negativa (los valores de ambas variables varían de forma contraria) o nula (sin relación) entre dos variables y la fortaleza de dicha relación, cuanto más cerca de +1, más alta es su asociación. 

Coeficiente de Pearson (Temperatura media max VS min) Córdoba: 0.15 
Coeficiente de Pearson (Temperatura media max VS min) Burgos: 0.61 

En la imagen observamos que mientras en Córdoba se aprecia una mayor dispersión, en Burgos se observa una mayor correlación. 

A continuación, modificaremos las gráficas de dispersión anteriores para que nos aporten más información de forma visual. Para ello dividimos el espacio por sectores de colores (rojo con valores de temperatura más altos/ azul valores de temperatura más bajos) y mostramos en las distintas burbujas la etiqueta con el año correspondiente. Cabe destacar que los límites de cambio de color de los cuadrantes corresponden con los valores medios de cada una de las variables. 

Las principales conclusiones obtenidas de las visualizaciones de este apartado son: 

Existe una relación lineal positiva entre la temperatura media máxima y mínima tanto en Córdoba como en Burgos, siendo mayor esta correlación en los datos de Burgos. 
Los años que presentan valores más elevados de temperaturas máximas y mínimas en Burgos son (2003, 2006 y 2020) 
Los años que presentan valores más elevados de temperaturas máximas y mínimas en Córdoba son (1995, 2006 y 2020) 

## 5.7 Matriz de correlación
La matriz de correlación es una tabla que muestra las correlaciones entre todas las variables en un conjunto de datos. Es una matriz cuadrada que muestra la correlación entre cada par de variables en una escala que va de -1 a 1. Un valor de -1 indica una correlación negativa perfecta, un valor de 0 indica que no hay correlación y un valor de 1 indica una correlación positiva perfecta. La matriz de correlación se utiliza comúnmente para identificar patrones y relaciones entre variables en un conjunto de datos, lo que puede ayudar a comprender mejor los factores que influyen en un fenómeno o resultado. 

Hemos generado dos mapas de calor con los datos de las matrices de correlación para ambas estaciones meteorológicas.

Las principales conclusiones obtenidas de las visualizaciones de este apartado son: 

Existe una fuerte correlación negativa (- 0.42) para Córdoba y (-0.45) para Burgos entre el número de días anuales con temperaturas superiores a 30º y las precipitaciones acumuladas. Esto quiere decir que conforme aumenta el número de días con temperaturas superiores a 30º disminuyen notablemente las precipitaciones.

# 6. Conclusiones del ejercicio
La visualización de datos es uno de los mecanismos más potentes para explotar y analizar el significado implícito de los datos. Como hemos observado en este ejercicio, "ggplot2" se trata de una potente librería capaz de representar una grán variedad de gráficos con un alto grado de personalización que permite ajustar numerosas caracteristicas propias de cada gráfico.

Una vez analizadas las visualizaciones anteriores, podemos concluir que tanto para la estación meteorológica de Burgos, como la de Córdoba, las temperaturas (mínimas, medias, máximas) han sufrido un aumento considerable, los días con calor extremo ( Tº > 30º) también lo han sufrido y las precipitaciones han disminuido en el periodo de tiempo analizado, desde 1990 hasta el 2020. 

Esperemos que esta visualización paso a paso te haya resultado útil para el aprendizaje de algunas técnicas muy habituales en el tratamiento, representación e interpretación de datos abiertos. Volveremos para mostraros nuevas reutilizaciones. ¡Hasta pronto! 





