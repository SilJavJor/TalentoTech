#
from pantalla import limpiar_pantalla, mostrar_mensaje

# Funcion de Eliminacion de Productos
def eliminar_productos():
    # Importamos el inventario de productos
    from inventory import inventario_productos
    #
    from productos.products import mostrar_titulo_eliminacion

    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_eliminacion()

    # Muestra un mensaje en pantalla
    mostrar_mensaje("Opción no implementada...")
