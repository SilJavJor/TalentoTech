# Menu_Products

# Importaciones
from products import agregar_productos, modificar_productos, eliminar_productos , buscar_productos, listar_productos
from screen import limpiar_pantalla, mostrar_mensaje


# Opciones del menú
# id_ opcion, ayuda
opciones_menu_productos = [
    [1, " 1 - Agregar Productos   ", "Agrega un Producto"],
    [2, " 2 - Modificar Productos ", "Modifica un Producto"],
    [3, " 3 - Eliminar Productos  ", "Elimina un Producto"],
    [4, " 4 - Buscar Productos    ", "Busca un Producto"],
    [5, " 5 - Listar Productos    ", "Lista todos los Productos"],
    [0, " ----------------------- ", ""],
    [9, " 9 - Salir               ", "Salir de la Aplicación"]
]


# Muestra la ayuda de los items del menu
def mostrar_ayuda_menu_productos(opcion_ingresada):
    print(f"\n Ayuda: {opcion_ingresada}\n")
    print(f"\n Ayuda: {opciones_menu_productos[int(opcion_ingresada)][2]}\n")


# Maneja y ejecuta las opciones del menu
def manejar_opciones_menu_productos(opcion_ingresada):
    if opcion_ingresada == '1':

        # Funcion de Agregar Productos
        agregar_productos()

    elif opcion_ingresada == '2':

        # 
        modificar_productos()

        
    elif opcion_ingresada == '3':

        # 
        eliminar_productos()

    elif opcion_ingresada == '4':

        # 
        buscar_productos()

    elif opcion_ingresada == '5':

        # Lista los productos del inventario
        listar_productos()

    else:

        # Muestra un mensaje en pantalla
        mostrar_mensaje("Opción inválida....")


# Muestra el menu de productos
def mostrar_menu_productos(opcion_ingresada):
    from inventory import mostrar_teclas_ayuda

    indice = 0 

    while (indice < len(opciones_menu_productos)):
        # Muestra en pantalla la opcion del menu
        if (opciones_menu_productos[indice][0] == int(opcion_ingresada)):

            print(f"> {opciones_menu_productos[indice][1]}")

        else: 

            print(f"  {opciones_menu_productos[indice][1]}")

        # Actualizacion del indice
        indice += 1

    #
    mostrar_teclas_ayuda()

    # Muestra la ayuda del menu
    mostrar_ayuda_menu_productos(opcion_ingresada)
