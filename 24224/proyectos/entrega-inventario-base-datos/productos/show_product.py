# Mostrar Producto

# Importaciones
# Importa desde Colorama
from colorama import Style, Fore
# Importa desde el paquete de pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje


# Titulo de Buscar Productos
def mostrar_titulo_busquedas():
    # Importa desde Pantalla
    from pantalla import mostrar_linea_separacion

    mostrar_linea_separacion()
    print(f"{Style.BRIGHT}{Fore.CYAN}               Buscando Productos               \n")
    mostrar_linea_separacion()


# Funcion para Mostrar un Producto
def mostrar_producto():
    # Importa desde Productos 
    from productos import buscar_productos, imprime_producto

    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo de Busquedas
    mostrar_titulo_busquedas()

    # Obtiene el Listado de los Productos
    producto = buscar_productos("Mostrar")    

    # Imprime los productos en pantalla
    if (producto):
        # Muestra los datos del producto
        imprime_producto(producto)

        # Muestra un mensaje en pantalla
        mostrar_mensaje("")

    else:
                # Muestra un mensaje en pantalla
        mostrar_mensaje("Producto no encontrado...")
