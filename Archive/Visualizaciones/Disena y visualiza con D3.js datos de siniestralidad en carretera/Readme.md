# Diseña y visualiza con D3.js datos de siniestralidad en carretera

## Descripción

En este repositorio se encuentran el dataset de entrada con los datos de siniestralidad en carretera recopilados por la Dirección General de Tráfico (DGT), el código en Python tanto para su lectura como para su procesamiento así como los ficheros de salida en formato JSON para su visualización utilizando la librería de Javascript D3.js a través de notebooks en Observable. 

A partir de los datos disponibles para el año 2024 es posible **extraer métricas cuantitativas** para hacernos una idea de las situaciones y consecuencias de los accidentes de tráfico a lo largo del tiempo.

En la base de datos encontramos más de cien mil accidentes **agregados por días de la semana**, con información respecto al número total de víctimas (fallecidos, heridos graves o heridos leves en horizontes temporales tanto de 24h como de 30 días) y respecto al **tipo de accidente, tipo de vía, titularidad de la vía y municipio**.

En este ejercicio realizaremos una serie de operaciones sencillas utilizando Python para poder extraer las métricas de nuestro interés en formato JSON, para su posterior visualización en Javascript, en concreto en D3.js.

## Análisis en Python

El objetivo de este ejercicio es la visualización de varias de las variables que caracterizan la siniestralidad en carretera. Para ello el ejericio se estructura en tres pasos en esta etapa a desarrollar en Python:

1.  Lectura del fichero de datos de la DGT
    *  Creación de un Dataframe
    *  Creacion de una fecha para cada entrada

2.  Cálculo de las métricas para caracterizar los datos disponibles
    *   Suma del total de víctimas en cada hora del día
    *   Suma de accidentes por categoría
    *   Asignación de valores a los municipios

3.  Exportar las métricas en formato JSON

## Visualización en D3.js via Observable

Una vez obtenemos las métricas ordenadas en diferentes ficheros de salida, pasamos la visualización de las mismas desarrollando visualizaciones en D3.js, en concreto: 

*   **Serie temporal** con el número total de víctimas en cada hora y día de la semana, con un menú desplegable interactivo para seleccionar el día de la semana de interés. A mayores de la curva que describe el número de víctimas dibujaremos sobre el fondo de la gráfica la incertidumbre de todos los días de la semana, de forma que la serie temporal diaria queda enmarcada en el contexto de toda la semana como referencia.  
 
*   **Mapa** de la provincia de Valencia con el número total de accidentes por municipio. 

*   **Diagrama de burbujas**, con las diferentes magnitudes de los diferentes tipos de accidentes con el número total de accidentes en cada caso escrita de forma detallada. 

*   **Diagrama de puntos apilados**, donde acumulamos círculos o cualquier otra forma geométrica para las diferentes titularidades de la vía y su número total de accidentes dentro del marco de cada titularidad. 

## Lecciones aprendidas 

A través de estos pasos aprenderemos toda una serie de habilidades transversales que nos permiten trabajar con aquellos conjunto de datos que se nos presentan en formato CSV en columnas, un formato muy popular para el cual podremos realizar tanto su análisis como su visualización. Estas lecciones son en concreto:  

*   **Universalidad de lectura y estructuración de datos**: el uso de herramientas como Python, con sus librerías Numpy y Pandas, permiten acceder a los datos en detalle y estructurarlos de forma ordenada e intuitiva con pocas líneas de código. 

*   **Cálculos sencillos en Pandas**: la propia librería de Python permite cálculos sencillos pero esenciales para la interpretación preliminar de resultados.  

*   **Formato Datetime**: a través de esta librería de Python podemos familiarizarnos con el estándar del formato de fecha, y así realizar todo tipo de transformaciones, filtros y selecciones que más nos interesen en cualquier intervalo temporal.   

*   **Formato JSON**: una vez que decidimos dar espacio a nuestras visualizaciones en la web, aprender la estructura y uso del formato JSON es de gran utilidad dado su amplio uso en todo tipo de aplicaciones y arquitecturas web.  

*   **Espectro de posibilidades de D3.js**: esta librería de Javascript nos permite explorar de lo más tradicional y conservador a lo más creativo gracias a sus principios basados en las formas más básicas, sin plantillas, templates o diagramas predefinidos.  
 
## Conclusiones y próximos pasos 

Hemos aprendido a leer y a estructurar datos según los estándares de los formatos más utilizados en el mundo del análisis y visualización. Este ejercicio también sirve como módulo introductorio al mundo de D3.js, una herramienta muy versátil, vigente y popular dentro del mundo del storytelling y la visualización de datos a todos los niveles.  

Para poder avanzar en este ejercicio se recomienta:  

*   **Para los analistas y desarrolladores**, se puede prescindir de la librería Pandas y estructurar los datos con objetos más elementales de Python como arrays y matrices, buscando qué funciones y qué operadores permiten realizar las mismas tareas que hace Pandas pero de una forma más fundamental, sobre todo si pensamos en entornos de producción para los cuales necesitamos el menor número de librerías posibles para aligerar la aplicación.  

*   **Para los creadores de visualizaciones**, la información sobre los municipios puede proyectarse igualmente sobre bases cartográficas ya existentes como OpenStreetMap y de esta forma vincular la incidencia de accidentes a características orográficas o infraestructuras ya reflejadas en esas bases cartográficas. Para las magnitudes de los números de accidentes se pueden explorar diagramas de tipo Treemap o diagramas de Voronoi y ver si transmiten el mismo mensaje que los que presentamos en este ejercicio.  

## Ámbitos de aplicación 

Los pasos descritos en este ejercicio pueden pasar a formar parte de cualquier caja de herramientas de uso habitual para los siguientes perfiles:  

*   **Analistas de datos**: aquí se encuentran los pasos básicos para la descripción de un fichero de datos en formato CSV y los cálculos básicos a realizar tanto en el campo de la fecha como de operaciones entre variables de diferentes columnas. Estas herramientas pueden servir para introducirse en el mundo del análisis de datos y ayuda en esos primeros pasos a la hora de enfrentarse a un dataset.  

*   **Científicos y personal investigador**: la universalidad de las herramientas aquí descritas aplican a una gran variedad de origen de datos, como el que se experimenta en las ciencias experimentales y de observaciones o medidas de todo tipo. Estas herramientas permiten un análisis rápido a la vez que riguroso sin importar el campo de conocimiento en el que se trabaje. 

*   **Desarrolladores web**: la exportación de datos en formato JSON así como el código en Javascript que se ofrece en los notebooks de Observable son fácilmente integrables en todo tipo de entornos (Svelte, React, Angular, Vue) y permite la creación de visualizaciones en una web de forma sencilla e intuitiva. 

*   **Periodistas**: abarcar todo el proceso de vida de un fichero de datos, desde su lectura a su visualización, otorga al periodista o investigador independencia a la hora de evaluar e interpretar los datos por sí mismo sin depender de recursos técnicos ajenos. La creación del mapa por municipios abre la puerta a utilizar cualquier otro dato similar, como por ejemplo procesos electorales, con el mismo formato de salida para mostrar variabilidad geográfica respecto a cualquier tipo de magnitud.  

*   **Diseñadores Gráficos**: el manejo de herramientas de visualización con un amplio grado de libertad permite a los diseñadores cultivar toda su creatividad dentro del rigor y la exactitud que los datos necesitan. 