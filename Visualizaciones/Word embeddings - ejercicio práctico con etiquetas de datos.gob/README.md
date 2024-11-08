# Word Embeddings - Ejercicio práctico de tratamiento de etiquetas

## Descripción
Este ejercicio práctico explora el uso de *embeddings* para la optimización y estandarización de etiquetas en portales de datos abiertos, utilizando como caso de estudio el portal [datos.gob.es](https://datos.gob.es/es/catalogo).

## Marco Teórico

### Word Embeddings
Los *word embeddings* son representaciones vectoriales de palabras en un espacio multidimensional. A diferencia de las representaciones tradicionales (como one-hot encoding), los *embeddings* capturan relaciones semánticas entre palabras, permitiendo operaciones matemáticas que reflejan relaciones lingüísticas.

#### Características principales
- **Dimensionalidad reducida:** Cada palabra se representa mediante un vector denso de números reales (típicamente entre 100-600 dimensiones).
- **Semántica distribuida:** El significado de una palabra se distribuye en todas las componentes del vector.
- **Relaciones vectoriales:** Capturan relaciones semánticas mediante operaciones vectoriales (ej: Rey - Hombre + Mujer ≈ Reina).

### Modelo GloVe
En este ejercicio se utiliza el modelo GloVe (*Global Vectors for Word Representation*), que:
- Combina las ventajas de dos familias de modelos: matriz de co-ocurrencia global y contexto local.
- Genera vectores mediante el aprendizaje de ratios de probabilidades de co-ocurrencia.
- Considera tanto el contexto global como las relaciones locales entre palabras.

### Similitud Coseno
La similitud entre palabras se mide mediante la similitud coseno:
```math
similarity = cos(θ) = \frac{A · B}{||A|| ||B||}
```
Donde:
- A y B son vectores de palabras
- · representa el producto escalar
- ||A|| representa la norma del vector

## Contexto
Los portales de datos abiertos juegan un papel fundamental en el acceso y reutilización de la información pública. Un aspecto clave en estos sistemas es el etiquetado de los conjuntos de datos, que facilita su organización y recuperación. En sistemas distribuidos donde múltiples publicadores aportan contenidos desde diversos portales de origen, es natural encontrar variaciones en la forma de etiquetar.

### Problemática actual
- **Inconsistencia en etiquetas:** 
  - Variaciones ortográficas (mayúsculas/minúsculas).
  - Sinónimos y variantes léxicas.
  - Diferentes niveles de especificidad.

- **Desafíos de estandarización:**
  - Falta de vocabularios controlados.
  - Ausencia de jerarquías temáticas.
  - Dificultad en la normalización de términos.
  - Barreras en la interoperabilidad semántica.

## Solución propuesta
El ejercicio presenta una Prueba de Concepto (PoC) que implementa un sistema de recomendación de etiquetas basado en *embeddings*. El proceso se divide en tres fases principales:

### 1. Procesamiento de Texto
- Normalización de textos (lowercase, eliminación de caracteres especiales).
- Tokenización y limpieza de stopwords.
- Generación de *embeddings* para títulos y descripciones.

### 2. Sistema de Recomendación
- Cálculo de similitud coseno entre datasets.
- Identificación de datasets semánticamente similares.
- Extracción y ranking de etiquetas candidatas.

### 3. Estandarización con Eurovoc
- Mapeo de etiquetas recomendadas con términos Eurovoc.
- Cálculo de similitud semántica con términos del tesauro.
- Selección de términos estandarizados más apropiados.


## Estructura del proyecto
- `notebook.ipynb`: Notebook principal con la implementación.
- `README.md`: Este archivo con la documentación.
- `requirements.txt`: Dependencias necesarias.
- `eurovoc_export_es_unzip.csv`: Conjunto de datos de Eurovoc.

## Requisitos técnicos
### Software
- Python 3.x
- Jupyter Notebook

### Bibliotecas principales
```python
import numpy as np          # Operaciones numéricas
import pandas as pd         # Manipulación de datos
import matplotlib.pyplot    # Visualización
import sklearn             # Machine Learning
import gensim              # Word Embeddings
import seaborn             # Visualización estadística
import requests            # Peticiones HTTP
import graphviz            # Visualización de grafos
```

## Instalación
```bash
pip install -r requirements.txt
```

## Referencias
### Recursos técnicos
- [Tesauro Eurovoc](https://eur-lex.europa.eu/browse/eurovoc.html?locale=es)
- [API datos.gob.es](https://datos.gob.es/es/apidata)
- [Tutorial de uso de la API](https://www.youtube.com/watch?v=UzOK0TdnCM0)

### Referencias académicas
- Pennington, J., Socher, R., & Manning, C. D. (2014). GloVe: Global Vectors for Word Representation
- Mikolov, T., et al. (2013). Distributed Representations of Words and Phrases and their Compositionality
- Bojanowski, P., et al. (2017). Enriching Word Vectors with Subword Information

## Conclusiones
El ejercicio demuestra el potencial de los *embeddings* como herramienta para la asociación semántica de textos y la estandarización de etiquetas. Los resultados sugieren que esta aproximación puede mejorar significativamente la organización y recuperación de información en portales de datos abiertos.

### Ventajas del enfoque
1. **Automatización del proceso de etiquetado**
   - Reducción de trabajo manual
   - Consistencia en las recomendaciones
   - Escalabilidad del sistema

2. **Mejora en la calidad de metadatos**
   - Estandarización de vocabulario
   - Coherencia semántica
   - Interoperabilidad mejorada

3. **Facilidad de búsqueda y recuperación**
   - Mejor organización de contenidos
   - Navegación más intuitiva
   - Recuperación más precisa

### Limitaciones y trabajo futuro
- La precisión depende de la calidad de títulos y descripciones.
- La cobertura temática del tesauro Eurovoc puede no ser completa.
- Posibilidad de explorar modelos más avanzados, aunque computacionalmente más costosos:
  - BERT (Bidirectional Encoder Representations from Transformers).
  - GPT (Generative Pre-trained Transformer).
  - RoBERTa (Robustly Optimized BERT Approach).
- Oportunidades de mejora:
  - Entrenamiento con corpus específico del dominio.
  - Implementación de validación humana.
  - Desarrollo de interfaces de usuario.
  - Integración con sistemas existentes.

## Licencia
Este documento ha sido elaborado en el marco de la Iniciativa Aporta (datos.gob.es), desarrollada por el Ministerio para la Transformación Digital y de la Función Pública a través de la Entidad Pública Empresarial Red.es, y en colaboración con la Dirección General del Dato.
Aviso legal: Esta obra está sujeta a una licencia Atribución 4.0 de Creative Commons (CC BY 4.0). Está permitida su reproducción, distribución, comunicación pública y transformación para generar una obra derivada, sin ninguna restricción, siempre que se cite al titular de los derechos (Ministerio de Asuntos Económicos y Transformación Digital a través de la Entidad Pública Empresarial Red.es). La licencia completa se puede consultar en: https://creativecommons.org/licenses/by/4.0
