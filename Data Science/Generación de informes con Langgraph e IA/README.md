# Aprende a generar informes con LangGraph e IA

## Introducción

Este ejercicio implementa un agente avanzado para la generación automática de reportes utilizando LangGraph e inteligencia artificial (IA). A diferencia de los enfoques tradicionales basados en plantillas o análisis estadísticos predefinidos, esta solución aprovecha los últimos avances en modelos de lenguaje para crear equipos virtuales de analistas especializados, realizar entrevistas simuladas y sintetizar hallazgos en un informe coherente y bien estructurado.

### Usos y Aplicaciones

Este sistema puede ser aplicado en diversos contextos:

• **Investigación de mercado**: análisis de tendencias, competidores o nuevos mercados.

• **Análisis de políticas**: evaluación de políticas públicas desde diferentes perspectivas.

• **Reportes sectoriales**: informes detallados sobre sectores específicos.

• **Síntesis de literatura**: resúmenes de investigaciones en campos específicos.

• **Análisis de impacto**: evaluación del impacto potencial de nuevas tecnologías.

### Aspectos clave del proyecto

El empleo de **LangGraph** se fundamenta en que es un framework de vanguardia para la creación de agentes de IA basados en grafos de estados. A diferencia de los enfoques tradicionales que utilizan cadenas secuenciales, LangGraph permite:

• Crear flujos de trabajo no lineales con bifurcaciones condicionales.
• Mantener conversaciones multi-turno con memoria a largo plazo.
• Coordinar múltiples sub-agentes especializados.
• Permitir la intervención humana en puntos estratégicos.

Las **entrevistas simuladas** constituyen otro aspecto innovador donde:

• Se crean perfiles de analistas virtuales especializados.

• Cada analista formula preguntas relevantes a su área de conocimiento.

• Se busca información actualizada en fuentes como Tavily y Wikipedia.

• Se generan respuestas informativas combinando la información obtenida con el perfil del experto.

La **paralelización con Send()** representa una de las innovaciones técnicas del proyecto mediante la implementación de entrevistas paralelas mediante el método Send() de LangGraph, que permite ejecutar múltiples flujos de entrevista simultáneamente, optimizando significativamente el tiempo de procesamiento.

## Contenido del Notebook

En el notebook se desarrollan los siguientes apartados:

### 0. Planteamiento del problema y configuración del entorno

Esta sección introduce el problema de la generación automática de informes completos y prepara el entorno de desarrollo con todas las dependencias necesarias. Veremos cómo configurar el acceso a modelos de lenguaje como GPT-4 y Google Gemini.

### 1. Aprendiendo sobre LangGraph: framework avanzado para la creación de agentes IA

En este apartado se introduce a LangGraph, un framework que utiliza grafos de estados para modelar el comportamiento de agentes de IA. Aprenderemos sobre sus conceptos fundamentales (nodos, aristas y condiciones) y sus ventajas frente a otros enfoques más tradicionales. Esto nos permitirá comprender cómo funciona el sistema que se desarrolla posteriormente en detalle.

### 2. Implementación del agente

La arquitectura que se desarrolla en el notebook se basa en un diseño modular implementado como un grafo de estados interconectados, donde cada nodo representa una funcionalidad específica en el proceso de generación de reportes. Esta estructura permite un flujo de trabajo flexible, recursivo cuando es necesario, y con capacidad de intervención humana en puntos estratégicos.

Los principales componentes de esta implementación incluyen: modelos de datos, componentes principales y flujo completo del proceso.

#### 2.1. Modelos de datos

En el núcleo de la arquitectura tenemos los modelos de datos que definen la estructura de la información procesada, que incluyen:

• **Analista**: define los perfiles de los expertos virtuales, incluyendo nombre, afiliación, rol y descripción.

• **Perspectivas**: contiene la colección completa de analistas que participan en el proceso.

• **EstadoGeneracionAnalistas**: mantiene el estado del proceso de generación de analistas.

• **EstadoEntrevista**: gestiona la información durante el proceso de entrevista.

• **EstadoInvestigacion**: mantiene el estado global de todo el proceso de investigación.

#### 2.2. Componentes principales

La arquitectura se divide en tres componentes principales que forman un flujo secuencial con posibilidad de retroalimentación:

##### 2.2.1. Generador de analistas virtuales

Este componente crea un equipo diverso de analistas virtuales especializados en diferentes aspectos del tema a investigar. El flujo incluye:

1. Creación inicial de analistas: genera perfiles basados en el tema de investigación.
2. Punto de retroalimentación humana: permite revisar y refinar los perfiles generados.
3. Regeneración (opcional): si hay retroalimentación, refina los analistas incorporando las sugerencias.

##### 2.2.2. Sistema de entrevistas

Una vez generados los analistas, cada uno participa en un proceso de entrevista simulada que incluye:

1. Generación de preguntas: crea preguntas relevantes basadas en el perfil del analista.
2. Búsqueda de información: utiliza servicios como Tavily y Wikipedia para obtener datos actualizados.
3. Generación de respuestas: combina la información obtenida con el perfil del experto.
4. Enrutamiento: decide si continuar la entrevista o finalizarla.
5. Guardado de transcripción: almacena la entrevista completa para su procesamiento.

##### 2.2.3. Generador de reportes

Finalmente, el sistema procesa las entrevistas para crear un informe coherente, siguiendo estos pasos:

1. Redacción de secciones individuales: procesa cada entrevista para generar secciones temáticas.
2. Redacción de introducción: crea una introducción que presente el tema y estructura del informe.
3. Redacción de contenido principal: consolida todas las secciones en un cuerpo coherente.
4. Redacción de conclusión: genera una síntesis de hallazgos y recomendaciones.
5. Finalización del informe: integra todas las partes en un documento estructurado.

#### 2.3. Flujo completo del proceso

El flujo completo del agente sigue esta secuencia lógica:

1. Inicialización: el proceso comienza con la definición del tema y parámetros iniciales.
2. Generación de analistas: se crean perfiles especializados que cubrirán distintos aspectos del tema.
3. Intervención humana: se permite refinar los analistas generados según necesidades específicas.
4. Entrevistas paralelas: cada analista participa en una entrevista simulada para recopilar información.
5. Procesamiento de entrevistas: las transcripciones se transforman en secciones estructuradas.
6. Generación de componentes del informe: se crean introducción, cuerpo y conclusión.
7. Consolidación final: se integran todos los componentes en un informe coherente.

La arquitectura completa se implementa como un grafo principal que coordina los subgrafos especializados, permitiendo una ejecución flexible y robusta del proceso completo de generación de reportes.

### 3. Paralelización y formateo del informe

Una vez desarrollado el flujo, se optimiza su rendimiento mediante la paralelización de entrevistas y la consolidación de los resultados en un informe final estructurado, con introducción, cuerpo y conclusión.

### 4. Ejecución del Agente y Generación de un informe de ejemplo

Contiene la demostración práctica del sistema completo, incluyendo:

1. Definir los parámetros iniciales (tema y número de analistas).
2. Ejecutar el grafo hasta el punto de retroalimentación humana.
3. Revisar los analistas generados y proporcionar retroalimentación si es necesario.
4. Continuar con la ejecución completa del grafo.
5. Revisar y presentar el informe final generado.

### 5. Conclusiones y Aplicaciones Prácticas

Análisis de las ventajas del enfoque, posibles aplicaciones en diferentes contextos y discusión sobre limitaciones y oportunidades de mejora.

## Requisitos técnicos

### Software

• Python 3.11.x o superior
• Entorno de Jupyter (preferiblemente Google Colab)

### Librerías principales

Las dependencias necesarias incluyen:

• LangGraph y sus componentes.

• LangChain Community y Core.

• APIs de modelos de lenguaje (OpenAI, Google Gemini).

• Herramientas de búsqueda (Tavily, Wikipedia).

• Librerías estándar para manejo de datos (Pandas, Matplotlib).

### Configuración

Para instalar las dependencias necesarias, ejecuta:

```bash
pip install -r requirements.txt
```

Después de la instalación:

1. Obtener API keys para OpenAI, Google AI, Tavily, etc.
2. Configurar las variables de entorno con las claves necesarias.
3. Ejecutar el notebook siguiendo las instrucciones paso a paso.

## Licencia

Este proyecto ha sido elaborado en el marco de la Iniciativa Aporta (datos.gob.es), desarrollada por el Ministerio para la Transformación Digital y de la Función Pública a través de la Entidad Pública Empresarial Red.es, y en colaboración con la Dirección General del Dato.

**Aviso legal**: Esta obra está sujeta a una licencia Atribución 4.0 de Creative Commons (CC BY 4.0). Está permitida su reproducción, distribución, comunicación pública y transformación para generar una obra derivada, sin ninguna restricción, siempre que se cite al titular de los derechos (Ministerio de Asuntos Económicos y Transformación Digital a través de la Entidad Pública Empresarial Red.es). La licencia completa se puede consultar en: https://creativecommons.org/licenses/by/4.0
