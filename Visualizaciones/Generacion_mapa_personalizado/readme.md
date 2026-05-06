# Visualización paso a paso: Generación de mapa turístico personalizado

## 1. Introducción
Las visualizaciones son representaciones gráficas de datos que permiten comunicar de manera sencilla y efectiva la información ligada a los mismos. Las posibilidades de visualización son muy amplias, desde representaciones básicas, como puede ser un gráfico de líneas, barras o sectores, hasta visualizaciones configuradas sobre cuadros de mando o dashboards interactivos.  

En esta sección de “Visualizaciones paso a paso” estamos presentando periódicamente ejercicios prácticos de visualizaciones de datos abiertos disponibles en  datos.gob.es u otros catálogos similares. En ellos se abordan y describen de manera sencilla las etapas necesarias para obtener los datos, realizar las transformaciones y análisis que resulten pertinentes para, finalmente, la creación de visualizaciones interactivas, de las que podemos extraer información resumida en unas conclusiones finales. En cada uno de estos ejercicios prácticos, se utilizan sencillos desarrollos de código convenientemente documentados, así como herramientas de uso gratuito. Todo el material generado está disponible para su reutilización en el repositorio de GitHub.

En este ejercicio práctico, hemos realizado un sencillo desarrollo de código que está convenientemente documentado apoyandonos en herramientas de uso gratuito. 

[Accede al repositorio del laboratorio de datos en Github.](https://github.com/datosgobes/Laboratorio-de-Datos/tree/main/Visualizaciones/Generacion_mapa_personalizado)

[Ejecuta el código de pre-procesamiento de datos sobre Google Colab.](https://colab.research.google.com/drive/1MUpic-GtjNsyg-RnpJtM1eWfuhT82DAi?usp=sharing)


## 2. Objetivo
El objetivo principal de este post es mostrar cómo generar un mapa personalizado de Google Maps mediante la herramienta ["My Maps"](https://www.google.com/intl/es_ES/maps/about/mymaps/) partiendo de datos abiertos. Este tipo de mapas son altamente populares en páginas, blogs y aplicaciones del sector turístico, no obstante, la información útil proporcionada al usuario suele ser escasa.

En este ejercicio, utilizaremos el potencial de los datos abiertos para ampliar la información a mostrar en nuestro mapa y hacerlo de una forma automática. También mostraremos como realizar un enriquecimiento de los datos abiertos para añadir información de contexto que mejore significativamente la experiencia de usuario. 

Desde un punto de vista funcional, el objetivo del ejercicio es la creación de un mapa personalizado para planificar rutas turísticas por los espacios naturales de la Comunidad Autónoma de Castilla y León. Para ello se han utilizado conjuntos de datos abiertos publicados por la Junta de Castilla y León, que hemos preprocesado y adaptado a nuestras necesidades de cara a generar el mapa personalizado. 


## 3. Recursos
### 3.1 Conjuntos de datos
Los conjuntos de datos contienen distinta información turística de interés geolocalizada. Dentro del catálogo de datos abiertos de la Junta de Castilla y León, encontramos el [“diccionario de entidades”](https://datosabiertos.jcyl.es/web/jcyl/set/es/medio-ambiente/refugios/1284378322579) (sección información adicional), documento de vital importancia, ya que nos define la terminología utilizada en los distintos conjuntos de datos. 

[Miradores en espacios naturales](https://datos.gob.es/es/catalogo/a07002862-miradores-en-espacios-naturales1)
      
[Observatorios en espacios naturales](https://datos.gob.es/es/catalogo/a07002862-observatorios-en-espacios-naturales1)
      
[Refugios en espacios naturales](https://datos.gob.es/es/catalogo/a07002862-refugios-en-espacios-naturales1)
      
[Árboles en espacios naturales](https://datos.gob.es/es/catalogo/a07002862-arboles-singulares-en-espacios-naturales1)
      
[Casas del parque en espacios naturales](https://datos.gob.es/es/catalogo/a07002862-casas-del-parque-en-espacios-naturales1)
      
[Zonas recreativas en espacios naturales](https://datos.gob.es/es/catalogo/a07002862-zonas-recreativas-en-espacios-naturales1)
      
[Registro de establecimientos hoteleros](https://datosabiertos.jcyl.es/web/jcyl/set/es/turismo/alojamientos_hoteleros/1284211831639)

Estos conjuntos de datos también se encuentran disponibles en el [repositorio de Github](https://github.com/datosgobes/Laboratorio-de-Datos/tree/main/Visualizaciones/Generacion_mapa_personalizado/Conjunto_datos_origen)


### 3.2 Herramientas
Para la realización de las tareas de preprocesado de los datos se ha utilizado el lenguaje de programación Python escrito sobre un Notebook de Jupyter alojado en el servicio en la nube de Google Colab.

[Google Colab](https://colab.research.google.com/?hl=es) o también llamado Google Colaboratory, es un servicio gratuito en la nube de Google Research que permite programar, ejecutar y compartir código escrito en Python o R desde tu navegador, por lo que no requiere la instalación de ninguna herramienta o configuración.

Para la creación de la visualización interactiva se ha usado la herramienta Google My Maps.

[Google My Maps](https://www.google.com/intl/es_ES/maps/about/mymaps/) es una herramienta online que permite crear mapas interactivos que pueden ser incrustados en sitios web o exportarse como archivos. Esta herramienta es gratuita, sencilla de usar y permite múltiples opciones de personalización.  

Si quieres conocer más sobre herramientas que puedan ayudarte en el tratamiento y la visualización de datos, puedes recurrir al informe ["Herramientas de procesado y visualización de datos".](https://datos.gob.es/es/documentacion/herramientas-de-procesado-y-visualizacion-de-datos)


## 4. Tratamiento o preparación de los datos
Los procesos que te describimos a continuación los encontrarás comentados en el [Notebook](https://colab.research.google.com/drive/1MUpic-GtjNsyg-RnpJtM1eWfuhT82DAi?usp=sharing)  que podrás ejecutar desde Google Colab.

Antes de lanzarnos a construir una visualización efectiva, debemos realizar un tratamiento previo de los datos, prestando especial atención a la obtención de los mismos y validando su contenido, asegurando que se encuentran en el formato adecuado y consistente para su procesamiento y que no contienen errores.  

Como primer paso del proceso es necesario realizar un análisis exploratorio de los datos (EDA) con el fin de interpretar adecuadamente los datos de partida, detectar anomalías, datos ausentes o errores que pudieran afectar a la calidad de los procesos posteriores y resultados. Si quieres conocer más sobre este proceso puedes recurrir a la Guía Práctica de Introducción al Análisis Exploratorio de Datos.  

El siguiente paso a dar es generar las tablas de datos preprocesados que usaremos para alimentar el mapa. Para ello, transformaremos los sistemas de coordenadas, modificaremos y filtraremos la información según nuestras necesidades. 

Los pasos que se siguen en este preprocesamiento de los datos, explicados en el [Notebook](https://colab.research.google.com/drive/1MUpic-GtjNsyg-RnpJtM1eWfuhT82DAi?usp=sharing), son los siguientes: 
1. Instalación y carga de librerías
2. Carga de los conjuntos de datos
3. Análisis exploratorio de datos (EDA)
4. Preprocesamiento de los conjuntos de datos​
4.1 Transformación de coordenadas
4.2 Filtrado de la información
4.3 Representación gráfica de los conjuntos de datos
4.4 Almacenamiento de las nuevas tablas de datos transformadas

Durante el preprocesado de las tablas de datos, hay que hacer un cambio de sistema de coordenadas ya que en los conjuntos de datos de origen el sistema en el que se encuentran es ESTR89 (sistema estándar que se usa en la Unión Europea), mientras que las necesitaremos en el sistema WGS84 (sistema usado por Google My Maps entre otras aplicaciones geográficas). La forma de realizar este cambio de coordenadas se encuentra explicado en el Notebook. Si quieres saber más sobre tipos y sistemas de coordenadas, puedes recurrir a la [“Guía de datos espaciales”](https://datos.gob.es/es/documentacion/guia-practica-para-la-publicacion-de-datos-espaciales) 

Una vez terminado el preprocesamiento, obtendremos las tablas de datos "recreativas_parques_naturales.csv", "alojamientos_rurales_2estrellas.csv", "refugios_parques_naturales.csv", "observatorios_parques_naturales.csv", "miradores_parques_naturales.csv", "casas_del_parque.csv", "arboles_parques_naturales.csv" las cuales incluyen campos de información genéricos y comunes como: nombre, observaciones, geoposición, … junto a campos de información específicos, los cuales se definen en detalle en el apartado 6.2 Personalización de la información a mostrar en el mapa.

Podrás reproducir este análisis, ya que el código fuente está disponible en nuestra cuenta de GitHub. La forma de proporcionar el código es a través de un documento realizado sobre un Jupyter Notebook que una vez cargado en el entorno de desarrollo podrás ejecutar o modificar de manera sencilla. Debido al carácter divulgativo de este post y para favorecer el entendimiento de los lectores no especializados, el código no pretende ser el más eficiente, sino facilitar su comprensión por lo que posiblemente se te ocurrirán muchas formas de optimizar el código propuesto para lograr fines similares. ¡Te animamos a que lo hagas! 


## 5. Enriquecimiento de los datos
Con la finalidad de aportar mayor información relacionada, se realiza un proceso de enriquecimiento de datos sobre el conjunto de datos “registro de alojamientos hoteleros” explicado a continuación. Con este paso vamos a lograr añadir de forma automática información complementaria que no está inicialmente incluida. Con ello, conseguiremos mejorar la experiencia del usuario durante su uso del mapa al proporcionar información de contexto relacionada con cada punto de interés. 

Para ello vamos a utilizar una herramienta útil para este tipo de tarea, OpenRefine. Esta herramienta de código abierto permite realizar múltiples acciones de preprocesamiento de datos, aunque en esta ocasión la usaremos para llevar a cabo un enriquecimiento de nuestros datos mediante la incorporación de contexto enlazando automáticamente información que reside en el popular repositorio de conocimiento Wikidata.  

Una vez instalada la herramienta en nuestro ordenador, al ejecutarse se abrirá una aplicación web en el navegador, en caso de que eso no ocurriese, se accedería a dicha aplicación tecleando en la barra de búsqueda del navegador http://localhost:3333. 

A continuación, se detallan los pasos a seguir. 

* Paso 1: 
Carga del CSV en el sistema (Figura 1). En esta caso, el conjunto de datos “Registro de alojamientos hoteleros”.

[Figura 1. Carga de archivo CSV en OpenRefine](https://github.com/datosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Generacion_mapa_personalizado/Imagenes/OpenRefine1.PNG)

* Paso 2: 
Creación del proyecto a partir del CSV cargado (Figura 2). OpenRefine se gestiona mediante proyectos (cada CSV subido será un proyecto), que se guardan en el ordenador dónde se esté ejecutando OpenRefine para un posible uso posterior. En este paso debemos dar un nombre al proyecto y algunos otros datos, como el separador de columnas, aunque lo más habitual es que estos últimos ajustes se rellenen automáticamente. 

[Figura 2. Creación de un proyecto en OpenRefine](https://github.com/datosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Generacion_mapa_personalizado/Imagenes/OpenRefine2.PNG)

* Paso 3: 
Enlazado (o reconciliación, usando la nomenclatura de OpenRefine) con fuentes externas. OpenRefine nos permite enlazar recursos que tengamos en nuestro CSV con fuentes externas como Wikidata. Para ello se deben realizar las siguientes acciones: 
Identificación de las columnas a enlazar. Habitualmente este paso suele estar basado en la experiencia del analista y su conocimiento de los datos que se representan en Wikidata. Como consejo, de forma genérica se podrán reconciliar o enlazar aquellas columnas que contengan información de carácter más global o general como nombres de países, calles, distritos, etc., y no se podrán enlazar aquellas columnas como coordenadas geográficas, valores numéricos o taxonomías cerradas (tipos de calles, por ejemplo). En este ejemplo, disponemos de la columna “municipios” que contiene el nombre de los municipios españoles. 
Comienzo de la reconciliación. (Figura 3) Comenzamos la reconciliación y seleccionamos la fuente por defecto que estará disponible: Wikidata(en). Después de hacer clic en Start Reconciling, automáticamente comenzará a buscar la clase del vocabulario de Wikidata que más se adecue basado en los valores de nuestra columna.

[Figura 3. Selección de la clase que mejor representa los valores de la columna "municipio"](https://github.com/datosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Generacion_mapa_personalizado/Imagenes/OpenRefine3.PNG)

Obtención de los valores de la reconciliación. OpenRefine nos ofrece la posibilidad de mejorar el proceso de reconciliación agregando algunas características que permitan orientar el enriquecimiento de la información con mayor precisión. 

Paso 4:
Generar una nueva columna con los valores reconciliados o enlazados. (Figura 4) Para ello debemos pulsar en la columna “municipio” e ir a “Edit Column → Add column based in this column”, dónde se mostrará un texto en la que tendremos que indicar el nombre de la nueva columna (en este ejemplo podría ser “wikidata”). En la caja de expresión deberemos indicar: “http://www.wikidata.org/entity/”+cell.recon.match.id y los valores aparecen como se previsualiza en la Figura.  “http://www.wikidata.org/entity/” se trata de una cadena de texto fija para representar las entidades de Wikidata, mientras el valor reconciliado de cada uno de los valores lo obtenemos a través de la instrucción cell.recon.match.id, es decir, cell.recon.match.id(“Adanero”) = Q1404668 
Mediante la operación anterior, se generará una nueva columna con dichos valores. Con el fin de comprobar que se ha realizado correctamente, haciendo clic en una de las celdas de la nueva columna, está debería conducir a una página web de Wikidata con información del valor reconciliado.  

[Figura 4. Generación de nueva columna con valores reconciliados](https://github.com/datosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Generacion_mapa_personalizado/Imagenes/OpenRefine4.PNG)

* Paso 5:
El proceso lo repetimos modificando en el paso 4 el “Edit Column → Add column based in this column” por “Add columns from reconciled values” (Figura 5). De esta forma, podremos elegir la propiedad de la columna reconciliada.  
En este ejercicio hemos elegido la propiedad “image” con identificador P18 y la propiedad “population” con identificador P1082. No obstante, podríamos añadir todas las propiedades que consideremos útiles, como el número de habitantes, el listado de monumentos de interés, etc. Cabe destacar que al igual que enriquecemos los datos con Wikidata, podemos hacerlo con otros servicios de reconciliación.
En el caso de la propiedad “image”, debido a la visualización, queremos que el valor de las celdas tenga forma de link, por lo que hemos realizado varios ajustes. Estos ajustes han sido la generación de varias columnas según los valores reconciliados, adecuación de las columnas mediante comandos en lenguaje GREL (lenguaje propio de OpenRefine) y unión de los diferentes valores de ambas columnas. Puedes consultar estos ajustes y más técnicas para mejorar tu manejo de OpenRefine y adaptarlo a tus necesidades en el siguiente User Manual. 

[Figura 5. Elección propiedad para reconciliación](https://github.com/datosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Generacion_mapa_personalizado/Imagenes/OpenRefine5.PNG)

## 6. Visualización del mapa
### 6.1 Generación del mapa con "Google My Maps"
* Iniciamos sesión con una cuenta Google y vamos a "Google My Maps", teniendo acceso de forma gratuita sin tener que descargar ningún tipo de software. 
* Importamos las tablas de datos preprocesados, uno por cada nueva capa que añadimos al mapa. Google My Maps permite importar archivos CSV, XLSX, KML y GPX (Figura 6), los cuales deberán tener asociada información geográfica. Para realizar este paso, primero se debe crear una capa nueva desde el menú de opciones lateral.

[Figura 6. Importación de archivos en "Google My Maps"](https://github.com/datosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Generacion_mapa_personalizado/Imagenes/MyMaps1.PNG)

* En este caso práctico, importaremos tablas de datos preprocesados que contienen una variable con la latitud y otra con la longitud. Esta información geográfica se reconocerá automáticamente. My Maps también reconoce direcciones, códigos postales, países, ...

[Figura 7. Selección columnas con valores de posición](https://github.com/datosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Generacion_mapa_personalizado/Imagenes/MyMaps2.PNG)

* Mediante la opción de editar estilo que aparece en el menú lateral izquierdo, en cada una de las capas, podemos personalizar los pines, editando el color y su forma.

[Figura 8. Edicción de pines de posición](https://github.com/datosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Generacion_mapa_personalizado/Imagenes/MyMaps3.PNG)

* Por último, podemos elegir el mapa base que queremos visualizar en la parte inferior de la barra lateral de opciones. 

[Figura 9. Selección de mapa base](https://github.com/datosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Generacion_mapa_personalizado/Imagenes/MyMaps4.PNG)

Si quieres conocer más sobre los pasos para la generación de mapas con “Google My Maps”, consulta el siguiente [tutorial paso a paso.](https://www.google.com/earth/outreach/learn/visualize-your-data-on-a-custom-map-using-google-my-maps/) 

### 6.2 Personalización de la información a mostrar en el mapa
Durante el preprocesamiento de las tablas de datos, hemos realizado un filtrado de la información según el enfoque del ejercicio, que es la generación de un mapa para realizar rutas tusísticas por los espacios naturales de Castilla y León. A continuación, se describe la personalización de la información que hemos llevado a cabo para cada uno de los conjuntos de datos. 
* En el conjunto de datos perteneciente a los árboles singulares de los espacios naturales, la información a mostrar para cada registro es el nombre, las observaciones, la señalización y la posición (latitud/longitud) 
* En el conjunto de datos perteneciente a las casas del parque de los espacios naturales, la información a mostrar para cada registro es el nombre, las observaciones, la señalización, el acceso, la web y la posición (latitud/longitud) 
* En el conjunto de datos perteneciente a los miradores de los espacios naturales, la información a mostrar para cada registro es el nombre, las observaciones, la señalización, el acceso y la posición (latitud/longitud) 
* En el conjunto de datos perteneciente a los observatorios de los espacios naturales, la información a mostrar para cada registro es el nombre, las observaciones, la señalización y la posición (latitud/longitud) 
* En el conjunto de datos perteneciente a los refugios de los espacios naturales, la información a mostrar para cada registro es el nombre, las observaciones, la señalización, el acceso y la posición (latitud/longitud). Dado que los refugios pueden encontrarse en estados muy diferentes y que algunos registros no ofrecen información en el campo “observaciones”, hemos decidido filtrar para que nos muestre solamente aquellos que tengan información en dicho campo. 
* En el conjunto de datos perteneciente a las áreas recreativas de los espacios naturales, la información a mostrar para cada registro es el nombre, las observaciones, la señalización, el acceso y la posición (latitud/longitud).  Hemos decidido filtrar para que nos muestre solamente aquellos que tengan información en los campos de “observaciones” y “acceso”. 
* En el conjunto de datos perteneciente a los alojamientos, la información a mostrar para cada registro es el nombre, tipo de establecimiento, categoría, municipio, web, teléfono y la posición (latitud/longitud). Hemos filtrado el “tipo” de establecimiento para que nos muestre solamente los que están categorizados como alojamientos de turismo rural y hemos filtrado para que nos muestre los que son de 2 estrellas. 
A continuación, tenemos la [visualización del mapa personalizado](https://www.google.com/maps/d/viewer?mid=1iqx-9Rpueb-YXehyNAGRHJWyKXSJaIk&ll=41.68387617058557%2C-4.671331899999988&z=7) que hemos creado. Seleccionando el icono para agrandar el mapa que aparece en la esquina superior derecha, podrás acceder su visualización en pantalla completa.

### 6.3 Funcionalidades sobre el mapa (capas, pines, rutas y vista inmersiva 3D)
En este punto, una vez creado el mapa personalizado, explicaremos diversas funcionalidades que nos ofrece "Google My Maps" durante la visualización de los datos.
* Capas: Mediante el menú desplegable de la izquierda, podemos activar y desactivar las capas a mostrar según nuestras necesidades. 

[Figura 10. Capas en "My Maps"](https://github.com/datosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Generacion_mapa_personalizado/Imagenes/MyMaps5.PNG)

* Pines: Pinchando en cada uno de los pines del mapa podemos acceder a la información asociada a esa posición geográfica.

[Figura 11. Pines en "My Maps"](https://github.com/datosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Generacion_mapa_personalizado/Imagenes/MyMaps6.PNG)

* Rutas: Podemos crear una copia del mapa sobre la que añadir nuestros recorridos personalizados.  
En las opciones del menú lateral izquierdo, seleccionamos “copiar mapa”. Una vez copiado el mapa, mediante el símbolo de añadir indicaciones, situado debajo de la barra buscador, generaremos una nueva capa. A esta capa podremos indicarle dos o más puntos, junto al medio de transporte y nos creará el trazado junto a las indicaciones de trayecto. 

[Figura 12. Rutas en "My Maps"](https://github.com/datosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Generacion_mapa_personalizado/Imagenes/MyMaps7.PNG)

* Mapa inmersivo en 3D: Mediante el símbolo de opciones que aparece en el menú lateral, podemos acceder a Google Earth, desde donde podemos realizar una exploración del mapa inmersiva en 3D, destacando el poder observar la altitud de los distintos puntos de interés. También puedes acceder mediante el siguiente enlace.

[Figura 13. Rutas en "My Maps"](https://github.com/datosgobes/Laboratorio-de-Datos/blob/main/Visualizaciones/Generacion_mapa_personalizado/Imagenes/MyMaps8.PNG)

## 7. Conclusiones del ejercicio
La visualización de datos es uno de los mecanismos más potentes para explotar y analizar el significado implícito de los datos. Cabe destacar la vital importancia que los datos geográficos tienen en el sector del turismo, lo cual hemos podido comprobar en este ejercicio. 

Como resultado, hemos desarrollado un mapa interactivo con información aportada por los datos abiertos enriquecidos (Linked Data), la cual hemos personalizado según nuestros intereses. 

Esperemos que esta visualización paso a paso te haya resultado útil para el aprendizaje de algunas técnicas muy habituales en el tratamiento y representación de datos abiertos. Volveremos para mostraros nuevas reutilizaciones. ¡Hasta pronto! 
