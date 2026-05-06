# Descripción del Jupyter Notebook

Este cuaderno de Jupyter está diseñado para ser ejecutado en la plataforma de ciencia de datos colaborativa [Google Colab](https://colab.research.google.com/%5D). El cuaderno reproduce un flujo completo de ciencia de datos en el que el objetivo es entrenar un algoritmo de Inteligencia Artificial que sea capaz de clasificar automáticamente un conjunto de imágenes de rayos-x en dos categorías: persona enferma frente a persona no-enferma. En particular, la enfermedad escogida es pneumotorax.

El cuaderno de Jupyter, realiza las siguientes actividades diferenciadas:

1. Instalación y carga de dependencias
2. Configuración del entorno de trabajo (Google Colab)
3. Descarga, carga y ligero pre-procesamiento de datos necesarios (imágenes médicas) en el entorno de trabajo
4. Pre-visualización de las imágenes cargadas
5. Preparación de los datos para entrenamiento del algoritmo
6. Entrenamiento del modelo y resultados
7. Conclusiones del ejercicio.


# Proyectos previos


En este repositorio encontrarás toda la información necesaria para reproducir este ejercio. Hemos preparado el cuarderno de Jupyter y unos conjuntos de datos alojados en un almacenamiento remoto para que no tengas que preocuparte de nada más :smiley:. Sin embargo, no podríamos haber preparado este ejercicio sin el trabajo y el esfuerzo previo de otros entusiastas de la ciencia de datos :raised_hands: A continuación, te dejamos una pequeña nota y las referencias a estos trabajos previos. 

Este ejercicio es una adaptación del proyecto original de Michael Blum [tweeted](https://twitter.com/mblum_g/status/1475940763716444161?s=20) sobre el desafío [STOIC2021 - dissease-19 AI challenge](https://stoic2021.grand-challenge.org/stoic2021/). El proyecto original de Michael, partía de un conjunto de imágenes de pacientes con patología Covid-19, junto con otros pacientes sanos para hacer de contraste. En una segunda aproximación, [Olivier Gimenez](https://oliviergimenez.github.io/) utilizó un conjunto de datos similar al del proyecto original publicado en una competición de [Kaggle](https://en.wikipedia.org/wiki/Kaggle) (repositorio: <https://www.kaggle.com/plameneduardo/sarscov2-ctscan-dataset>). Este nuevo _dataset_ (250 MB) era considerablemente más manejable que el original (280GB). El nuevo _dataset_ contenía algo más de 1000 imágenes de pacientes sanos y enfermos. El código del proyecto de Olivier puede encontrase en el siguiente repositorio de [Github](https://github.com/oliviergimenez/bin-image-classif).

En nuestro caso, inspirándonos en estos dos fantásticos proyectos previos, hemos dado un paso más. En este proyecto, partimos de un conjunto de datos (imágenes médicas) de radio-diagnóstico que están disponibles en el repositorio abierto del [NIH](https://clinicalcenter.nih.gov/). El Centro Clínico NIH es un hospital dedicado únicamente a la investigación clínica en el campus del Instituto Nacional de Salud en Bethesda, Maryland (EEUU). En el post [10 repositorios de datos públicos relacionados con la salud y el bienestar](https://datos.gob.es/es/noticia/10-repositorios-de-datos-publicos-relacionados-con-la-salud-y-el-bienestar) se cita al NIH como uno de los orígenes de datos sanitarios de calidad.

En particular, nuestro conjunto de datos está disponible públicamente [aquí](https://nihcc.app.box.com/v/ChestXray-NIHCC/folder/36938765345). El repositorio incluye toda la información necesario para usarlo y en la descripción los autores comentan:

>El examen de rayos X de tórax es uno de los exámenes de imágenes médicas más frecuentes y rentables. Sin embargo, el diagnóstico clínico de la radiografía de tórax puede ser un desafío y, a veces, se cree que es más difícil que el diagnóstico mediante imágenes de [TC](https://es.wikipedia.org/wiki/Tomograf%C3%ADa_axial_computarizada) (Tomografía Computerizada) de tórax.

El conjunto de datos de rayos X de tórax comprende **112.120** imágenes de rayos-X (vista frontal) de **30.805** pacientes únicos. Las imágenes se acompañan con las **etiquetas asociadas de catorce enfermedades** (donde cada imagen puede tener múltiples etiquetas), extraídas de los informes radiológicos asociados utilizando procesamiento de lenguaje natural (NLP). Si quieres ampliar la información sobre el campo de procesamiento del lenguaje natural puedes consultar el [siguiente informe](https://datos.gob.es/es/documentacion/tecnologias-emergentes-y-datos-abiertos-procesamiento-del-lenguaje-natural).
