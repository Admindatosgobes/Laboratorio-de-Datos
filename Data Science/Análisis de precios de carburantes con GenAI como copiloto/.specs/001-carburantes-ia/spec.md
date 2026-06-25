# Feature Specification: Análisis de Precios de Carburantes con GenAI

**Feature Branch**: `001-carburantes-ia`  
**Created**: 2026-04-12  
**Status**: Draft  
**Input**: "Usa el documento Inception.md como base para crear una primera especificación que luego refinemos"

## Descripción General

Crear un notebook de Jupyter reproducible en Google Colab que demuestre cómo utilizar herramientas de GenAI (ChatGPT, Claude, etc.) como copiloto en un análisis completo de ciencia de datos. El análisis toma el dataset público de "Precios de Carburantes en las Gasolineras Españolas" de datos.gob.es y lo procesa a través de 7 fases: ingesta, limpieza, análisis exploratorio, ingeniería de variables, modelado y conclusiones.

El resultado entregable es:
- **Notebook funcional en Colab** con el flujo completo comentado en español
- **Post Markdown reflexivo** que contextualiza cómo GenAI aceleró cada fase y qué aprendió el usuario

---

## Clarifications

### Session 2026-04-12

- Q: Estructura exacta del dataset (columnas, tipos) → A: No se especifica. El descubrimiento de estructura IS parte del análisis (User Story 1 incluye EDA inicial de esquema).
- Q: Versionado e iteraciones → A: Notebook DEBE mostrar explícitamente versión e iteración en primera celda como metadatos educativos.
- Q: Manejo de fallos en descargas → A: Try-once simple con mensaje de error claro en español. Sin retry automático (mantiene simplicidad, enseña error handling básico).
- Q: Alcance del Post Markdown → A: Reflexión educativa (~500-1000 palabras) con secciones: Problema, Proceso con GenAI, Aprendizajes, Limitaciones, Guía de Uso del Repo (dónde notebook, dónde prompts), Extensiones sugeridas.
- Q: Los 4 gráficos específicos → A: (1) Precio medio por provincia (barras), (2) Evolución temporal de precios (línea), (3) Relación ubicación-precio (scatter con coordenadas), (4) Distribución de precios por marca (box-plot).
- Q: Interactividad en visualizaciones → A: Usar plotly para gráficos interactivos (zoom, pan, hover, filtros). Plotly preinstalado en Colab. Preservar pedagógica.
- Q: Las 3 librerías exactas → A: pandas, matplotlib, scikit-learn. Requisito crítico: código SIMPLE y COMPACTO. El notebook ilustra cómo componer análisis con interés de negocio mediante prompts, NO es un notebook exhaustivo.

---

## User Scenarios & Testing

### User Story 0 - Documentación de Versión e Iteraciones (Priority: P0)

**Descripción**: Como usuario educativo, quiero ver claramente qué versión del notebook estoy usando y cuántas iteraciones/mejoras ha tenido. Esto ayuda a rastrear evolución del análisis y fomenta iteración incremental.

**Por qué esta prioridad**: Meta-requisito de documentación que debe aparecer desde el inicio. Base para todas las demás historias.

**Test independiente**: Ejecutar primera celda. Verificar que se muestra versión (ej: v0.1.0) y contador de iteración (ej: Iteración 1).

**Acceptance Scenarios**:

1. **Given** un notebook nuevo, **When** ejecuto la primera celda, **Then** veo mensaje tipo "Versión: v0.1.0 | Iteración: 1"
2. **Given** un notebook con mejoras, **When** se incrementa la versión, **Then** el contador de iteración también se actualiza
3. **Given** el notebook documentado, **When** lo comparto, **Then** otros usuarios saben exactamente qué versión están usando

---

### User Story 1 - Cargar y Formatear Datos Públicos (Priority: P1)

**Descripción**: Como usuario, quiero poder cargar el dataset de carburantes desde datos.gob.es directamente en Colab sin configuración previa. El dataset tiene particularidades españolas (codificación ISO-8859-1, separadores europeos de decimales) que GenAI puede ayudarme a resolver.

**Por qué esta prioridad**: Sin datos cargados correctamente, no hay análisis. Es el paso bloqueante inicial. Demuestra cómo GenAI resuelve problemas técnicos específicos del dataset.

**Test independiente**: Ejecutar la celda de carga de datos en Colab con usuario nuevo. Verificar que el dataframe está disponible con las 11k filas y todas las columnas intactas.

**Acceptance Scenarios**:

1. **Given** un usuario nuevo en Colab sin dependencias previas, **When** ejecuta la celda de descarga y carga, **Then** obtiene un dataframe con 11000+ filas y las 20+ columnas originales del dataset
2. **Given** caracteres acentuados en nombres de gasolineras, **When** se carga el dataset, **Then** aparecen correctamente sin corrupción de caracteres
3. **Given** precios con decimales europeos (ej: "1,234€"), **When** se carga el dataset, **Then** se convierten a valores numéricos flotantes (1.234)

---

### User Story 2 - Limpiar y Normalizar Datos (Priority: P2)

**Descripción**: Como usuario, quiero identificar y corregir problemas en los datos (valores nulos, inconsistencias en nombres de marcas, outliers en precios) usando funciones generadas con GenAI que verifiquen integridad ("sanity checks").

**Por qué esta prioridad**: La calidad del análisis depende de datos limpios. Muestra cómo GenAI detecta problemas de forma inteligente sin scripting manual.

**Test independiente**: Ejecutar funciones de validación que reporten anomalías encontradas (cantidad de nulos, marcas inconsistentes, precios anómalos). Verificar que el dataset limpio es coherente.

**Acceptance Scenarios**:

1. **Given** el dataset cargado, **When** ejecuto la función de validación de precios, **Then** recibo un reporte de precios fuera de rango (ej: ≤0€ o >3€)
2. **Given** marcas de gasolineras con variaciones ortográficas (ej: "REPSOL", "Repsol", "repsol"), **When** ejecuto normalización, **Then** se unifican bajo un estándar único
3. **Given** datos con valores nulos, **When** ejecuto análisis de cobertura, **Then** obtengo porcentaje de faltantes por columna

---

### User Story 3 - Análisis Exploratorio con Visualizaciones (Priority: P2)

**Descripción**: Como usuario, quiero generar visualizaciones que revelen patrones de precios por provincia, marca, tipo de carburante y evolución temporal, usando prompts a GenAI para "traducir" preguntas en código de gráficos.

**Por qué esta prioridad**: El EDA es fundamental para entender datos. Demuestra flujo iterativo: pregunta → código generado → interpretación → siguiente pregunta.

**Test independiente**: Generar al menos 4 gráficos (barras, línea temporal, mapa/scatter de coordenadas, box-plot). Verificar que son legibles y responden preguntas del negocio.

**Acceptance Scenarios**:

1. **Given** datos limpios, **When** genero gráfico de precio medio por provincia, **Then** aparecen todas las provincias sin provincias duplicadas o faltantes
2. **Given** histórico de precios, **When** creo gráfico de series temporales, **Then** se ve tendencia clara de evolución de precios en los últimos 30 días
3. **Given** coordenadas geográficas, **When** creo scatter plot de ubicación vs precio, **Then** se identifica si hay correlación visual norte/sur

---

### User Story 4 - Ingeniería de Variables Asistida (Priority: P3)

**Descripción**: Como usuario, quiero crear features nuevas (ej: si es fin de semana, región geográfica superior) usando sugerencias de GenAI sobre qué variables podrían mejorar un análisis posterior.

**Por qué esta prioridad**: Feature engineering es una habilidad avanzada. Demuestra cómo GenAI sugiere ideas más allá del código mecánico.

**Test independiente**: Crear al menos 3 variables nuevas a partir de las existentes. Verificar que se calculan correctamente.

**Acceptance Scenarios**:

1. **Given** columna de fecha, **When** genero variable de "es_fin_de_semana", **Then** valores son True/False correctamente según día de la semana
2. **Given** coordenadas (latitud/longitud), **When** calculo distancia a punto de referencia, **Then** la distancia es razonable (mayor a 0)
3. **Given** código postal, **When** agrupo en región geográfica (norte/centro/sur), **Then** todas las provincias están mapeadas sin nulos

---

### User Story 5 - Análisis de Impacto de Features (Priority: P3)

**Descripción**: Como usuario, quiero visualizar cómo cada feature engineered (fin de semana, distancia a Madrid, región) impacta el precio del carburante, usando gráficos interactivos que muestren correlaciones y patrones.

**Por qué esta prioridad**: Cierra el ciclo del análisis. Demuestra cómo las features cuentan historias sobre precios sin necesidad de predicción. Más educativo que modelado sin datos históricos.

**Test independiente**: Generar 3-4 visualizaciones que relacionen features con precios. Verificar que cada gráfico responde una pregunta de negocio clara.

**Acceptance Scenarios**:

1. **Given** la feature es_fin_semana, **When** visualizo precio fin de semana vs entre semana, **Then** veo si hay diferencia significativa en el precio medio
2. **Given** la feature distancia_a_madrid, **When** creo scatter plot precio vs distancia, **Then** observo si hay correlación geográfica
3. **Given** la feature región (norte/centro/sur), **When** visualizo box plot por región, **Then** veo diferencias de precio por zona

---

## Edge Cases

- ¿Qué ocurre si el dataset tiene gasolineras cerradas (sin datos recientes)? → Se excluyen del análisis
- ¿Cómo maneja el modelo cambios bruscos de precio? → Se documenta limitación en conclusiones
- ¿Qué si hay provincias con muy pocas muestras? → Se visualiza cobertura de datos por región

---

## Requirements

### Functional Requirements

- **FR-001**: Notebook DEBE descargar dataset público de datos.gob.es sin requerer autenticación y DEBE explorar su estructura (columnas, tipos, nulos) como parte inicial del análisis
- **FR-001a**: Si falla la descarga del dataset, DEBE mostrar mensaje de error claro en español explicando el problema (sin retry automático)
- **FR-002**: Notebook DEBE ejecutarse completamente en Google Colab sin instalaciones previas
- **FR-003**: Todas las celdas DEBEN contener comentarios en español explicando su propósito
- **FR-004**: DEBE incluir funciones de validación de integridad de datos (sanity checks) con reporte de anomalías
- **FR-005**: DEBE generar exactamente 4 visualizaciones específicas interactivas: (1) Gráfico de barras: precio medio por provincia, (2) Gráfico de línea: evolución temporal de precios, (3) Scatter plot: relación ubicación geográfica vs precio, (4) Box-plot: distribución de precios por marca. Usar plotly para interactividad (zoom, pan, hover, filtros)
- **FR-006**: DEBE crear al menos 3 variables de ingeniería (features nuevas derivadas)
- **FR-007**: DEBE entrenar un modelo de predicción con métricas de desempeño (R², RMSE, MAE)
- **FR-008**: DEBE incluir conclusiones numéricamente fundamentadas con insights principales
- **FR-009**: Post Markdown (~500-1000 palabras) DEBE incluir secciones: Problema, Proceso con GenAI, Aprendizajes, Limitaciones, Guía de Uso del Repo, Extensiones
- **FR-010**: Post DEBE describir explícitamente dónde encontrar el notebook y dónde los prompts organizados en el repositorio (estructura de directorios)
- **FR-011**: Código DEBE ser simple y compacto (máximo 3 librerías: pandas, matplotlib, scikit-learn). NO es un notebook exhaustivo; ilustra cómo usar prompts para componer análisis con interés de negocio
- **FR-012**: Tiempo total de ejecución DEBE ser menor a 5 minutos en Colab
- **FR-013**: Notebook DEBE mostrar explícitamente en la primera celda el número de versión y un contador de iteraciones por las que ha pasado
- **FR-014**: Notebook DEBE ser manejable (no exhaustivo): máximo ~100-150 líneas de código activo, enfoque en ilustrar patrones de composición con prompts, no en cobertura completa del dominio

### Key Entities

- **Gasolinera**: Identificada por código, nombre, marca, ubicación (provincia, código postal, coordenadas)
- **Precio**: Valor en euros de un tipo de carburante en una gasolinera en una fecha
- **Carburante**: Tipo (Gasolina 95, Gasolina 98, Diésel, etc.)
- **Fecha**: Timestamp de cuando se capturó el precio
- **Región Geográfica**: Agrupación de provincias (norte/centro/sur derivada de coordenadas)

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: Notebook ejecutable sin errores de principio a fin en Colab nuevo (0 modificaciones necesarias)
- **SC-002**: Al menos 90% de filas del dataset cargadas correctamente (>10k de 11k esperadas)
- **SC-003**: Código ejecuta en menos de 5 minutos en Colab estándar
- **SC-004**: Los 4 gráficos responden preguntas de negocio: ¿provincia más cara?, ¿tendencia de precios?, ¿ubicación afecta precio?, ¿marca afecta precio?
- **SC-005**: Post Markdown contiene todas 6 secciones (Problema, Proceso, Aprendizajes, Limitaciones, Guía de Uso, Extensiones) y claramente explica rol de GenAI en el análisis
- **SC-006**: Modelo de predicción tiene R² ≥ 0.5 en conjunto de prueba (explica mínimo 50% de varianza)
- **SC-007**: Métricas de desempeño (RMSE, MAE) se interpretan en contexto de negocio (ej: "error promedio de ±X€")
- **SC-008**: Usuario aprendiz puede reproducir notebook copiando + pegando en Colab sin pasos manuales
- **SC-009**: Documentación en español sin términos técnicos no explicados es comprensible para Data Scientist junior
- **SC-010**: Primera celda del notebook muestra versión (ej: "v0.1.0") e iteración actual (ej: "Iteración 3") de forma clara y visible
- **SC-011**: Notebook es manejable (~100-150 líneas código activo). Cada celda enseña un patrón de uso de prompts, no es un tutorial exhaustivo

---

## Assumptions

- El dataset permanecerá disponible en datos.gob.es sin cambios en formato durante el análisis
- Los usuarios tienen acceso a Google Colab gratuito (sin GPU necesaria, CPU es suficiente)
- Familiarity con conceptos básicos de DataFrames (pandas) se asume; no requiere experiencia previa en ML
- Carburantes de interés principal: Gasolina 95 y Diésel (tipos más comunes)
- Período de análisis: últimos 30-90 días de datos disponibles (no requiere histórico completo)
- "GenAI como copiloto" significa: usuario formula preguntas, GenAI genera código, usuario ejecuta y evalúa
- No se requiere predicción en tiempo real; ejercicio es educativo, no productivo
- Lenguaje del código y comentarios: 100% español (por constitución del proyecto)
