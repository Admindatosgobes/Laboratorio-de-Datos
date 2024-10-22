# Word Embeddings - Ejercicio práctico con etiquetas de Datos.gob

## Descripción del Proyecto

Este proyecto tiene como objetivo realizar una prueba de concepto sobre el uso de técnicas avanzadas de procesamiento de lenguaje natural, específicamente embeddings semánticos y el tesauro Eurovoc, para la mejora del etiquetado de los conjuntos de datos registrados en datos.gob.es.

## Visión General

El portal datos.gob.es ofrece una valiosa colección de conjuntos de datos públicos. Sin embargo, el sistema actual de etiquetado presenta algunas inconsistencias debido a la entrada manual de datos por diferentes usuarios. Este proyecto demuestra una prueba de concepto para optimizar las sugerencias de etiquetas utilizando:

1. Embeddings de palabras (GloVe-Twitter-50)
2. Análisis de similitud semántica
3. Integración del tesauro Eurovoc

## Características Principales

- **Recolección de datos**: utiliza la API pública de datos.gob.es para obtener información sobre los conjuntos de datos.
- **Análisis de similitud semántica**: emplea embeddings para comparar títulos y descripciones de los datasets.
- **Recomendación de etiquetas**: sugiere etiquetas basadas en datasets similares identificados.
- **Integración con eurovoc**: incorpora términos estandarizados del tesauro Eurovoc para mejorar la consistencia del etiquetado.
- **Visualización**: utiliza Graphviz para representar gráficamente el proceso de recomendación.

