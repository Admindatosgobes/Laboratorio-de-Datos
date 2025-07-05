# Introducción
En la actualidad, la **compartición de datos o data sharing se ha convertido en un pilar imprescindible** para el avance de la analítica y el intercambio de conocimiento, tanto en el ámbito privado como en el público. Las organizaciones de cualquier tamaño y sector –empresas, administraciones públicas, instituciones de investigación, comunidades de desarrolladores o individuos– encuentran un fuerte valor en la capacidad de compartir información de forma segura, fiable y eficiente. Este intercambio no se limita a datos en crudo o datasets estructurados; también se extiende a productos de datos más avanzados, tales como modelos de machine learning entrenados, dashboards analíticos, resultados de experimentos científicos y otros artefactos complejos que generan un gran impacto a través de su reutilización.
En este contexto, la importancia de la gobernanza de estos recursos cobra un papel crítico. No es suficiente con disponer de un método para mover ficheros de un sitio a otro; es necesario **garantizar aspectos clave como el control de acceso** (quién puede leer o modificar cierto recurso), **la trazabilidad y la auditoría** (saber quién ha accedido, cuándo y con qué finalidad) o **el cumplimiento de regulaciones o estándares**, especialmente en entornos empresariales y gubernamentales.
Con el fin de unificar estos requisitos, **Unity Catalog** surge como un almacén de metadatos (metastore) de próxima generación, pensado para centralizar y simplificar la gobernanza de datos y recursos de datos. Originalmente, Unity Catalog formaba parte de los servicios ofrecidos por la plataforma [Databricks](https://www.databricks.com/), pero el proyecto ha dado un salto a la **comunidad de código abierto** para convertirse en un estándar de referencia. Esto implica que ahora es posible utilizarlo, modificarlo y, en definitiva, contribuir a su evolución desde un entorno libre y colaborativo. Con ello, se espera que más organizaciones adopten sus modelos de catálogo y compartición, impulsando la reutilización de datos y la creación de flujos analíticos e innovaciones tecnológicas.
![Unity Catalog Overview](https://github.com/Admindatosgobes/Laboratorio-de-Datos/blob/main/Data%20Science/Unity%20Catalog%3A%20Potenciando%20la%20colaboraci%C3%B3n%20en%20el%20ecosistema%20Data%20e%20IA%20mediante%20c%C3%B3digo%20abierto/Imagenes/uc_overview.png?raw=true)
*Fuente: https://docs.unitycatalog.io/*

# Objetivos
En este proyecto vamos a familiarizarnos con la herramienta Unity Catalog realizando un laboratorio práctico. Repasaremos sus conceptos básicos y desarrollaremos los pasos necesarios para instalar, configurar y utilizar esta herramienta que nos ayuda a gobernar y colaborar en torno a datos y productos de datos, como modelos de inteligencia artificial.

# Caso de uso
Para ello, vamos a tratar de representar un caso de uso real en el que un organismo desea habilitar varios catálogos de datos y recursos de datos relativos a servicios públicos ofrecidos por diferentes ciudades españolas. Entre estos servicios, podremos encontrar recursos relativos a alumbrado, transporte público o gestión de residuos. 
Este organismo dispone de estos datos en un entorno de nube pública, en particular Amazon Web Services (AWS) y utilizará Unity Catalog como herramienta para catalogar dichos datos y habilitar el acceso a los mismos a diferentes tipos de usuario, como un ciudadano que desea consultar datos públicos de los servicios de su ciudad o un ingeniero de datos que debe tener además permisos de modificación del catálogo de datos concretos sobre el que está desarrollando su trabajo.
Adicionalmente, este organismo desarrolla modelos de *machine learning* como parte de su trabajo del día a día: predicción de tiempo de llegada de autobuses, predicción de llenado de contenedores de residuos urbanos, etc. El ciclo de vida de estos modelos se gestiona desde *MLflow*.
![Unity Catalog - Caso de uso](https://github.com/Admindatosgobes/Laboratorio-de-Datos/blob/main/Data%20Science/Unity%20Catalog%3A%20Potenciando%20la%20colaboraci%C3%B3n%20en%20el%20ecosistema%20Data%20e%20IA%20mediante%20c%C3%B3digo%20abierto/Imagenes/uc_use-case.png?raw=true)

# Arquitectura de la solución
En este apartado profundizaremos en el diagrama anterior para explicar la arquitectura de la solución a desplegar:
- **AWS y Amazon S3**:

    Utilizaremos la nube de AWS, concretamente el servicio Amazon S3 (*Simple Storage Service*), como repositorio de los datos de nuestro catálogo. S3 es un servicio ampliamente utilizado gracias a su escalabilidad y bajo coste de almacenamiento. Crearemos un *bucket* en la región de Irlanda (eu-west-1) y subiremos allí los datos que queremos catalogar.

- **MLflow**:

    Utilizaremos MLflow,  plataforma de código abierto diseñada para gestionar de manera integral el ciclo de vida de los modelos de *machine learning*. Mostratemos cómo este tipo de herramientas se integran con servicios de registro como Unity Catalog.

- **Aplicación de Unity Catalog**:

    El código abierto de Unity Catalog se encuentra disponible en su [repositorio oficial de GitHub](https://github.com/unitycatalog/unitycatalog). La aplicación se compone de tres elementos principales:

    - *Backend* (núcleo de la aplicación): Contiene toda la lógica y funcionalidad de Unity Catalog. A veces nos referiremos a este componente como el servidor de Unity Catalog.
    
    - Base de datos (MySQL): Actúa como *metastore*, almacenando los metadatos de catálogos, esquemas, tablas, etc.

    - Interfaz de usuario : Una interfaz web desarrollada a modo de ejemplo (o prototipo) para permitir la interacción visual con los catálogos.
    
    - CLI (*Command Line Interface*): Además de la interfaz de usuario web, Unity Catalog facilita una utilidad que permite a usuarios realizar operaciones como crear catálogos y tablas a través de línea de comandos.

- **Docker Desktop**:
    
    Para simplificar el desarrollo de este laboratorio, desplegaremos la aplicación de Unity Catalog en nuestro propio PC (host), empleando Docker Desktop. De esta manera, cada componente de Unity Catalog (backend, web, base de datos) se ejecutará en su propio contenedor, lo que nos permite abstraernos de las diferencias de sistema operativo entre los lectores.

- **Apache Spark**:

    Utilizaremos [Apache Spark](https://spark.apache.org/), y en particular [Spark SQL](https://spark.apache.org/sql/). Unity Catalog dispone de capacidad de [integración](https://docs.unitycatalog.io/integrations/unity-catalog-spark/) con este motor de transformación y análisis de datos ampliamente utilizado por la comunidad de ingeniería y ciencia de datos.

En el diagrama siguiente se muestran los distintos componentes de la solución anteriormente descritos, así como las comunicaciones entre ellos.
![Unity Catalog - Arquitectura](https://github.com/Admindatosgobes/Laboratorio-de-Datos/blob/main/Data%20Science/Unity%20Catalog%3A%20Potenciando%20la%20colaboraci%C3%B3n%20en%20el%20ecosistema%20Data%20e%20IA%20mediante%20c%C3%B3digo%20abierto/Imagenes/uc_arquitecture.png?raw=true)
Aunque de forma simplificada, el ecosistema de componentes que desplegaremos a lo largo de este laboratorio cubre muchos de los componentes que típicamente nos encontramos en arquitecturas de Data e IA reales.

# Requisitos Previos

En esta sección explicaremos los requisitos previos y recursos necesarios para poder desarrollar este laboratorio. El laboratorio está pensado para desarrollarse en un ordenador personal estándar (Windows, MacOS, Linux).

## Docker Desktop
Para poder desplegar Unity Catalog en nuestro PC, lo primero que debemos hacer es instalar Docker Desktop en el mismo. Para ello, desde [su página oficial](https://www.docker.com/products/docker-desktop/):
- Debemos darnos de alta de forma gratuita indicando *Choose Plan > Docker Personal > Create your account*.

    ![Docker - Get Started](https://github.com/Admindatosgobes/Laboratorio-de-Datos/blob/main/Data%20Science/Unity%20Catalog%3A%20Potenciando%20la%20colaboraci%C3%B3n%20en%20el%20ecosistema%20Data%20e%20IA%20mediante%20c%C3%B3digo%20abierto/Imagenes/docker_get-started.png?raw=true)
    ![Docker - Choose Plan](https://github.com/Admindatosgobes/Laboratorio-de-Datos/blob/main/Data%20Science/Unity%20Catalog%3A%20Potenciando%20la%20colaboraci%C3%B3n%20en%20el%20ecosistema%20Data%20e%20IA%20mediante%20c%C3%B3digo%20abierto/Imagenes/docker_choose-plan.png?raw=true)

- Una vez creada la cuenta, descargaremos Docker Desktop en nuestro PC seleccionando *Go to download* y posteriormente la opción que se corresponda con nuestro sistema operativo (Windows, MacOS o Linux).

   ![Docker - OS](https://github.com/Admindatosgobes/Laboratorio-de-Datos/blob/main/Data%20Science/Unity%20Catalog%3A%20Potenciando%20la%20colaboraci%C3%B3n%20en%20el%20ecosistema%20Data%20e%20IA%20mediante%20c%C3%B3digo%20abierto/Imagenes/docker_OS.png?raw=true)
   
- A continuación, instalamos la aplicación de forma normal siguiendo las instrucciones de la página oficial. En función de tu sistema operativo, deberás autorizar que docker se ejecute en segundo plano o activar virtualización en la BIOS como parte del proceso de instalación.
Si has seguido los pasos de forma correcta, dispondrás del icono de Docker Desktop entre tus aplicaciones y podrás abrirla aunque aún no dispongamos de ningún contenedor en ejecución.

![Docker - Apliación](https://github.com/Admindatosgobes/Laboratorio-de-Datos/blob/main/Data%20Science/Unity%20Catalog%3A%20Potenciando%20la%20colaboraci%C3%B3n%20en%20el%20ecosistema%20Data%20e%20IA%20mediante%20c%C3%B3digo%20abierto/Imagenes/docker_application.png?raw=true)

## Clonar Repositorio Código Laboratorio (TODO)
Debemos ahora clonar el repositorio de GitHub donde hemos habilitado el código y herramientas necesarias para poder desarrollar este proyecto. Para ello, debemos disponer de [Git](https://git-scm.com/) instalado en nuestro PC. 

Una vez instalado, abrimos un terminal en la carpeta donde deseemos desarrollar nuestro proyecto, por ejemplo, Documentos, y ejecutamos el siguiente comando:

```git clone (pte crear GitHub)```

(IMAGEN git clone terminal)

Esto descargará nuestra carpeta de trabajo con todos los archivos necesarios para desarrollar el proyecto.

## Visual Studio Code
Nuestro entorno de trabajo será un Jupyter Notebook python que ejecutaremos y manipularemos a través del editor de código [Visual Studio Code](https://code.visualstudio.com/). Para disponer de esta herramienta en nuestro PC, podemos seguir el enlace de descarga e instrucciones provistas en su [página oficial](https://code.visualstudio.com/download).


Una vez instalado y abierto el editor de código, debemos descargar e instalar algunas extensiones disponibles en su *marketplace* para poder desarrollar este laboratorio. En la barra lateral izquierda encontraremos el icono de extensiones. 

![VS Code - Extensiones](https://github.com/Admindatosgobes/Laboratorio-de-Datos/blob/main/Data%20Science/Unity%20Catalog%3A%20Potenciando%20la%20colaboraci%C3%B3n%20en%20el%20ecosistema%20Data%20e%20IA%20mediante%20c%C3%B3digo%20abierto/Imagenes/vscoce_extensions.png?raw=true)

Buscamos e instalamos las siguientes extensiones:
- Jupyter.

![VS Code - Jupyter](https://github.com/Admindatosgobes/Laboratorio-de-Datos/blob/main/Data%20Science/Unity%20Catalog%3A%20Potenciando%20la%20colaboraci%C3%B3n%20en%20el%20ecosistema%20Data%20e%20IA%20mediante%20c%C3%B3digo%20abierto/Imagenes/vscode_jupyter.png?raw=true)

- Python.

![VS Code - Python](https://github.com/Admindatosgobes/Laboratorio-de-Datos/blob/main/Data%20Science/Unity%20Catalog%3A%20Potenciando%20la%20colaboraci%C3%B3n%20en%20el%20ecosistema%20Data%20e%20IA%20mediante%20c%C3%B3digo%20abierto/Imagenes/vscode_python.png?raw=true)

A continuación, seleccionamos *Archivo > Abrir Carpeta* y seleccionamos nuestra carpeta de trabajo anteriormente clonada desde GitHub.

**(Opcional)** Si deseamos utilizar el estilo visual típico de Jupyter Notebooks, podemos además instalar la extensión ```sam-the-programmer.jupyter-theme```, que nos permite seleccionar entre diferentes temas visuales para nuestro entorno de trabajo.

## Kernel Python
Para poder ejecutar código desde nuestro Notebook en Visual Studio Code, debemos además instalar un Kernel de Python en nuestro PC.

En primer lugar, descargamos e **instalamos Python 3 y su gestor de packetes pip**. Este paso es dependiente de cada plataforma (Windows, MacOS, Linux), pero podemos seguir las instrucciones de manera sencilla desde su [página oficial](https://www.python.org/downloads/). En nuestro caso, al estar trabajando sobre MacOS, podemos ejecutar ```brew install python``` desde un terminal para realizar la instalación.

Una vez instalado, abrimos un terminal en nuestra carpeta de trabajo (carpeta creada al clonar el respositorio de código del laboratorio) y ejecutamos los siguientes comandos:
```
python3 -m venv python-venv
source python-venv/bin/activate
pip install ipykernel
python3 -m ipykernel install --user --name uc-kernel-venv --display-name "UC Catalog (uc-kernel-venv)"
```

Esto creará un entorno virtual de python donde instalaremos todas las librerías Python necesarias para desarrollar el proyecto. También instalará e instanciará un kernel python,  UC Catalog (uc-kernel-venv), que nos permitirá seguir con el resto de pasos de este proyecto sobre este mismo Notebook desde nuestro PC. 

Abrimos para ello el archivo UC-Notebook.ipynb en VS Code desde nuestra carpeta de trabajo, y en la esquina superior derecha seleccionamos *Python Kernel > Jypter Kernel... > UC Catalog (uc-kernel-venv)*.

![VS Code - Kernel](./Imagenes/vscode_kernel.png?raw=true)

## Java Development Kit (JDK)
La instalación del JDK es bastante sencilla y habitual, y disponemos de mucha documentación online para poder realizarla. Dependerá del sistema operativo de nuestro PC (Windows, Linux, MacOS) pero la [guía oficial](https://docs.oracle.com/en/java/javase/23/install/overview-jdk-installation.html) nos guía paso a paso según cuál sea nuestra plataforma.
Tanto si dudas de si ya dispones del JDK instalado en tu PC como si acabas de terminar la instalación del mismo, puedes ejecutar el siguiente comando para validar si Java está ya disponible en tu PC:
%%sh
java --version

# Desarrollo del Ejercicio
¡Pasamos a la acción! Una vez completados los pasos previos, procedemos a desarrollar el ejercicio. Como indicamos en la sección anterior, esta parte del ejercicio la realizaremos sobre este **Notebook ya abierto en nuestro PC en Visual Studio Code**. Puedes descargar el Notebook [aquí](https://enlace.com) 
