## Laboratorio de Datos

### Visualizaciones

#### [Cómo crear nubes de palabras a partir de un texto utilizando técnicas de PLN](https://datos.gob.es/es/documentacion/como-crear-nubes-de-palabras-partir-de-un-texto-utilizando-tecnicas-de-pln)

El objetivo principal de este post es realizar una visualización paso a paso que incluya imágenes generadas a partir de conjuntos de palabras representativas de diversos textos, conocidas popularmente como "nubes de palabras". Para este ejercicio práctico hemos escogido 6 posts publicados [en la sección de blog del portal de datos.gob.es](https://datos.gob.es/es/blog). A partir de estos textos y utilizando técnicas de PLN generamos una nube de palabras para cada  texto que nos permitirá detectar de manera sencilla y visual la frecuencia e importancia de cada palabra, facilitando la identificación de las palabras clave y la temática principal de cada uno de los posts. 

El post está dividido en cuatro apartados principales: 

 1. **Recursos**

**Herramientas:** Para la realización del tratamiento previo de los datos y la visualización de la nube de palabras, se utiliza [Python (versión 3.7)](https://www.python.org/) y [Jupyter Notebook (versión  6.1)](https://jupyter.org/). Para abordar las tareas relacionadas con el Procesamiento del Lenguaje Natural (PLN), utilizamos dos librerías, [Stickit-Learn](https://scikit-learn.org/stable/) y [wordcloud](https://amueller.github.io/word_cloud/index.html). 

**Conjuntos de datos:** para este análisis se han seleccionado 6 posts publicados recientemente en el portal de datos abiertos datos.gob.es, en su sección de [blog](https://datos.gob.es/es/blog): 

 - [Lo último en el procesamiento del lenguaje natural: resúmenes de obras clásicas en tan solo unos cientos de palabras](https://datos.gob.es/es/blog/lo-ultimo-en-procesamiento-del-lenguaje-natural-resumenes-de-obras-clasicas-en-tan-solo-unos).
 - [La importancia de la anonimización y la privacidad de datos](https://datos.gob.es/es/blog/la-importancia-de-la-anonimizacion-y-la-privacidad-de-datos).
 - [El valor de los datos en tiempo real a través de un ejemplo práctico](https://datos.gob.es/es/blog/el-valor-de-los-datos-en-tiempo-real-traves-de-un-ejemplo-practico).
 - [Nuevas iniciativas para abrir y aprovechar datos para investigación en salud](https://datos.gob.es/es/blog/nuevas-iniciativas-para-abrir-y-aprovechar-datos-para-investigacion-en-salud).
 - [Kaggle y otras plataformas alternativas para aprender ciencia de datos](https://datos.gob.es/es/blog/kaggle-y-otras-plataformas-alternativas-para-aprender-ciencia-de-datos).
 - [La infraestructura de Datos Espaciales de España (IDEE), un referente de la información geoespacial](https://datos.gob.es/es/blog/la-infraestructura-de-datos-espaciales-de-espana-idee-un-referente-de-la-informacion).

		
 2. **Tratamiento de datos**

Para la realización de una visualización efectiva, debemos realizar un preprocesamiento de los datos con el fin de conocer la realidad de los datos a los que nos enfrentamos. Un tratamiento previo de los datos es esencial para que los análisis o las visualizaciones que se realicen posteriormente sean consistentes y efectivas.
Antes de comenzar el preprocesamiento de datos, en el directorio de trabajo debemos tener: (a) una carpeta denominada "post" que contendrá todos los archivos en formato TXT con los cuales vamos a trabajar y que están disponibles en este repositorio; (b) un archivo denominado "stop_words_spanish.txt" que contiene el listado de las stop words en español, que también está disponible en este repositorio y (c) una carpeta llamada "imagenes" donde guardaremos las imágenes de las nubes de palabras en formato PNG. 
El código en Python generado en este apartado, esta suministrado en esta sección de **"Laboratorio de datos"**, una vez cargado en el entorno de desarrollo, podrá ejecutarse o modificarse de manera sencilla si se desea. 
 
 3. **Creación de la nube de palabras**
 
Una vez que hemos realizado un preprocesamiento del texto, crearemos una nube de palabras o "WordCloud" para cada uno de los textos analizados. 

4. **Conclusiones**

El post finaliza con un listado de conclusiones obtenidas a partir del análisis y visualización de los datos. 



*Nota: El código publicado pretende ser una guía para el lector, no está diseñado para maximizar su eficiencia, sino para facilitar su comprensión y puede requerir de dependencias externas o configuraciones específicas para cada usuario que desee ejecutarlo.*
