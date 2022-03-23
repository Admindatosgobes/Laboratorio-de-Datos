# Ejecutar Morph-KGC en local para generar datos en RDF a partir de CSV

1. Tener instalado Python v3.7 o superior en el ordenador 
2. Ejecutar `python3 -m pip install morph-kgc` 
3. Descargar el archivo de configuración de esta carpeta en el ordenador.
4. Situar en una misma carpeta: la configuración, los mappings y los datos.
5. Cambiar el path de los datos en los mappings al actual (e.g.,`/Users/myuser/Downloads/datos-a-rdf/`)
6. Traducir el mapping con [Matey](https://rml.io/yarrrml/matey/) y descargar el RML (copiar el contenido del `Output RML`).
7. Guardar el nuevo mapping en RML en la misma carpeta como `mapping.ttl`
8. Ejectuar Morph-KGC `python3 morph_kgc config.ini` y los resultados estarán en la carpeta output.
