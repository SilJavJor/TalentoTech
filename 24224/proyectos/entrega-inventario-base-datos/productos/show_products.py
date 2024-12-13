# Muestra todos los Productos

# Importaciones
# Importa Colorama
from colorama import Style, Fore
# Importa desde datos
from gestor_base_datos import listar_productos
# Importa desde Pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje

# Titulo de Listar Productos
def mostrar_titulo_listados():
    # Importa desde Pantalla
    from pantalla import mostrar_linea_separacion

    mostrar_linea_separacion()
    print(f"{Style.BRIGHT}{Fore.CYAN}            Inventario de Productos             \n")
    mostrar_linea_separacion()


# Muestra por pantalla un listado de todos los productos
def mostrar_productos():
    # Importa desde Productos 
    from productos import imprime_productos

    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_listados()

    # Obtiene el Listado de los Productos
    productos = listar_productos()

    # Imprime los productos en pantalla
    if (productos):
        # Imprime todos los productos en el inventario
        imprime_productos(productos)

        # Muestra un mensaje en pantalla
        mostrar_mensaje("")

    else:
        # Muestra un mensaje en pantalla
        mostrar_mensaje("No hay productos para mostrar...")
