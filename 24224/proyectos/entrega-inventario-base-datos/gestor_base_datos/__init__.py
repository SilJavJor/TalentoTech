# Paquete de Base de Datos

# Importaciones
# Importa desde Conection
from .config import DIRECTORIO_BASE_DATOS, ARCHIVO_BASE_DATOS, BASE_DATOS, DATA_BASE
# Importa desde Conection
from .data_base_manager import ( verifica_directorio_base_datos, conectar, desconectar, verifica_conexion, guardar_cambios, 
                                    guardar_cambios_desconectar )
#
from .create_tables import crear_tabla_productos
# Importa desde Operaciones de Productos
from .operations_products import ( leer_producto, insertar_producto, actualizar_producto, eliminar_producto, 
                                    listar_productos )

#
print("Inicializando el paquete de Base de Datos")