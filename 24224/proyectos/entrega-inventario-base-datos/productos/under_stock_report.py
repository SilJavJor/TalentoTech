# Reporte Bajo Sotck

# Importaciones
# Importa desde Colorama
from colorama import Style, Fore
# Importa desde datos
from gestor_base_datos import lista_reporte_bajo_stock
# Importa desde el paquete de pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje


# Subtitulo de Reporte de Bajo Stock
def mostrar_subtitulo_reporte_bajo_stock():
    # 
    print(f"{Style.BRIGHT}{Fore.YELLOW} Limite maximo para la cantidad de productos a mostrar \n")


# Titulo de Reporte de Bajo Stock
def mostrar_titulo_reporte_bajo_stock():
    # Importa desde Pantalla
    from pantalla import mostrar_linea_separacion

    mostrar_linea_separacion()
    print(f"{Style.BRIGHT}{Fore.CYAN}          Reporte de Bajo Stock              \n")
    mostrar_linea_separacion()

    # Muestra el subtitulo para el Reporte de Bajo Stock
    mostrar_subtitulo_reporte_bajo_stock()


# Funcion para buscar productos
def reporte_bajo_stock():
    # Importa desde Productos 
    from productos import imprime_productos, ingresa_cantidad

    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para el Reporte de Bajo Stock
    mostrar_titulo_reporte_bajo_stock()

    # Ingreso y validacion de la variable cantidad
    cantidad_limite = ingresa_cantidad()

    # Obtiene el Listado de los Productos
    productos = lista_reporte_bajo_stock(cantidad_limite)

    # Imprime los productos en pantalla
    if (productos):
        # Imprime todos los productos en el inventario
        imprime_productos(productos)

        # Muestra un mensaje en pantalla
        mostrar_mensaje("")

    else:
        # Muestra un mensaje en pantalla
        mostrar_mensaje("No hay productos para mostrar...")
