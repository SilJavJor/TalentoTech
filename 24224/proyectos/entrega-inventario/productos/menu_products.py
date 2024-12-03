# Menu Products

# Importaciones
from colorama import Style, Fore
from pantalla import mostrar_mensaje
from productos.products import mostrar_productos, modificar_productos, eliminar_productos , buscar_productos, reporte_bajo_stock 
from productos.add_products import agregar_productos 


# Opciones del menu
# id_opcion, item mostrado, ayuda
opciones_menu_productos = [
    [1, " 1 - Agregar producto                 ", "Agrega un producto"],
    [2, " 2 - Mostrar productos                ", "Muestra todos los productos"],
    [3, " 3 - Actualizar cantidad de producto  ", "Actualiza / Modifica la cantidad de un producto"],
    [4, " 4 - Eliminar producto                ", "Elimina un producto"],
    [5, " 5 - Buscar producto                  ", "Busca un producto"],
    [6, " 6 - Reporte de bajo stock            ", "Muestra los productos bajo stock"],
    [0, " ------------------------------------ ", ""],
    [8, " 9 - Salir                            ", "Salir de la Aplicación"]
]


# Muestra la ayuda de los items del menu
def mostrar_ayuda_menu_productos(opcion_ingresada):
    #print(f"\n Ayuda : {Style.BRIGHT}{Fore.YELLOW}{opciones_menu_productos[int(opcion_ingresada)][2]}\n")
    for opcion in opciones_menu_productos:
        # Muestra en pantalla la opcion del menu
        if ((opcion[0]) == (int(opcion_ingresada))):
            #
            print(f"\n Ayuda : {Style.BRIGHT} {Fore.YELLOW} {opcion[2]}\n")


# The commented code block you provided is a function named `seleccionar_opciones_menu_productos` in
# Python. This function takes an `opcion_ingresada` parameter, which presumably represents the user's
# selected option from the menu.
"""
# Controla y ejecuta las opciones del menu
def seleccionar_opciones_menu_productos(opcion_ingresada):
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
        opcion_ingresada = 1

    return opcion_ingresada
"""


# Muestra el menu de productos
def mostrar_menu_productos(opcion_ingresada):
    # Importacion de funcion en forma local
    from inventory import mostrar_teclas_ayuda

    # Recorre cada opción en la lista de opciones_menu_productos
    for opcion in opciones_menu_productos:
        # Muestra en pantalla la opcion del menu
        if ((opcion[0]) == (int(opcion_ingresada))):
            #
            print(f"{Style.BRIGHT}{Fore.CYAN}  >  {opcion[1]}")

        else: 
            # Muestra la opcion en pantalla
            print(f"     {opcion[1]}")

    # Muestra las teclas de ayuda
    mostrar_teclas_ayuda()

    # Muestra la ayuda del menu
    mostrar_ayuda_menu_productos(opcion_ingresada)
