# Configuracion del directorio de la base de datos 

# Importaciones
# Importa desde Os
import os
# Importa desde Screen
from pantalla import mostrar_mensaje


# Configura el directorio de la base de datos
# Directorio donde se guardara la base de datos
#./"
DIRECTORIO_BASE = "..\\"
#"base_datos/"
DIRECTORIO_DATOS = "base_datos\\"
DIRECTORIO_BASE_DATOS =  f"{DIRECTORIO_BASE}{DIRECTORIO_DATOS}"


# Configura el nombre y la extension de la base de datos
NOMBRE_ARCHIVO = "inventario"
EXTENSION_ARCHIVO = ".db"
ARCHIVO_BASE_DATOS =  f"{NOMBRE_ARCHIVO}{EXTENSION_ARCHIVO}" 


# Ruta completa de la base de datos
BASE_DATOS = f"{DIRECTORIO_BASE_DATOS}{ARCHIVO_BASE_DATOS}"


# Configurar la ruta del archivo de base de datos
DATA_BASE = os.path.join(os.path.dirname(__file__), BASE_DATOS)