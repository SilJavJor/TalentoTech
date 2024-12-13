# Productos

# Importaciones
# Importa desde Colorama
from colorama import Style, Fore
# Importa desde Pantalla
from pantalla import mostrar_mensaje


# Controla y ejecuta las opciones del menu
def seleccionar_opciones_menu_productos(opcion_ingresada):
    # Importa desde Productos
    from productos import ( agregar_productos, mostrar_productos, modificar_cantidad, eliminar_productos, 
                            mostrar_producto, reporte_bajo_stock )

    if opcion_ingresada == '1':
        # Funcion Agregar Productos
        agregar_productos()

    elif opcion_ingresada == '2':
        # Muestra los productos del inventario
        mostrar_productos()

    elif opcion_ingresada == '3':
        # Funcion Modificar Productos
        modificar_cantidad()

    elif opcion_ingresada == '4':
        # Funcion Eliminaar Productos
        eliminar_productos()

    elif opcion_ingresada == '5':
        # Funcion Buscar Productos
        mostrar_producto()

    elif opcion_ingresada == '6':
        # Funcion Modificar Productos
        reporte_bajo_stock()

    else:
        # Muestra un mensaje en pantalla
        mostrar_mensaje("Opción inválida....")

        #
        opcion_ingresada = 1

    return opcion_ingresada
