# Investigación de Algoritmos de Búsqueda

## Requisitos 
- Python 3.x: Si no lo tienes instalado, puedes descargarlo desde [python.org](https://www.python.org/downloads/).
- pip: El gestor de paquetes de Python. Generalmente se instala automáticamente con Python 3.

## Configuración del Entorno Virtual

Se recomienda usar entornos virtuales para evitar conflictos entre las dependencias de diferentes proyectos. Sigue estos pasos para crear y activar un entorno virtual:

```bash
# Instalar la herramienta virtualenv si no está instalada
pip install virtualenv

# Crear un nuevo entorno virtual
virtualenv venv

# Activar el entorno virtual (Windows)
venv\Scripts\activate
# o (Linux/macOS)
source venv/bin/activate
```

## Instalación de Dependencias
Para instalar las librerías necesarias, ejecuta el siguiente comando después de activar tu entorno virtual:

```bash
pip install psutil
```

## Búsqueda Lineal 

En esta búsqueda se hace una iteración elemento por elemento dentro de la lista, en lista grandes con muchos elementos no es del todo óptimo porque lo vuelve demasiado lento, en listas pequeñas si puede ser útil este tipo de búsqueda.

## Búsqueda Binaria

En esta búsqueda lo primero que se hace es obtener el valor que está en el medio de la lista si el valor obtenido en igual al que se está buscando se devuelve ese valor, si es mayor entonces se descarta los elementos de la derecha y en cambio, si es menor se descartan los elementos de la izquierda, y así sucesivamente hasta encontrar el elemento buscado. Este búsqueda es adecuada para cuando la lista contiene muchos elementos.

## Conclusión 

La búsqueda lineal se podría usar para cuando la lista tiene pocos elementos pero si tenemos una lista con demasiados elementos esta búsqueda es demasiado lenta, por ello es más conveniente usar la búsqueda binaria que responde mejor ante listas con muchos elementos, otro tema a tener en cuenta es que la búsqueda lineal se puede usar tanto en listas ordenadas como en listas desordenadas, en cambio la búsqueda binaria solo se puede usar en listas ordenadas, por ende si se quiere usar el algoritmo de búsqueda binaria primero se debería de validar que la lista esté ordenada y ordenarla en caso de no estarlo.