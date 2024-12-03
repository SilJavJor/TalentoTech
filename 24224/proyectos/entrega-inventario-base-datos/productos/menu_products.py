# Menu Products

# Importaciones
# Importa Colorama
from colorama import Style, Fore


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
    for opcion in opciones_menu_productos:
        # Muestra en pantalla la opcion del menu
        if ((opcion[0]) == (int(opcion_ingresada))):
            #
            print(f"\n Ayuda : {Style.BRIGHT} {Fore.YELLOW} {opcion[2]}\n")


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
