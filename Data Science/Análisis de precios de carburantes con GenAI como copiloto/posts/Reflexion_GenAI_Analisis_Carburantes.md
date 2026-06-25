# Reflexión: GenAI como Copiloto en Análisis de Datos

**Fecha**: Abril 2026 
**Proyecto**: Análisis de Precios de Carburantes en España 
**Herramienta**: Claude como IA Copiloto 
**Código**: Completamente reproducible en Google Colab

---

## Introducción


Este documento refleja cómo usar **GenAI como un copiloto**, no solo para escribir código, sino para pensar junto con nosotros sobre el problema de datos. Analizamos +11,000 gasolineras españolas en 5 fases: ingesta, limpieza, EDA, features, y análisis de impacto de features.

El **resultado** es un notebook educativo en Colab que documenta cada paso con prompts originales, problemas reales encontrados, y soluciones reutilizables. Todo el proyecto está disponible de forma abierta en un repositorio de Github.

En este post explicamos el análisis que hemos realizado de un conjunto de datos abiertos publicados en el portal datos.gob.es. A diferencia de otros ejercicios de datos, para realizar este análisis hemos utilizado un entorno agéntico que consiste en una interfaz conversacional que se apoya en un modelo grande del lenguaje (LLM) y un sistema de codificación asistido por inteligencia artifical. De forma práctica, esto se traduce en que, en vez de realizar las tareas de codificación para el análisis de datos por nosotros mismos, le "decimos" a un sistema en lenguaje natural qué queremos conseguir y el lo implementa.

_Nota: para la realización de este ejercicio hemos empleado una metodología Spec Driven Development pero su explicación queda fuera del alcance de este post. Esta metodología ayuda a "guiar a la IA" a través de un proceso estructurado con el objetivo de evitar que la conversación pierda el objetivo del ejercicio._

El proceso, aunque asistido por IA, sigue un flujo estándar en ciencia de datos que ya hemos comentado en varias ocasiones en este espacio (XXX link). En el proceso, hemos diseñado prompts para cada una de las fases del análisis: ingesta, limpieza, visualización (EDA), enriquecimiento y finalmente, análisis enriquecidos.

Por ejemplo:
```
Una vez descargado el dataset de carburantes, necesito explorar su estructura.
Escribe código Python que:

1. Muestre el nombre y tipo de datos de cada columna (.info())
2. Muestre los primeros 5 registros (.head())
3. Muestre estadísticas básicas (.describe())
4. Reporte el número total de filas y columnas
5. Identifique columnas con valores nulos
6. Todo con comentarios en español

El código debe ser educativo, mostrando qué información aporta cada exploración.
```

Vamos paso a paso!
---

## 1. Fase 1: Ingesta Robusta de APIs Públicas

### El Reto

Descargar datos del Ministerio de Turismo español es conceptualmente simple: un GET HTTP a `https://sedeaplicaciones.minetur.gob.es/...` retorna JSON con ~11,000 gasolineras. Pero en la vida real, las APIs públicas fallan o están mal documentadas. Algunos errores con los que nos hemos encontrado son:

- **Certificados SSL expirados** → `SSLError`
- **Bloqueo de IPs cloud** → `ConnectionResetError`
- **Servidores inestables** → timeouts
- **Mala documentación** → La documentación de la API describe un `JSON` cuando es un `XML`

### Cómo GenAI Aceleró la Solución
Gracias a la IA, podemos probar múltiples enfoques hasta dar con la solución. En vez de escribir múltiples intentos de `try-except` a ciegas, **codeé el problema con GenAI**:

1. Describí: *"Necesito descargar datos. El servidor a veces rechaza requests. Necesito fallbacks."*
2. GenAI propuso: *"Intenta requests → curl → estructura vacía"*
3. Yo refuté: *"¿Por qué curl ayuda si requests ya falló?"*
4. GenAI explicó: *"Curl usa TLS diferente + no envía certificados de Python. Sortea algunos bloqueos."*
5. Implementamos: **Triple fallback strategy** (requests con verify=False → curl -k → demo data)

**Tiempo ahorrado**: 2-3 horas de debugging hubiera tomado el trial-and-error puro. Con GenAI: 30 minutos iterando.

**Lección aprendida**: `requests.Session()` + `User-Agent` navegador + `verify=False` resuelve 80% de problemas de SSL en este endpoint de gasolinearas españolas.

### Código Resultante
```python
def descargar_datos_api(url):
 try:
 sesion = requests.Session()
 sesion.headers.update({"User-Agent": "Mozilla/5.0..."})
 response = sesion.get(url, timeout=45, verify=False)
 return response.json()
 except:
 # Fallback curl con -k
 resultado = subprocess.run(["curl", "-s", "-k", url], ...)
 return json.loads(resultado.stdout)
```

---

Descargar los datos ha sido uno de las mayores dificultades pero no la única.

## 2. Fase 2: Limpieza con Aprendizajes Reales

### El Reto
Los datos reales nunca son perfectos. Dar sentido de negocio a los datos es una de las actividades más costosas porque la intuición y el razonamiento humano son difíciles de emular. Algunos ejemplos:

- **Variantes sin normalizar**: "MOEVE", "Moeve", "moeve" → 3 marcas diferentes en agregaciones. Las personas sabemos que es la misma marca, pero estrictamente hablando son textos diferentes.
- **Coordenadas erroneas**: Puntos fuera de España (islas remotas, Marruecos)
- **Precios con separador coma**: `"1,349"` en lugar de `1.349`
- **Conversión genera NaN**: `pd.to_numeric(..., errors='coerce')` introduce NaN en variables clave

### Cómo GenAI Aceleró el Debug
Cuando ejecuté el notebook por primera vez, obtenía errores o gráficos poco coherentes.

En lugar de corregir el código a mano, le dictamos a la IA las reglas de negocio que conocemos como humanos y ella implementa los mecanismos de corrección y normalización.

**Tiempo ahorrado**: 1 hora debugging hubiera sido necesaria. Con GenAI: 15 minutos.

**Lección aprendida**: Las reglas de calidad más técnicas son fácilmente identificadas por la IA casi automáticamente (el tipado de datos, nulos, números como texto y viceversa) sin emabargo, las reglas más humanas, como coordenadas sin sentido para España o las agregaciones de marcas (CEPSA es MOEVE desde hace poco) son reglas que hay que especificar en el prompt.

### Patrones Documentados
Cada problema real documentado en `prompts/`:

| Problema | Solución | Reutilizable |
|----------|----------|-------------|
| Variantes marca fusionadas | `.str.upper().str.strip()` | Sí - cualquier columna categórica |
| Precios no visuales en barplot | `ax.set_xlim(min*0.95, max*1.05)` | Sí - cualquier serie con rango estrecho |
| Península e islas mezcladas | Separar por marcador: ● vs ▲ | Sí - análisis geográfico multirregión |
---

## 3. Fase 3: Análisis Exploratorio Visual

### El Reto
Responder 4 preguntas de negocio con visualizaciones:
1. ¿Qué provincia tiene precios más caros?
2. ¿Hay correlación ubicación (lat/lon) → precio?
3. ¿Marcas con precios significativamente diferentes?
4. ¿Distribución de precios (media, mediana, outliers)?

### Cómo GenAI Ayudó a Elegir Visualizaciones
No escribí gráficos al azar. **Codifiqué la pregunta junto con GenAI**:

- **Pregunta**: "¿Qué provincia es más cara?" → **Respuesta visual**: Bar chart ordenado descendente
- **Pregunta**: "¿Ubicación vs precio?" → **Respuesta visual**: Scatter con colormap (lon, lat, color=precio)
- **Pregunta**: "¿Marcas diferentes?" → **Respuesta visual**: Box plot por marca (mediana, cuartiles, outliers)

**Beneficio**: No gasté tiempo buscando "¿box plot o violin plot?". GenAI sugirió la visualización correcta basada en la pregunta.

### Insight Inesperado
La visualización de península vs islas reveló un patrón que un groupby nunca hubiera mostrado: **Los precios en islas son más caros**, probablemente por logística. Este insight emergió de la **visualización, no de las métricas**.

**Lección aprendida**: La interacción con las visuzlizaciones es una de las tarea más intensivas en depuración. La IA "no ve" el resultado gráfico y por lo tanto no es capaz de detectar sola, cuando un rango o escala en un eje es adecuada o no. Tampoco es sensible a la densidad de información. Gráficas con exceso de información son inútiles por eso son importantes los filtros Top 5, Top 10, etc.

---

## 4. Fase 4: Ingeniería de Variables (Features)

### El Reto
Crear 3 features numéricos/categóricos que capturen:
- **Temporal**: ¿Fin de semana afecta precio? → `es_fin_semana` (0/1)
- **Geográfico**: ¿Distancia a hub afecta? → `distancia_a_madrid` (km)
- **Regional**: ¿Regiones con patrones diferentes? → `region` (norte/centro/sur)

### Cómo GenAI Aceleró Feature Engineering
Típicamente, feature engineering es iterativo: crear, validar, descartar. Con GenAI:

1. Propuse: *"¿Qué features capturan la variación de precios?"*
2. GenAI sugirió: Fin de semana (temporal), distancia a hub (geográfico), región (regional)
3. Yo pregunté: *"¿Por qué Madrid como hub?"*
4. GenAI: *"Es mercado más eficiente/estable. Precios desviación de Madrid son proxy de fricción."*
5. Validé: Efectivamente, distancia_a_madrid muestra correlación visible

**Tiempo ahorrado**: Trial-and-error feature creation hubiera sido 3-4 horas. Con GenAI: 45 minutos.

**Lección aprendida**: Proponer features **junto** con reasoning. No solo código, sino narrativa.

---

## 6. Lecciones Organizadas por Funcionalidad

Todo problema real documentado en `prompts/`. Estructura:

```
prompts/
├── ingesta/
│ ├── descargar_dataset.md (Leccion #1, #4: APIs robustas)
│ └── explorar_estructura.md
├── limpieza/
│ ├── validar_precios.md (Leccion #2: validar ranges)
│ ├── normalizar_marcas.md (Leccion #3: normalizar antes de agrupar)
├── visualizacion/
│ ├── precio_por_provincia.md (Scatter mapbox interactivo)
│ ├── distribucion_por_marca.md (Box plot top 10 marcas)
│ ├── ubicacion_vs_precio.md (Scatter mapbox 11k estaciones)
│ ├── analisis_impacto_features.md (Correlación + tendencias)
│ └── mejoras_visualizaciones_interactivas.md
└── features/
 ├── crear_fin_semana.md
 ├── distancia_punto_referencia.md
 └── region_geografica.md
```

**Clave**: Cada prompt es reusable en proyectos futuros (predecir ventas, demanda, stocks).

---

## 7. Reflexión: Qué Hace GenAI un Buen Copiloto

### Dónde GenAI Agrega Valor
1. **Iteración rápida**: Pasar de problema → solución en minutos
2. **Pattern matching**: "Ah, esto es como cuando..."
3. **Pensamiento lateral**: Alternativas que hubiera descartado (ej: curl vs requests)
4. **Comunicación**: Ayuda a explicar técnica a audiencias no-técnicas
5. **Documentación**: Articula WHY, no solo WHAT

### ⚠ Dónde GenAI Falla
1. **Domain expertise**: No reemplaza conocimiento de datos/negocio
2. **Validación estadística**: Sugiere modelos, pero TÚ validas si son válidos
3. **Creativity profunda**: Ideación genuina sigue siendo humana
4. **Responsabilidad**: Yo valido cada línea. GenAI no.

---

## 8. Guía de Uso del Repositorio

### Para Estudiantes de Análisis de Datos
1. Abre `notebook/Analisis_Carburantes_v0_1.ipynb` en [Google Colab](https://colab.research.google.com)
2. Lee cada celda lentamente - cada fase tiene comentarios pedagógicos
3. Para cada problema visual (gráfico), mira `prompts/visualizacion/`
4. Replica patrón en tus datos

### Para Ciencientes de Datos
1. Revisa `specs/001-carburantes-ia/plan.md` para ver decisiones arquitectónicas
2. Usa prompts como **snippets reutilizables** en tus proyectos
3. La tabla "Lecciones Técnicas" documenta bugs reales encontrados + soluciones

### Para Ingenieros de IA/Prompt Engineering
1. Observa cómo iteré con GenAI en cada sección anterior
2. Modelo: Describe problema → cuestiona solución → refina → valida
3. Cada `prompts/*.md` es un ejemplo de prompt + reflexión iterativa

---

## 9. Métricas de Éxito del Proyecto

| Métrica | Target | Logrado | Estado |
|---------|--------|---------|--------|
| Notebook 100% ejecutable en Colab | Sí | Sí | |
| Fallback robusto para API | Sí | Triple fallback | |
| Prompts documentados | 10+ | 13 | |
| Lecciones técnicas documentadas | 3+ | 5 | |
| Datos demo realistas si API falla | Sí | 11,000 gasolineras | |
| Todo en español | Sí | Sí | |
| < 150 líneas código activo | Sí | ~120 líneas | |
| Ejecución < 5 min Colab | Sí | ~3 min | |

---

## 10. Conclusiones

### GenAI Acelera Análisis de Datos Cuando
- Trabajas en **iteraciones rápidas** (código → validar → refinar)
- Necesitas **múltiples enfoques** (box plot vs histogram? Ambos en 10 min)
- Debuggeas problemas **con contexto** (traceback + dominio = solución rápida)
- Comunicas resultados **a audiencias diversas** (técnico + negocio)

### Pero GenAI NO Reemplaza
- Pensamiento crítico sobre validez de datos
- Domain expertise (¿es normal que Canarias sea 5% más caro?)
- Decisiones sobre qué **preguntar** a los datos
- Responsabilidad sobre conclusiones

### Lección Final
**GenAI es mejor pensando CON nosotros que pensando POR nosotros.**

Este proyecto lo demostró: no fue "pedir a Claude que lo hiciera". Fue:
1. Yo describo problema
2. Claude sugiere enfoque
3. Yo cuestiono supuestos
4. Claude elabora reasoning
5. Yo implemento + valido
6. Claude documenta patrones

Resultado: Un análisis robusto, documentado, y **reusable** en 40 horas de trabajo (vs 120 sin GenAI).

---

**Autor**: Análisis realizado como ejercicio educativo con GenAI como copiloto 
**Licencia**: MIT - Abierto para usos educativos 
**Código**: https://github.com/user/ejercicio-datos-ia-copiloto
