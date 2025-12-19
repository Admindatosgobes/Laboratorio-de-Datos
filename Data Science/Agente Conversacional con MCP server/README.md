# Agente Conversacional con MCP Server para datos.gob.es


## Descripción

Este ejercicio práctico desarrolla un sistema de agente conversacional de IA con arquitectura desacoplada que permite explorar el catálogo nacional de datos abiertos de España (datos.gob.es) mediante consultas en lenguaje natural. Esta solución facilita el acceso a datos gubernamentales permitiendo a cualquier usuario interactuar mediante preguntas simples en español, complementando los mecanismos de búsqueda facetada y filtrado ya disponibles en el portal.

El sistema implementa una arquitectura de microservicios donde un agente de IA (construido con Google Agent Development Kit), que interpreta las preguntas de los usuarios, se comunica con un servidor de herramientas, que expone herramientas para consultar la API del portal, y que implementa el protocolo MCP (Model Context Protocol). Esta separación de responsabilidades hace que el sistema sea mantenible, escalable y extensible, mientras que el uso de MCP garantiza interoperabilidad con diferentes modelos de lenguaje.

El proyecto completo está implementado usando Docker Compose para facilitar el despliegue, FastAPI para las APIs REST, httpx para peticiones asíncronas, y mcp.server.fastmcp para la implementación del servidor de herramientas. Es una base educativa ideal para aprender sobre arquitectura de agentes, programación asíncrona, integración de APIs externas y orquestación de microservicios.


## Contenido del Notebook

En el notebook se desarrollan los siguientes apartados:

### 0. Planteamiento del problema y configuración del entorno
Introduce el desafío de hacer accesible el catálogo de datos.gob.es sin requerir conocimientos técnicos, y explica la solución propuesta: un agente conversacional con arquitectura desacoplada usando MCP.

### 1. Componente Core: El Servidor de Herramientas (MCP)
Implementa el servidor MCP usando FastMCP, definiendo cuatro herramientas fundamentales: `buscar_datasets()`, `listar_tematicas()`, `obtener_detalle_dataset()` y `buscar_por_tematica()`. Cada herramienta envuelve la complejidad de consultar la API de datos.gob.es y devuelve resultados estructurados y limpios.

### 2. Componente core: el agente conversacional (Google ADK)
Crea el agente conversacional usando Google ADK (Agent Development Kit), configurando el `LlmAgent` con un prompt de sistema especializado y conectándolo al servidor MCP mediante `MCPToolset`. El agente se expone a través de una API FastAPI con interfaz web interactiva.


### 3. Archivos de configuración y soporte
Configura la infraestructura completa con `docker-compose.yml`, definiendo dos servicios independientes (agente y servidor MCP) que se comunican a través de una red privada. Incluye configuración de variables de entorno, dependencias y mapeo de puertos.

### 4. Despliegue y pruebas del sistema
Guía paso a paso para levantar el sistema completo, verificar que ambos servicios están funcionando correctamente, y acceder a la interfaz web del agente en `http://localhost:8080`.

### 5. Ejecución del proyecto
Demuestra casos de uso reales con ejemplos concretos de consultas en lenguaje natural, mostrando cómo el agente encadena herramientas automáticamente, procesa respuestas complejas y las presenta de forma legible.

### 6. Aplicación práctica y conclusiones
Analiza los conceptos técnicos aprendidos (arquitectura desacoplada, MCP, Google ADK, Docker Compose, programación asíncrona), presenta casos de uso prácticos en periodismo, investigación y gobierno abierto, y propone extensiones futuras del sistema.


## Conceptos Clave

### Model Context Protocol (MCP)

MCP es un protocolo estándar abierto que permite a los agentes de IA descubrir y usar herramientas externas de forma dinámica. Actúa como un "contrato" que define cómo los agentes y los servidores de herramientas se comunican entre sí, permitiendo que el agente pregunte al servidor qué herramientas tiene disponibles y cómo usarlas correctamente.

En este ejercicio, usamos **FastMCP** (mcp.server.fastmcp), una implementación ligera del protocolo que permite crear un servidor de herramientas con muy poco código. Las características clave incluyen:

- **Descubrimiento automático**: el agente puede preguntar dinámicamente qué herramientas están disponibles
- **Definición declarativa**: cada herramienta declara sus parámetros y tipos usando decoradores Python
- **Agnóstico al modelo**: funciona con cualquier modelo de IA (GPT, Claude, Gemini, Llama, etc.)
- **Basado en estándares web**: usa HTTP/JSON para facilitar integración y debugging

### Google Agent Development Kit (ADK)

Google ADK es un framework para crear agentes de IA conversacionales completos. Proporciona `LlmAgent`, una clase que:

- Comprende y procesa lenguaje natural usando modelos como Gemini
- Puede usar herramientas externas (en nuestro caso, las provistas por el servidor MCP)
- Mantiene estado de conversación y contexto entre mensajes
- Se expone fácilmente a través de APIs REST usando FastAPI

El agente no tiene conocimiento intrínseco de cómo consultar datos.gob.es, pero descubre dinámicamente las herramientas disponibles en el servidor MCP mediante `MCPToolset`, que actúa como puente de conexión.

### Arquitectura Desacoplada

La separación completa entre el agente (que comprende lenguaje natural) y el servidor de herramientas (que consulta APIs externas) no es solo una decisión técnica, sino un principio arquitectónico que aporta:

**Ventajas principales:**

- **Reutilización**: el mismo servidor MCP puede ser consumido por múltiples agentes o aplicaciones.

- **Mantenibilidad**: cambios en la API externa solo afectan al servidor MCP, no al agente.

- **Escalabilidad**: cada componente se escala independientemente según sus necesidades.

- **Flexibilidad**: podemos cambiar el modelo de IA sin modificar el servidor de herramientas.

- **Testing**: las herramientas se prueban de forma aislada sin ejecutar el agente


## Flujo de Trabajo del Sistema

El sistema sigue esta secuencia lógica cuando un usuario hace una consulta:

1. **Usuario envía mensaje**: Por ejemplo, *"Busca datasets sobre clima"* en la interfaz web.
2. **Agente analiza intención**: El LlmAgent determina qué herramienta necesita invocar.
3. **Invocación de herramienta**: El agente llama al servidor MCP solicitando `buscar_datasets(titulo="clima")`.
4. **Consulta a API externa**: El servidor MCP hace una petición asíncrona a `https://datos.gob.es/apidata`.
5. **Procesamiento de respuesta**: El servidor limpia el JSON complejo y extrae solo datos relevantes.
6. **Devolución al agente**: El servidor MCP devuelve un diccionario Python simple.
7. **Formulación de respuesta**: El agente genera una respuesta en lenguaje natural.
8. **Visualización**: El usuario ve la respuesta con indicadores de las herramientas usadas.

El agente puede encadenar múltiples herramientas automáticamente para consultas complejas como *"Busca datasets de salud y dame detalles del primero"*.

## Requisitos Técnicos

### Software
- Docker 20.10 o superior
- Docker Compose 2.0 o superior
- Python 3.9+ (si se ejecuta sin Docker)

### Bibliotecas Principales

**Servidor MCP:**
```python
import httpx              # Peticiones HTTP asíncronas
from mcp.server.fastmcp import FastMCP  # Servidor de herramientas
import json               # Procesamiento de respuestas
```

**Agente ADK:**
```python
from google.generativeai.adk import LlmAgent  # Agente conversacional
from google.generativeai.adk.mcp import MCPToolset  # Conexión a MCP
from fastapi import FastAPI              # API REST
import uvicorn                           # Servidor ASGI
```

## Usos y Aplicaciones

Este sistema puede aplicarse en diversos contextos reales:

### Periodismo de Datos
Permite a periodistas encontrar rápidamente estadísticas gubernamentales para artículos mediante preguntas como *"Busca datasets recientes sobre contaminación"*, eliminando la necesidad de navegar manualmente el portal o construir queries complejas. Acelera significativamente la fase de descubrimiento en investigaciones.

### Investigación Académica
Estudiantes e investigadores pueden mantener conversaciones iterativas refinando búsquedas: *"Lista temáticas", "Busca datasets de demografía", "Dame detalles del dataset sobre migración"*. El agente actúa como asistente de investigación que entiende contexto y sugiere datasets relacionados.

### Transparencia y Gobierno Abierto
ONGs y organizaciones pueden monitorear automáticamente nuevos datasets de contratación pública. Extendiendo el servidor MCP con herramientas adicionales (webhooks, análisis), pueden crear workflows que detecten publicaciones relevantes y las analicen sin intervención manual.

### Consultoría y Business Intelligence
Consultoras que necesitan datos económicos y de empleo pueden centralizar búsquedas y cruzar información de múltiples datasets mediante consultas encadenadas como *"Busca datasets de empleo por sectores y luego dame estadísticas del sector tecnológico"*.

### Educación en Ciencia de Datos
Herramienta didáctica para enseñar arquitecturas de software, programación asíncrona, integración de APIs y diseño de agentes de IA. El código es suficientemente simple para ser comprendido, pero completo para ilustrar conceptos avanzados.


## Referencias

### Recursos Técnicos
- [FastMCP Documentation](https://github.com/jlowin/fastmcp) - Implementación rápida del Model Context Protocol
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - Framework web moderno para Python
- [httpx Documentation](https://www.python-httpx.org/) - Cliente HTTP asíncrono
- [Docker Compose](https://docs.docker.com/compose/) - Orquestación de contenedores

### Datos Abiertos
- [Portal datos.gob.es](https://datos.gob.es/es/catalogo) - Catálogo Nacional de Datos Abiertos
- [API de datos.gob.es](https://datos.gob.es/apidata) - Documentación de la API pública


### Model Context Protocol
- [MCP Specification](https://modelcontextprotocol.io/) - Especificación oficial del protocolo



## Conclusiones

### Ventajas del Enfoque

**Accesibilidad democratizada:**

- Interfaz en lenguaje natural elimina barreras técnicas.

- Sin necesidad de conocimientos de programación o APIs.

- Resultados presentados de forma clara y estructurada.

**Arquitectura robusta:**

- Separación de responsabilidades (agente vs. herramientas).

- Protocolo estándar MCP garantiza interoperabilidad.

- Fácil escalado independiente de cada componente.

**Flexibilidad y extensibilidad:**

- Añadir nuevas herramientas al servidor MCP sin tocar el agente.

- Cambiar el modelo de IA subyacente sin modificar herramientas.

- Reutilizable por múltiples agentes o aplicaciones.


### Limitaciones y Oportunidades de Mejora

**Limitaciones actuales:**

- Dependencia de la disponibilidad de la API de datos.gob.es.

- Necesidad de conexión a Internet activa.

- Uso de memoria para sesiones (no persiste entre reinicios).

- Sin autenticación ni rate limiting (no listo para producción).

**Oportunidades de mejora:**

- Implementar caché con Redis para búsquedas frecuentes.

- Añadir persistencia de sesiones con SQLite o PostgreSQL.

- Implementar autenticación (OAuth2, API keys) para producción.

- Añadir rate limiting para prevenir abuso.

- Integrar observabilidad (Prometheus, Grafana, logging estructurado).

- Implementar más herramientas (filtros avanzados, descarga de datasets).

- Añadir soporte multi-idioma con traducción automática.

- Desplegar en la nube (AWS ECS, Google Cloud Run, Kubernetes).



## Licencia

Este proyecto ha sido elaborado en el marco de la Iniciativa Aporta (datos.gob.es), desarrollada por el Ministerio para la Transformación Digital y de la Función Pública a través de la Entidad Pública Empresarial Red.es, y en colaboración con la Dirección General del Dato.

**Aviso legal**: Esta obra está sujeta a una licencia Atribución 4.0 de Creative Commons (CC BY 4.0). Está permitida su reproducción, distribución, comunicación pública y transformación para generar una obra derivada, sin ninguna restricción, siempre que se cite al titular de los derechos (Ministerio para la Transformación Digital y de la Función Pública a través de la Entidad Pública Empresarial Red.es). La licencia completa se puede consultar en: https://creativecommons.org/licenses/by/4.0
