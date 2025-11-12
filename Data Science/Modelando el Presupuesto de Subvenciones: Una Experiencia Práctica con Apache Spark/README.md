# Introducción

En este laboratorio práctico nos familiarizaremos con **Apache Spark**, una de las plataformas más utilizadas para el procesamiento y análisis de grandes volúmenes de datos. A través de un ejercicio guiado, trabajaremos con el dataset abierto del **Sistema Nacional de Publicidad de Subvenciones y Ayudas Públicas (BDNS)**, que recoge cientos de miles de convocatorias de subvenciones publicadas en España.

Durante el desarrollo del ejercicio aprenderemos a cargar, transformar y explorar datos en Spark, así como a construir un modelo de **machine learning** capaz de predecir el rango de presupuesto de una convocatoria en función de variables como el órgano convocante, la región o el tipo de beneficiario.

Este ejercicio te permitirá entender cómo funciona Spark en la práctica, cómo se estructuran sus DataFrames y pipelines de machine learning, y cómo aplicar técnicas de clasificación sobre datos categóricos y numéricos.

En este README encontrarás las instrucciones paso a paso para realizar el laboratorio práctico. El repositorio incluye dos carpetas principales: una con las imágenes utilizadas para facilitar el seguimiento del ejercicio, y otra, denominada **Código**, que contiene los recursos técnicos como el **Notebook** y otros ficheros relevantes.

# Caso de uso

Para ello, vamos a representar un caso de uso real en el que una administración pública desea analizar el histórico de subvenciones gestionadas en España. El organismo cuenta con un dataset procedente del Sistema Nacional de Publicidad de Subvenciones (BDNS) que recoge información sobre cientos de miles de convocatorias: quién las convoca, a qué tipo de beneficiarios van dirigidas, en qué regiones se aplican y qué presupuesto tienen asignado.

El objetivo es aprovechar estas características para **predecir el rango de presupuesto de nuevas convocatorias**, de manera que sea posible anticipar si se trata de ayudas pequeñas, medianas o de gran volumen. Esto permitiría a analistas y responsables de gestión obtener una visión más clara de cómo se distribuyen los fondos públicos y qué factores influyen en esa distribución.

# RECURSOS  

En este apartado indicamos los elementos necesarios para poder realizar el ejercicio:  

## 🛠 Herramientas  

- **Lenguaje de programación:** Python.  
- **Plataforma:** [Google Colab](https://colab.research.google.com/) – entorno interactivo que permiten crear y compartir documentos con código, visualizaciones y texto explicativo.  
- **Principales librerías y módulos:**  
    - Procesamiento distribuido y machine learning: [Apache Spark](https://spark.apache.org/) (PySpark), librería de código abierto para el procesamiento de grandes volúmenes de datos y la construcción de modelos de aprendizaje automático a escala.  
    - Manipulación de datos adicionales: [Pandas](https://pandas.pydata.org/), para conversiones y muestreo de datos.  
    - Visualización de datos: [Plotly](https://plotly.com/python/): librería para crear gráficos interactivos y dinámicos de alta calidad.  

## 💾 Conjuntos de datos  

Datos de **convocatorias de subvenciones y ayudas públicas en España** publicados en el **Sistema Nacional de Publicidad de Subvenciones (BDNS)**.  
Disponibles vía:  
- [Portal de Subvenciones](https://www.infosubvenciones.es/) del Ministerio de Hacienda y Función Pública.  

<sub>*Los datos utilizados en este ejercicio fueron descargados el 28 de agosto de 2025. La reutilización de los datos del Sistema Nacional de Publicidad de Subvenciones y Ayudas Públicas está sujeta a las condiciones legales recogidas en [https://www.infosubvenciones.es/bdnstrans/GE/es/avisolegal](https://www.infosubvenciones.es/bdnstrans/GE/es/avisolegal).* </sub>

# Desarrollo del Ejercicio
¡Pasamos a la acción! Una vez completados los pasos previos, procedemos a desarrollar el ejercicio. Como indicamos en la sección anterior, esta parte del ejercicio la realizaremos sobre un Notebook de Python el cual encontrarás en la carpeta *Código* con el nombre *Notebook.ipynb*. 

Si deseas tan solo revisar el Notebook en Colab sin proceder a su ejecución puedes encontrarlo [aquí](https://colab.research.google.com/github/Admindatosgobes/Laboratorio-de-Datos/blob/main/Data%20Science/Modelando%20el%20Presupuesto%20de%20Subvenciones%3A%20Una%20Experiencia%20Práctica%20con%20Apache%20Spark/Codigo/Notebook.ipynb).
