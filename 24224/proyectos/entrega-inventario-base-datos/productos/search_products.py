# Search Products

# Importaciones
# Importa desde Colorama
#from colorama import Style, Fore
# Importa desde Pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje


# Funcion para buscar productos
def buscar_productos():
    # Importamos el inventario de productos
    from inventory import inventario_productos
    # Importa el Titulo 
    from productos import mostrar_titulo_busquedas 

    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_busquedas()

    # Muestra un mensaje en pantalla
    mostrar_mensaje("Opción no implementada...")
