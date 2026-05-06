# Estudio sobre la alimentación en los hogares españoles

## 1. Introducción
Las visualizaciones son representaciones gráficas de datos que permiten comunicar de manera sencilla y efectiva la información ligada a los mismos. Las posibilidades de visualización son muy amplias, desde representaciones básicas, como los gráficos de líneas, de barras o de sectores, hasta visualizaciones configuradas sobre cuadros de mando interactivos.  

En esta sección de [“Visualizaciones paso a paso”](https://datos.gob.es/es/documentacion/tipo/visualizaciones-paso-paso-3923) estamos presentando periódicamente ejercicios prácticos de visualizaciones de datos abiertos disponibles en  datos.gob.es u otros catálogos similares. En ellos se abordan y describen de manera sencilla las etapas necesarias para obtener los datos, realizar las transformaciones y los análisis que resulten pertinentes para, finalmente, posibilitar la creación de visualizaciones interactivas que nos permitan obtener unas conclusiones finales a modo de resumen de dicha información. En cada uno de estos ejercicios prácticos, se utilizan sencillos desarrollos de código convenientemente documentados, así como herramientas de uso gratuito. Todo el material generado está disponible para su reutilización en el repositorio Laboratorio de datos de GitHub. 

A continuación, y como complemento a la explicación que encontrarás seguidamente, puedes acceder al código que utilizaremos en el ejercicio y que iremos explicando y desarrollando en los siguientes apartados de este post.

[Accede al repositorio del laboratorio de datos en Github](https://github.com/datosgobes/Laboratorio-de-Datos/tree/main/Visualizaciones/Estudio_alimentacion_hogares_espa%C3%B1oles).

[Ejecuta el código de pre-procesamiento de datos sobre Google Colab](https://colab.research.google.com/drive/1TH5mCsTlnTHeOgQaFLqZtpaJyootYWDc?usp=sharing).


## 2. Objetivo
El objetivo principal de este ejercicio es mostrar como generar un cuadro de mando interactivo que, partiendo de datos abiertos, nos muestre información relevante sobre el consumo en alimentación de los hogares españoles partiendo de datos abiertos. Para ello realizaremos un preprocesamiento de los datos abiertos con la finalidad de obtener las tablas que utilizaremos en la herramienta generadora de las visualizaciones para crear el cuadro de mando interactivo.  

Los cuadros de mando son herramientas que permiten presentar información de manera visual y fácilmente comprensible. También conocidos por el témino en inglés "dashboards", son utilizados para monitorizar, analizar y comunicar datos e indicadores. Su contenido suele incluir gráficos, tablas, indicadores, mapas y otros elementos visuales que representan datos y métricas relevantes. Estas visualizaciones ayudan a los usuarios a comprender rápidamente una situación, identificar tendencias, detectar patrones y tomar decisiones informadas.   

Una vez analizados los datos, mediante esta visualización podremos contestar a preguntas como las que se plantean a continuación:  

*¿Cuál es la tendencia de los últimos años en el gasto y del consumo per cápita en los distintos alimentos que componen la cesta básica? 

*¿Qué alimentos son los más y menos consumidos en los últimos años?  

*¿En qué Comunidades Autónomas se produce un mayor gasto y consumo en alimentación? 

*¿El aumento en el coste de ciertos alimentos en los últimos años ha significado una reducción de su consumo?  

Éstas, y otras muchas preguntas pueden ser resueltas mediante el cuadro de mando que mostrará información de forma ordenada y sencilla de interpretar. 


## 3. Recursos
### 3.1 Conjuntos de datos
Los conjuntos de datos abiertos utilizados en este ejercicio contienen distinta información sobre el consumo per cápita y el gasto per cápita de los principales grupos de alimentos desglosados por Comunidad Autónoma. Los conjuntos de datos abiertos utilizados, pertenecientes al [Ministerio de Agricultura, Pesca y Alimentación (MAPA)](https://www.mapa.gob.es/es/), se proporcionan en series anuales (utilizaremos las series anuales desde el 2010 hasta el 2021) 

*[Series anuales datos de consumo alimentario en hogares](https://www.mapa.gob.es/es/alimentacion/temas/consumo-tendencias/panel-de-consumo-alimentario/series-anuales/)

Estos conjuntos de datos también se encuentran disponibles para su descarga en el siguiente [repositorio de Github](https://github.com/datosgobes/Laboratorio-de-Datos/tree/main/Visualizaciones/Estudio_alimentacion_hogares_espa%C3%B1oles). 


### 3.2 Herramientas
Para la realización del preprocesamiento de los datos se ha utilizado el lenguaje de programación Python desde el servicio cloud de [Google Colab](https://colab.research.google.com/), que permite la ejecución de [Notebooks de Jupyter](https://jupyter.org/).

> Google Colab o también llamado Google Colaboratory, es un servicio gratuito en la nube de Google Research que permite programar, ejecutar y compartir código escrito en Python o R desde tu navegador, por lo que no requiere la instalación de ninguna herramienta o configuración.

Para la creación de la visualización interactiva se ha usado la herramienta [Looker Studio](https://lookerstudio.google.com/navigation/reporting).

> Looker Studio antiguamente conocido como Google Data Studio, es una herramienta online que permite realizar cuadros de mandos interactivos que pueden insertarse en sitios web o exportarse como archivos. Esta herramienta es sencilla de usar y permite múltiples opciones de personalización. 

Si quieres conocer más sobre herramientas que puedan ayudarte en el tratamiento y la visualización de datos, puedes recurrir al informe ["Herramientas de procesado y visualización de datos"](https://datos.gob.es/es/documentacion/herramientas-de-procesado-y-visualizacion-de-datos).


## 4. Tratamiento o preparación de los datos

Los procesos que te describimos a continuación los encontrarás comentados en el siguiente [Notebook](https://colab.research.google.com/drive/1TH5mCsTlnTHeOgQaFLqZtpaJyootYWDc?usp=sharing) que podrás ejecutar desde Google Colab.

Antes de lanzarnos a construir una visualización efectiva, debemos realizar un tratamiento previo de los datos, prestando especial atención a su obtención y a la validación de su contenido, asegurándonos que se encuentran en el formato adecuado y consistente para su procesamiento y que no contienen errores.   

Como primer paso del proceso, una vez cargados los conjuntos de datos iniciales, es necesario realizar un análisis exploratorio de los datos (EDA) con el fin de interpretar adecuadamente los datos de partida, detectar anomalías, datos ausentes o errores que pudieran afectar a la calidad de los procesos posteriores y resultados. Si quieres conocer más sobre este proceso puedes recurrir a la [Guía Práctica de Introducción al Análisis Exploratorio de Datos](https://datos.gob.es/es/documentacion/guia-practica-de-introduccion-al-analisis-exploratorio-de-datos).  

El siguiente paso es generar la tabla de datos preprocesada que usaremos para alimentar la herramienta de visualización (Looker Studio). Para ello modificaremos, filtraremos y uniremos los datos según nuestras necesidades. 

Los pasos que se siguen en este preprocesamiento de los datos, explicados en el Notebook de Google Colab, son los siguientes: 

*Instalación de librerías y carga de los conjuntos de datos 

*Análisis exploratorio de los datos (EDA) 

*Generación de tablas preprocesadas 

Podrás reproducir este análisis con el código fuente que está disponible en nuestra cuenta de GitHub. La forma de proporcionar el código es a través de un documento realizado sobre un Jupyter Notebook que una vez cargado en el entorno de desarrollo podrás ejecutar o modificar de manera sencilla. Debido al carácter divulgativo de este post y para favorecer el entendimiento de los lectores no especializados, el código no pretende ser el más eficiente, sino facilitar su comprensión por lo que posiblemente se te ocurrirán muchas formas de optimizar el código propuesto para lograr fines similares. ¡Te animamos a que lo hagas! 



## 5. Visualización del cuadro de mandos interactivo
Una vez hemos realizado el preprocesamiento de los datos, vamos con la generación del cuadro de mandos. Un cuadro de mandos es una herramienta visual que proporciona una visión resumida de los datos y métricas clave. Es útil para el monitoreo, la toma de decisiones y la comunicación efectiva, al proporcionar una vista clara y concisa de la información relevante. 

Para la realización de las visualizaciones interactivas que componen el cuadro de mando se ha usado la herramienta Looker Studio. Al ser una herramienta online, no es necesario tener instalado un software para interactuar o generar cualquier visualización, pero sí se necesita que la tabla de datos que le proporcionamos esté estructurada adecuadamente, razón por la que hemos realizado los pasos anteriores relativos al preprocesamiento de los datos. Si quieres saber más sobre cómo utilizar Looker Studio, en el siguiente enlace puedes acceder a [formación sobre el uso de la herramienta](https://support.google.com/looker-studio/topic/12398462?hl=es&ref_topic=6267740&sjid=12579296916849017026-EU). 

A continuación se muestra el cuadro de mandos, el cual se puede abrir en una nueva pestalla en el siguiente [link](https://lookerstudio.google.com/reporting/3aa58a05-bc36-46c3-bd4f-f7575bcd2a17/page/f2MRD). En los próximos apartados desglosaremos cada uno de los componentes que lo integran.

### 5.1 Filtros
Los filtros en un cuadro de mando son opciones de selección que permiten visualizar y analizar datos específicos mediante la aplicación de varios criterios de filtrado a los conjuntos de datos presentados en el panel de control. Ayudan a enfocarse en información relevante y a obtener una visión más precisa de los datos.  

Los filtros incluidos en el cuadro de mando generado permiten elegir el tipo de análisis a mostrar, el territorio o Comunidad Autónoma, la categoría de alimentos y los años de la muestra.  

También incorpora diversos botones para facilitar el borrado de los filtros elegidos, descargar el cuadro de mandos como un informe en formato PDF y acceder a los datos brutos con los que se ha elaborado este cuadro de mando. 

### 5.2 Visualizaciones interactivas
El cuadro de mandos está compuesto por diversos tipos de visualizaciones interactivas, que son representaciones gráficas de datos que permiten a los usuarios explorar y manipular la información de forma activa.

A diferencia de las visualizaciones estáticas, las visualizaciones interactivas brindan la capacidad de interactuar con los datos, permitiendo a los usuarios realizar diferentes e interesantes acciones como hacer clic en elementos, arrastrarlos, ampliar o reducir el enfoque, filtrar datos, cambiar parámetros y ver los resultados en tiempo real.

Esta interacción es especialmente útil cuando se trabaja con conjuntos de datos grandes y complejos, pues facilitan a los usuarios el examen de diferentes aspectos de los datos así como descubrir patrones, tendencias y relaciones de una manera más intuitiva. 

De cara a la definición de cada tipo de visualización, nos hemos basado en la [guía de visualización de datos para entidades locales](https://datos.gob.es/es/documentacion/guia-de-visualizacion-de-datos-para-entidades-locales) presentada por la RED de Entidades Locales por la Transparencia y Participación Ciudadana de la FEMP. 

#### 5.2.1 Tabla de datos
Las tablas de datos permiten la presentación de una gran cantidad de datos de forma organizada y clara, con un alto rendimiento de espacio/información.

Sin embargo, pueden dificultar la presentación de patrones o interpretaciones respecto a otros objetos visuales de carácter más gráfico.

#### 5.2.2 Mapa de cloropetas
Se trata de un mapa en el que se muestran datos numéricos por territorios marcando con intensidad de colores diferentes las distintas áreas. Para su elaboración se requiere de una medida o dato numérico, un dato categórico para el territorio y un dato geográfico para delimitar el área de cada territorio. 

#### 5.2.3 Gráfico de sectores
Se trata de un gráfico que muestra los datos a partir de unos ejes polares en los que el ángulo de cada sector marca la proporción de una categoría respecto al total. Su funcionalidad es mostrar las diferentes proporciones de cada categoría respecto a un total utilizando gráficos circulares. 

#### 5.2.4 Gráfico de líneas
Se trata de un gráfico que muestra la relación entre dos o más medidas de una serie de valores en dos ejes cartesianos, reflejando en el eje X una dimensión temporal, y una medida numérica en el eje Y. Estos gráficos son idóneos para representar series de datos temporales con un elevado número de puntos de datos u observaciones. 


#### 5.2.5 Gráfico de barras
Se trata de un gráfico de los más utilizados por la claridad y simplicidad de preparación. Facilita la lectura de valores a partir de la proporción de la longitud de las barras. El gráfico muestra los datos mediante un eje que representa los valores cuantitativos y otro que incluye los datos cualitativos de las categorías o de tiempo. 

#### 5.2.6 Gráfico de jerarquías
Se trata de un gráfico formado por distintos rectángulos que representan categorías, y que permite agrupaciones jerárquicas de los sectores de cada categoría. La dimensión de cada rectángulo y su colocación varía en función del valor de la medida de cada una de las categorías que se muestran respecto del valor total de la muestra. 

## 6. Conclusiones
Los cuadros de mando son uno de los mecanismos más potentes para explotar y analizar el significado de los datos. Cabe destacar la importancia que nos ofrecen a la hora de monitorear, analizar y comunicar datos e indicadores de una manera clara, sencilla y efectiva. 

Como resultado, hemos podido responder a las preguntas originalmente planteadas: 

*La tendencia del consumo per cápita se encuentra en disminución desde el 2013, año en el que llegó a su máximo, con un pequeño repunte en los años 2020 y 2021. 

*La tendencia del gasto per cápita se ha mantenido estable desde el 2011 hasta que en 2020 ha sufrido una subida del 17,7% pasando de ser el gasto medio anual de 1052 euros a 1239 euros, produciéndose una leve disminución del 4,4% de los datos del 2020 a los del 2021.

*Los tres alimentos más consumidos durante todos los años analizados son: frutas frescas, leche líquida y carne (valores en kgs) 

*Las Comunidades Autónomas donde el gasto per cápita es mayor son País Vasco, Cataluña y Asturias, mientras que Castilla la Mancha, Andalucía y Extremadura son las que menos gasto tienen. 

*Las Comunidad Autónomas donde un mayor consumo per cápita se produce son Castilla y León, Asturias y País Vasco, mientras que en las que menor son: Extremadura, Canarias y Andalucía. 

También hemos podido observar ciertos patrones interesantes, como un aumento de un 17,33% en el consumo de alcohol (cervezas, vino y bebidas espirituosas) en los años 2019 y 2020 .  

Puedes utilizar los distintos filtros para averiguar y buscar más tendencias o patrones en los datos según tus intereses e inquietudes. 

Esperemos que esta visualización paso a paso te haya resultado útil para el aprendizaje de algunas técnicas muy habituales en el tratamiento y representación de datos abiertos. Volveremos para mostraros nuevas reutilizaciones. ¡Hasta pronto! 
