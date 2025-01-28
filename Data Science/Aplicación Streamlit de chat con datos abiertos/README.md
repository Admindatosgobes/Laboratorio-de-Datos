# Chatea con datos públicos usando Streamlit e Inteligencia Artificial

## Descripción
Este ejercicio práctico desarrolla una aplicación web usando Streamlit que permite cargar datasets del catálogo del portal de datos abiertos [datos.gob.es](https://datos.gob.es/es/catalogo) y realizar consultas en lenguaje natural aprovechando las capacidades de los modelos de lenguaje (LLM).

## Marco Teórico

### Large Language Models (LLM)
Los modelos de lenguaje grandes son sistemas de IA entrenados para comprender y generar texto en lenguaje natural. En este ejercicio, actúan como intermediarios entre las consultas en lenguaje humano y el código de análisis necesario.

### Framework y Modelo
La solución se implementa **sin un framework específico** y construye la funcionalidad desde cero con llamadas directas a la API del LLM. Existen alternativas populares como:

- **LangChain**: framework popular para desarrollo de aplicaciones con LLMs.
- **LlamaIndex**: especializado en estructurar y procesar datos para LLMs.
- **Semantic Kernel**: framework de Microsoft para integración de LLMs.
- **Haystack**: framework para crear pipelines de procesamiento de lenguaje natural.

#### Razones para construir desde cero
- Control completo sobre cada componente del sistema.
- Mejor comprensión del funcionamiento interno.
- Mayor flexibilidad para personalizar la lógica de negocio.
- Código más fácil de mantener y probar.
- Mejor adaptabilidad a diferentes necesidades.

### Modelo Gemini
Se utiliza Gemini, el modelo más avanzado de Google, aunque existen alternativas como:

- GPT-4 de OpenAI.
- Claude de Anthropic.
- LLAMA 2 de Meta.
- Diversos modelos open source.

#### Ventajas de Gemini
- Nivel gratuito generoso.
  - 15 solicitudes por minuto.
  - 1 millón de tokens por minuto.
  - 1,500 solicitudes por día.
- API simple y bien documentada.

Se utiiza una arquitectura modular, por lo que se permite cambiar de modelo fácilmente.

## Contexto
Tradicionalmente, el análisis de datos requiere conocimientos de programación y consultas estructuradas. Esta aplicación busca democratizar el acceso a los datos mediante:

- Interfaz intuitiva en lenguaje natural.
- Procesamiento automático de consultas.
- Visualización interactiva de resultados.

### Desafíos abordados
- Brecha entre lenguaje natural y código.
- Necesidad de conocimientos técnicos.
- Complejidad en la visualización de datos.

## Solución propuesta
La aplicación implementa un flujo de trabajo en tres fases:

### 1. Procesamiento de Consultas
- Generación de contexto del dataset.
- Combinación con la pregunta del usuario.
- Envío al modelo de lenguaje.

### 2. Generación de Código
- Traducción de lenguaje natural a código Python.
- Validación y optimización del código.
- Manejo de errores y reintentos.

### 3. Visualización
- Ejecución segura del código.
- Generación de gráficos y tablas.
- Presentación interactiva de resultados.

## Estructura del proyecto (algunos de los archivos se crean directamente desde el notebook)
- `app.py`: aplicación principal Streamlit
- `funciones.py`: funciones auxiliares y utilitarias
- `constantes.py`: configuración y claves API
- `datasets.json`: catálogo de datasets disponibles
- `requirements.txt`: dependencias necesarias

## Requisitos técnicos

### Software
- Python 3.x
- Streamlit

### Bibliotecas principales
```python
import pandas as pd         # Manipulación de datos
import streamlit as st      # Interfaz web
import matplotlib.pyplot    # Visualización
import google.generativeai  # API de Gemini
import requests            # Peticiones HTTP
import pyngrok             # Túneles para desarrollo
```

## Instalación
```bash
pip install -r requirements.txt
```

### Configuración
1. Obtener API key de [Google AI Studio](https://ai.google.dev/).
2. Crear archivo `constantes.py` con las claves.
3. Configurar ngrok para la generación de tunnel desde colab.

## Referencias
### Recursos técnicos
- [Documentación de Streamlit](https://docs.streamlit.io/)
- [API de Gemini](https://ai.google.dev/docs)
- [Portal datos.gob.es](https://datos.gob.es/es/catalogo)


## Conclusiones

### Ventajas del enfoque
1. **Accesibilidad mejorada**
   - Interfaz en lenguaje natural.
   - Sin necesidad de conocimientos técnicos.
   - Resultados visuales inmediatos.

2. **Flexibilidad y extensibilidad**
   - Arquitectura modular.
   - Fácil cambio de modelo LLM.
   - Adaptable a diferentes fuentes de datos.

3. **Desarrollo iterativo**
   - Sistema de reintentos automático.
   - Manejo robusto de errores.
   - Feedback inmediato.

### Limitaciones y oportunidades de mejora
- Dependencia de la calidad del modelo LLM.
- Necesidad de conexión a Internet.
- Posibles limitaciones de la API gratuita.
- Oportunidades de mejora:
  - Implementar caché de resultados.
  - Añadir más fuentes de datos.
  - Mejorar la interpretación de consultas.
  - Ampliar tipos de visualizaciones.

## Licencia
Este proyecto ha sido elaborado en el marco de la Iniciativa Aporta (datos.gob.es), desarrollada por el Ministerio para la Transformación Digital y de la Función Pública a través de la Entidad Pública Empresarial Red.es, y en colaboración con la Dirección General del Dato.

Aviso legal: Esta obra está sujeta a una licencia Atribución 4.0 de Creative Commons (CC BY 4.0). Está permitida su reproducción, distribución, comunicación pública y transformación para generar una obra derivada, sin ninguna restricción, siempre que se cite al titular de los derechos (Ministerio de Asuntos Económicos y Transformación Digital a través de la Entidad Pública Empresarial Red.es). La licencia completa se puede consultar en: https://creativecommons.org/licenses/by/4.0

