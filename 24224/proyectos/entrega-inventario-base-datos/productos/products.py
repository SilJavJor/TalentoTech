# Productos

# Importaciones
# Importa desde Colorama
from colorama import Style, Fore
# Importa desde Pantalla
from pantalla import mostrar_linea_separacion, limpiar_pantalla, mostrar_mensaje


# Titulo de Agregar Productos
def mostrar_titulo_agregacion():
    mostrar_linea_separacion()
    print(f"{Style.BRIGHT}{Fore.CYAN}              Agregando Productos               \n")
    mostrar_linea_separacion()


# Titulo de Modificar Productos
def mostrar_titulo_modificacion():
    mostrar_linea_separacion()
    print(f"{Style.BRIGHT}{Fore.CYAN}             Modificando Productos              \n")
    mostrar_linea_separacion()


# Titulo de Eliminar Productos
def mostrar_titulo_eliminacion():
    mostrar_linea_separacion()
    print(f"{Style.BRIGHT}{Fore.CYAN}             Eliminando Productos               \n")
    mostrar_linea_separacion()


# Titulo de Buscar Productos
def mostrar_titulo_busquedas():
    mostrar_linea_separacion()
    print(f"{Style.BRIGHT}{Fore.CYAN}               Buscando Productos               \n")
    mostrar_linea_separacion()


# Titulo de Listar Productos
def mostrar_titulo_listados():
    mostrar_linea_separacion()
    print(f"{Style.BRIGHT}{Fore.CYAN}            Inventario de Productos             \n")
    mostrar_linea_separacion()


# Titulo de Reporte de Bajo Stock
def mostrar_titulo_reporte_bajo_stock():
    mostrar_linea_separacion()
    print(f"{Style.BRIGHT}{Fore.CYAN}          Reporte de Bajo Stock              \n")
    mostrar_linea_separacion()


# Titulo de Listados de Productos
def imprime_titulos_listados_completos():
    # Encabezados del listado de productos
    print(f"{Style.BRIGHT} {Fore.GREEN} {'Nombre':<30} {'Descripción':<30} {'Cantidad':>10} {'Precio':>15} {'Categoría':<30}")
    print("=" * 115)


# Controla y ejecuta las opciones del menu
def seleccionar_opciones_menu_productos(opcion_ingresada):
    # Importa desde Productos
    from productos import ( agregar_productos, mostrar_productos, modificar_productos, eliminar_productos, 
                            buscar_productos, reporte_bajo_stock )

    
    if opcion_ingresada == '1':
        # Funcion Agregar Productos
        agregar_productos()

    elif opcion_ingresada == '2':
        # Muestra los productos del inventario
        mostrar_productos()

    elif opcion_ingresada == '3':
        # Funcion Modificar Productos
        modificar_productos()

    elif opcion_ingresada == '4':
        # Funcion Eliminaar Productos
        eliminar_productos()

    elif opcion_ingresada == '5':
        # Funcion Buscar Productos
        buscar_productos()

    elif opcion_ingresada == '6':
        # Funcion Modificar Productos
        reporte_bajo_stock()

    else:
        # Muestra un mensaje en pantalla
        mostrar_mensaje("Opción inválida....")

        #
        opcion_ingresada = 1

    return opcion_ingresada
