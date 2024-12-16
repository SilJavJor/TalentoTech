# Paquete de Base de Datos

# Importaciones
# Importa desde Conection
from .config import (DIRECTORIO_BASE_DATOS, ARCHIVO_BASE_DATOS, BASE_DATOS, DATA_BASE)

# Importa desde Conection
from .data_base_manager import ( verifica_directorio_base_datos, conectar, desconectar, verifica_conexion, guardar_cambios, 
                                    guardar_cambios_desconectar )

#
from .create_tables import crear_tabla_productos

# Importa desde Operaciones de Productos
from .operations_products import (lee_producto, agrega_producto, actualiza_producto, actualiza_cantidad_producto, 
                                    elimina_producto, lista_productos, lista_reporte_bajo_stock)

#
from .queries import (consulta_creacion_tabla_productos, consulta_agrega_producto, 
                        consulta_actualiza_producto, consulta_actualiza_cantidad_producto, 
                        consulta_elimina_producto, consulta_lista_bajo_stock, 
                        consulta_lista_todos_productos, consulta_lee_producto)


#
print("Inicializando el paquete de Base de Datos")