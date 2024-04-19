# INTRODUCCIÓN

La transición hacia una movilidad más sostenible se ha convertido en una prioridad global, situando al vehículo eléctrico (VE) en el centro de numerosas discusiones sobre el futuro del transporte. En España, esta tendencia hacia la electrificación del parque automovilístico no solo responde a un creciente interés por parte de los consumidores en tecnologías más limpias y eficientes, sino también a un marco regulatorio y de incentivos diseñado para acelerar la adopción de estos vehículos. Con una creciente oferta de modelos eléctricos disponibles en el mercado, los vehículos eléctricos representan una pieza clave en la estrategia del país para reducir las emisiones de gases de efecto invernadero, mejorar la calidad del aire en las ciudades y fomentar la innovación tecnológica en el sector automotriz.

Sin embargo, la penetración de los vehículos eléctricos en el mercado español enfrenta una serie de desafíos, desde la infraestructura de carga hasta la percepción y el conocimiento del consumidor sobre estos vehículos. La expansión de la red de carga, junto con las políticas de apoyo y los incentivos fiscales, son fundamentales para superar las barreras existentes y estimular la demanda. A medida que España avanza hacia sus objetivos de sostenibilidad y transición energética, el análisis de la evolución del mercado de vehículos eléctricos se convierte en una herramienta esencial para entender el progreso realizado y los obstáculos que aún deben superarse. En este ejercicio, exploraremos la actual situación de la penetración de los vehículos eléctricos en España y las perspectivas de futuro de esta tecnología disruptiva en el transporte.

# OBJETIVOS

Este ejercicio se centra en mostrar al lector técnicas para el tratamiento, visualización y análisis avanzado de datos abiertos mediante Python. Adoptaremos para ello el enfoque “aprender haciendo”, de tal forma que el lector pueda comprender la utilización de estas herramientas en el contexto de la resolución de un reto real y de actualidad como es el estudio de la penetración del VE en España. Este enfoque práctico no solo mejora la comprensión de las herramientas de ciencia de datos, sino que también prepara a los lectores para aplicar estos conocimientos en la resolución de problemas reales, ofreciendo una experiencia de aprendizaje rica y directamente aplicable a sus propios proyectos.

# RECURSOS

En este apartado indicamos los elementos necesarios para poder realizar el ejercicio:

## 🛠 Herramientas

- **Lenguaje de programación:** Python.
- **Plataforma:** [Jupyter Notebooks](https://jupyter.org/) - aplicación web que permite crear y compartir documentos que contienen código vivo, ecuaciones, visualizaciones y texto narrativo. Se utiliza ampliamente para la ciencia de datos, análisis de datos, aprendizaje automático y educación interactiva en programación.
- **Principales librerías y módulos:**
    - Manipulación de datos: [Pandas](https://pandas.pydata.org/) - librería de código abierto que proporciona estructuras de datos de alto rendimiento y fáciles de usar, así como herramientas de análisis de datos.
    - Visualización de datos:
        - [Matplotlib](https://matplotlib.org/): librería para crear visualizaciones estáticas, animadas e interactivas en Python.
        - [Seaborn](https://seaborn.pydata.org/): librería basada en Matplotlib. Proporciona una interfaz de alto nivel para dibujar gráficos estadísticos atractivos e informativos.
    - Estadística y algoritmia:
        - [Statsmodels](https://www.statsmodels.org/): librería que proporciona clases y funciones para la estimación de muchos modelos estadísticos diferentes, así como para realizar pruebas y exploración de datos estadísticos.
        - [Pmdarima](https://pypi.org/project/pmdarima/): librería especializada en la modelización automática de series temporales, facilitando la identificación, el ajuste y la validación de modelos para pronósticos complejos.

## 💾 Conjuntos de datos

Datos de matriculaciones de vehículos en España publicados por la Dirección General de Tráfico (DGT). Disponibles vía:
- [Catálogo de Datos Abiertos](https://datos.gob.es/es/catalogo/e00130502-matriculacion-de-vehiculos) del Gobierno de España.
- [Portal estadístico](https://sedeapl.dgt.gob.es/WEB_IEST_CONSULTA/) de la DGT.

<sub>*Los datos utilizados en este ejercicio fueron descargados el 04 de marzo de 2024. La licencia aplicable a este conjunto de datos puede encontrarse en [https://datos.gob.es/avisolegal](https://datos.gob.es/avisolegal)*</sub>

# MANOS A LA OBRA

¡Pasamos a la acción! Para desarrollar este ejercicio paso a paso accede al Notebook [aquí](https://github.com/Admindatosgobes/Laboratorio-de-Datos/tree/main/Data%20Science/Ruta%20a%20la%20electrificaci%C3%B3n%20de%20la%20Movilidad/Codigo/Notebook.ipynb). También tienes a tu disposición la versión en colab [aquí](https://colab.research.google.com/github/Admindatosgobes/Laboratorio-de-Datos/blob/main/Data%20Science/Ruta%20a%20la%20electrificaci%C3%B3n%20de%20la%20Movilidad/Codigo/Notebook.ipynb).
