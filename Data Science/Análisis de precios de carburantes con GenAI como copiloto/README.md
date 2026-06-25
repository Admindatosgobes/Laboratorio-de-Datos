# Análisis de Precios de Carburantes con GenAI como Copiloto

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alijaalejandro/ejercicio-datos-ia-copiloto/blob/master/notebook/Analisis_Carburantes_v0_1.ipynb)

Un **ejercicio educativo reproducible en Google Colab** que demuestra cómo usar IA generativa como copiloto en un análisis de datos completo, desde ingesta hasta análisis de impacto de features.

## Descripción

Analizamos +11,000 gasolineras españolas usando datos públicos del Ministerio de Turismo para responder preguntas de negocio:
- ¿Qué provincia tiene carburantes más caros?
- ¿La ubicación geográfica afecta el precio?
- ¿Hay diferencias significativas entre marcas?
- ¿Podemos predecir precios futuros?

**Enfoque pedagógico**: Cada paso explica cómo GenAI aceleró el análisis, documentando problemas reales encontrados y soluciones reutilizables.

## Ejecución Rápida

### Google Colab (Recomendado)

Haz clic en el badge **"Open In Colab"** de arriba. El notebook se ejecuta directamente en el navegador sin necesidad de instalar nada.

**Tiempo total**: ~4 minutos

### Local (Python 3.9+)

```bash
git clone <repo-url>
cd ejercicio-datos-ia-copiloto
pip install -r requirements.txt
jupyter notebook notebook/Analisis_Carburantes_v0_1.ipynb
```

## Estructura

```
ejercicio-datos-ia-copiloto/
├── notebook/
│ └── Analisis_Carburantes_v0_1.ipynb # 19 celdas, 100% ejecutable
│
├── prompts/ # Problemas reales + soluciones
│ ├── ingesta/
│ │ ├── descargar_dataset.md # APIs robustas con fallbacks
│ │ └── explorar_estructura.md
│ ├── limpieza/
│ │ ├── validar_precios.md
│ │ └── normalizar_marcas.md
│ ├── visualizacion/
│ │ ├── precio_por_provincia.md # Scatter mapbox interactivo
│ │ ├── distribucion_por_marca.md # Box plot top 10 marcas
│ │ ├── ubicacion_vs_precio.md # Scatter mapbox 11k estaciones
│ │ ├── analisis_impacto_features.md # Correlación + tendencias
│ │ └── mejoras_visualizaciones_interactivas.md
│ └── features/
│ ├── crear_fin_semana.md
│ ├── distancia_punto_referencia.md
│ └── region_geografica.md
│
├── posts/
│ └── Reflexion_GenAI_Analisis_Carburantes.md # Reflexión sobre el proceso
│
├── specs/ # Documentación técnica
│ └── 001-carburantes-ia/
│ ├── spec.md # Especificación funcional
│ ├── plan.md # Plan técnico + lecciones aprendidas
│ └── checklists/
│
├── tests/ # Scripts de validación
│ ├── test_descarga_local.py
│ └── test_notebook_completo.py
│
├── requirements.txt # pandas, matplotlib, scikit-learn
├── LICENSE # MIT
└── README.md # Este archivo
```

## Fases del Análisis

### FASE 0: Preparación
- Setup de entorno, imports, metadatos
- Versión del notebook + contador de iteraciones

### FASE 1: Ingesta Robusta (T009-T010)
- Descarga desde API del Ministerio de Turismo
- **Triple fallback**: requests → curl → datos demo
- Maneja SSL, timeouts, bloqueos de IP

### FASE 2: Limpieza y Validación (T014-T017)
- Validación de precios (rango realista)
- Normalización de marcas (variantes sin normalizar)
- Filtrado de coordenadas (bounding box de España)
- Detección de valores nulos

### FASE 3: Análisis Exploratorio (T020-T023)
**4 visualizaciones con respuestas a preguntas de negocio:**
1. **Bar chart**: Precio promedio por provincia (top 12)
2. **Scatter map**: Ubicación vs precio (península ● / islas ▲)
3. **Histograma**: Distribución de precios (media + mediana)
4. **Bar chart**: Top 8 marcas (normalizado, con conteos)

### FASE 4: Ingeniería de Variables (T028-T030)
- `es_fin_semana`: Binario (0=semana, 1=fin de semana)
- `distancia_a_madrid`: Aproximación a hub económico
- `region`: Norte/Centro/Sur (basado en latitud)

### FASE 5: Análisis de Impacto de Features (T034-T037)
**3 visualizaciones adicionales que muestran el impacto de cada feature:**
1. **Scatter plot**: Precio vs Distancia a Madrid (correlación geográfica)
2. **Bar chart comparativo**: Precio fin de semana vs entre semana (impacto temporal)
3. **Box plot regional**: Distribución de precios por región norte/centro/sur

## Lecciones Técnicas Documentadas

Cada problema real encuentra solución documentada:

| # | Problema | Solución | Reutilizable |
|---|----------|----------|-------------|
| 1 | SSL/IP bloqueo en APIs | Triple fallback (requests→curl→demo) | APIs españolas públicas |
| 2 | Coordenadas fuera de España | Bounding box [lat:27.5-43.8, lon:-18.2-4.4] | Análisis geográfico |
| 3 | Variantes marca sin normalizar | `.str.upper().str.strip()` antes de agrupar | Cualquier agregación |
| 4 | Cifras similares no visuales | `ax.set_xlim(min*0.95, max*1.05)` | Rangos estrechos |
| 5 | ValueError: y contains NaN | Validar antes de train_test_split | ML pipelines |

Cada solución está documentada en `prompts/` con:
- **Prompt Original**: Qué pedimos a GenAI
- **Resultado Obtenido**: Código que funcionó
- **Reflexión**: Qué aprendimos + patrón reutilizable

## Cómo Usar Este Repo

### Para Aprender Análisis de Datos
1. Lee el notebook secuencialmente (cada celda tiene comentarios)
2. Para cada gráfico, consulta `prompts/visualizacion/`
3. Entiende por qué cada técnica resuelve una pregunta específica

### Para Reutilizar Código
1. Copia snippets de `prompts/` a tus análisis
2. Adapta features, visualizaciones, validaciones a tus datos
3. La estructura es modular: ingesta, limpieza, EDA, features, análisis de impacto

### Para Entender Prompt Engineering
1. Lee `posts/Reflexion_GenAI_Analisis_Carburantes.md`
2. Observa el patrón: Describe → Cuestiona → Refina → Valida
3. Cada prompt en `prompts/` es un ejemplo de iteración con IA generativa

## Requisitos

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
scikit-learn>=0.24.0
```

## Ejecución Rápida (Tiempo: ~3 minutos)

1. Abre el notebook en Colab
2. Ejecuta FASE 0 (imports) - 30 segundos
3. Ejecuta FASE 1 (descarga datos) - 1 minuto (con fallback a demo si API no responde)
4. Ejecuta FASE 2-5 (limpieza, EDA, features, análisis de impacto) - 90 segundos

## Datos

- **Fuente**: https://datos.gob.es/es/catalogo/e05068001-precio-de-carburantes-en-las-gasolineras-espanolas
- **Registro**: API del Ministerio de Turismo
- **Volumen**: 11,000-11,500 estaciones actualmente operativas en España
- **Actualización**: Tiempo real (datos.gob.es)
- **Fallback**: Si API no disponible, genera 11,000 gasolineras demo realistas

## Caso de Uso Educativo

Este proyecto demuestra:
1. **Cómo trabajar con APIs públicas reales** (no datos sintéticos)
2. **Debugging práctico** de problemas que surgen con datos reales
3. **Comunicación de resultados** a audiencias no-técnicas
4. **Iteración con GenAI** como pareja de programación

## Licencia

MIT - Abierto para usos educativos, comerciales, y personales.

---

**Nota Técnica**: Este proyecto fue desarrollado usando **Claude Code** (CLI) con el modelo **Claude Haiku** como IA copiloto, y **Speckit** como framework de Spec Driven Development (SDD). El enfoque SDD permitió documentar especificaciones, planes técnicos y lecciones aprendidas de forma estructurada antes de cada iteración de código.

**Herramientas utilizadas**:
- **Claude Code**: CLI para integración de IA en flujos de desarrollo
- **Claude Haiku**: Modelo de IA generativa para iteración rápida
- **Speckit**: Framework SDD para especificaciones y planning

**Tiempo de desarrollo**: ~40 horas iterando con IA (vs ~120 sin asistencia) 
**Última actualización**: Abril 2026 
**Estado**: 100% ejecutable, 5 lecciones técnicas documentadas, 14 prompts reutilizables
