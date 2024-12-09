======================================================================
                APLICACIÓN INVENTARIO (CRUD EN SQLITE)                
======================================================================


1. DESCRIPCIÓN GENERAL
-----------------------
La aplicación es una herramienta para la gestión de productos en una base de datos SQLite.
Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y generar reportes en pantalla como es al Reporte de Bajo Stock 
(con el ingrso de la cantidad minima de Stock).
Reportes en formatos CSV y PDF (si se puede terminar).


2. CARACTERÍSTICAS PRINCIPALES
-------------------------------
- Conexión a una base de datos SQLite llamada `inventario.db`.
  - No es obligatorio que el directorio de creacion exista (la aplicación lo generara de forma automatica).
  - No es obligatorio que la base de datos exista (la aplicación lo generara de forma automatica).
  - No es obligatorio que la tabla exista (la aplicación lo generara de forma automatica).
  - La aplicación genera de forma automatica el directorio "base_datos" (dentro del mismo creara una base de datos con el nombre de archivo 
	"inventario.db" y dentro de la misma una tabla de nombre productos con la especificacion de campos explicada mas adelante)dentro del directorio
	donde se encuentra nuestro archivo main.py.

- Gestión de la tabla `productos` con los campos:
  - id: Identificador único (autoincremental - clave primaria).
  - nombre: Nombre del producto (máximo 30 caracteres).
  - descripcion: Descripción breve (máximo 50 caracteres).
  - cantidad: Cantidad disponible (número entero).
  - precio: Precio del producto (hasta 4 decimales).
  - categoria: Categoría del producto (máximo 30 caracteres).

- Funcionalidades implementadas:
  - Inserción manual de productos.
  - Inserción automática de productos.
  - Búsqueda específica por ID de productos.
  - Actualización de cantidad.
  - Actualización de un producto por ID.
  - Eliminación de productos por ID.
  - Listado de todos los productos con formato legible (por pantalla).
  - Generación de reportes en CSV y PDF (a confirmar segun tiempos disponibles).
  - Creación de gráficos de barras para la visualización de datos (a confirmar segun tiempos disponibles).


4. REQUISITOS
--------------
- Requisitos previos:
  - Python 3.10 o superior instalado (Version de creacion 3.12).

- Bibliotecas requeridas:
  Colorama


5. EJECUCION DE LA APLICACIÓN
-------------------------------
- Ejecucion manual
  - Inatalar Python 3.10 o superior.
  - Instalación de las bibliotecas:
    pip install colorama

- Ejecucion automatica
  - Ejecutar el archivo run.bat (se puede ejecutar por linea de comando o PowerShell).
  - Este archivo instalara las librerias necesarias y ejecutara la aplicación al momento de terminar la instalacion.
