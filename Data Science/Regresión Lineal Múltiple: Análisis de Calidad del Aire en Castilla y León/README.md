# Regresión Lineal Múltiple: Análisis de Calidad del Aire en Castilla y León

## Descripción

Este ejercicio práctico aborda el modelado predictivo de la calidad del aire mediante regresión lineal múltiple, utilizando datos históricos reales de la comunidad autónoma de Castilla y León. A diferencia de los enfoques que analizan contaminantes de forma aislada, nuestra metodología aprovecha las interrelaciones entre múltiples variables para comprender las dinámicas de contaminación, desarrollar un modelo predictivo robusto y evaluar su fiabilidad mediante técnicas de diagnóstico avanzadas.

El objetivo es generar *insights* sobre los determinantes de la calidad del aire que puedan facilitar la toma de decisiones informadas en políticas ambientales y de salud pública.

## Contenido del Notebook

En el notebook se desarrollan los siguientes apartados:

### 0\. Configuración del entorno y planteamiento del problema

Esta sección introduce el desafío ambiental que supone la calidad del aire en el contexto urbano y prepara el entorno de desarrollo en R, instalando y cargando todas las librerías necesarias para el análisis, como `tidyverse`, `performance` y `caret`.

### 1\. Carga y exploración inicial de los datos

Este apartado se centra en todo el proceso de ingeniería de datos (*Data Engineering*), desde la obtención hasta su preparación para el modelado.

  - **1.1 Obtención del conjunto de datos**: se cargan los datos históricos de calidad del aire de Castilla y León.
  - **1.2 Limpieza y preparación de datos**: se transforman tipos de datos (como las fechas), se renombran columnas y se crean nuevas variables temporales (año, mes, día de la semana) para facilitar el análisis.
  - **1.3 Análisis de valores faltantes**: se realiza una limpieza profunda, cuantificando valores ausentes y filtrando datos anómalos, como mediciones negativas imposibles.
  - **1.4 Selección de variables y análisis de correlaciones**: se elige el **NO₂** como variable objetivo y se seleccionan los predictores más relevantes. Se realiza una primera ingeniería de características (*feature engineering*) creando variables cíclicas para los meses y se analiza la matriz de correlaciones para identificar relaciones clave y posibles problemas de multicolinealidad.

### 2\. Análisis Exploratorio Orientado al Modelado

En esta fase, se profundiza en la visualización de los datos para extraer intuiciones que guíen la construcción del modelo. Se generan gráficos clave como histogramas para analizar la distribución de los contaminantes, series temporales para identificar patrones estacionales y un mapa de calor (*corrplot*) para visualizar las correlaciones de forma más intuitiva.

### 3\. Desarrollo y Evaluación de Modelos de Regresión

Este es el núcleo del modelado predictivo.

  - **3.1 Construcción de Modelos Iterativos**: se crean tres modelos de regresión lineal con complejidad creciente: un modelo base, uno estacional y uno completo con interacciones.
  - **3.2 Análisis de resultados**: se comparan los modelos usando métricas como R², RMSE y AIC para seleccionar el más equilibrado. Se interpreta el significado de los coeficientes del modelo ganador.
  - **3.3 Diagnóstico del modelo**: se valida que el modelo seleccionado (`modelo_estacional`) cumple los supuestos de la regresión lineal (normalidad de residuos, homocedasticidad, no multicolinealidad).
  - **3.4 Validación Cruzada**: se evalúa la robustez y capacidad de generalización del modelo mediante técnicas de validación cruzada (k-fold) y validación temporal.
  - **3.5 Visualización de predicciones**: se crean gráficos de valores predichos vs. observados y de residuos por mes para diagnosticar visualmente el rendimiento y los sesgos del modelo.
  - **3.6 Guardado del Modelo para Producción**: se guardan el objeto del modelo (`.rds`) y otros artefactos (coeficientes, gráficos, información de la sesión) para su futuro despliegue. Estos objetos se encuentran en la carpeta `outputs`

### 4\. Aplicación del Modelo y Conclusiones

Finalmente, se explora el uso práctico del modelo y se sintetizan los hallazgos.

  - **4.1 Implicaciones para políticas ambientales**: se realiza un análisis de escenarios para simular el impacto de políticas como la reducción de emisiones de NO.
  - **4.2 Recomendaciones y trabajo futuro**: se analizan las limitaciones del modelo y se proponen futuras líneas de mejora, como la inclusión de datos meteorológicos.
  - **4.3 Conclusiones**: se resumen las contribuciones del análisis y su valor para la toma de decisiones.

## Conceptos Clave

  - **Regresión Lineal Múltiple**: técnica estadística para modelar la relación entre una variable dependiente y varios predictores.
  - **Análisis Exploratorio de Datos (EDA)**: proceso de visualización y resumen de datos para descubrir patrones y anomalías.
  - **Ingeniería de Características (*Feature Engineering*)**: creación de nuevas variables (predictores) a partir de los datos existentes para mejorar el rendimiento del modelo.
  - **Diagnóstico de Modelos**: verificación de los supuestos estadísticos de un modelo para asegurar su fiabilidad.
  - **Validación Cruzada (*Cross-Validation*)**: técnica para evaluar cómo un modelo generaliza a datos no vistos.
  - **Análisis de Escenarios**: simulación del impacto de cambios en las variables predictoras para evaluar políticas.

## Requisitos técnicos

  - **Software**: R 4.x o superior.
  - **Entorno**: RStudio o un notebook compatible con R (como Google Colab).
  - **Librerías principales**: `tidyverse`, `performance`, `corrplot`, `lubridate`, `caret`, `broom`.

## Usos y Aplicaciones

Este sistema puede ser aplicado en diversos contextos:

  - **Salud Pública**: estimar la exposición de la población a contaminantes.
  - **Planificación Urbana**: informar sobre el diseño de ciudades más saludables.
  - **Evaluación de Políticas**: cuantificar el impacto de medidas como las zonas de bajas emisiones.
  - **Sistemas de Alerta Temprana**: predecir picos de contaminación para activar protocolos de aviso.

## Aspectos destacados

  - **Análisis de datos reales y complejos** del portal de datos abiertos de Castilla y León.
  - **Enfoque iterativo** en la construcción de modelos para una evaluación comparativa.
  - **Diagnóstico estadístico completo** para asegurar la validez del modelo.
  - **Aplicación práctica** mediante simulación de escenarios de políticas públicas.

## Licencia

Este proyecto ha sido elaborado en el marco de la Iniciativa Aporta (datos.gob.es), desarrollada por el Ministerio para la Transformación Digital y de la Función Pública a través de la Entidad Pública Empresarial Red.es, y en colaboración con la Dirección General del Dato.

**Aviso legal**: Esta obra está sujeta a una licencia Atribución 4.0 de Creative Commons (CC BY 4.0). Está permitida su reproducción, distribución, comunicación pública y transformación para generar una obra derivada, sin ninguna restricción, siempre que se cite al titular de los derechos (Ministerio para la Transformación Digital y de la Función Pública a través de la Entidad Pública Empresarial Red.es). La licencia completa se puede consultar en: https://creativecommons.org/licenses/by/4.0
