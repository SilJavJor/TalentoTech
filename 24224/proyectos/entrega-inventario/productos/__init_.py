# Este archivo inicializa el paquete y define qué modulos o funciones se pueden importar directamente


from .menu_products import mostrar_menu_productos
from .products import seleccionar_opciones_menu_productos


"""
from .products import ( seleccionar_opciones_menu_productos, 
                        mostrar_titulo_agregacion, 
                        mostrar_titulo_modificacion,
                        mostrar_titulo_eliminacion,
                        mostrar_titulo_busquedas,
                        mostrar_titulo_listados)
"""

from .add_products import agregar_productos
from .remove_products import eliminar_productos
#from add_products import eliminar_producto
from .update_products import modificar_productos
from .show_products import mostrar_productos
