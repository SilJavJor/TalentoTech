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
from .operations_products import ( leer_producto, agregar_producto, actualizar_producto, eliminar_producto, 
                                    listar_productos )
from .queries import ( consulta_creacion_tabla_productos, consulta_agregar_producto, 
                        consulta_actualizar_producto, consulta_eliminar_producto,
                        consulta_listar_todos_productos )


#
print("Inicializando el paquete de Base de Datos")