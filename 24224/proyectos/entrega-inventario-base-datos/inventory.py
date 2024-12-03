# Aplicaion de invetario

# Importaciones
# Importacion de Colorama
from colorama import Style, Fore
# Importa desde Screen funciones independientes para el manejo de la pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje, mostrar_linea_separacion
# Importa desde Productos el menu y su manejo
from productos import  mostrar_menu_productos, seleccionar_opciones_menu_productos


# Variable que se utiliza para la carga del inventario
inventario_productos = []


# Muestra el titulo de la aplicacion
def mostrar_titulo_aplicacion():
    mostrar_linea_separacion()
    print(f"{Style.BRIGHT}{Fore.CYAN}             Sistema de Inventario              \n")
    mostrar_linea_separacion()


# Salida de la aplicación
def salida_aplicacion():
    # Muestra un mensaje en pantalla
    mostrar_mensaje("Saliendo de la aplicación...")

    # Limpia la Pantalla
    limpiar_pantalla()


# Mostrar la ayuda de la opcion del menu
def mostrar_teclas_ayuda():
    print("\n\n Presione el número correspondiente para seleccionar.")
    print(" Presione '9' para Salir.")


# 
def inventario():
    #
    from productos import opciones_menu_productos
    
    # Variable que se utiliza para el ingreso de la opcion del menu
    opcion_ingresada = '1'

    while True:
        # Limpia la pantalla
        limpiar_pantalla()

        # Muestra el titulo de la aplicación
        mostrar_titulo_aplicacion()

        # Muestra el menu en pantalla
        mostrar_menu_productos(opcion_ingresada)

        # Caputura el ingreso del teclado
        opcion_ingresada = input("\n Seleccione una opción: ").lower()

        if (opcion_ingresada == '9'):

            # Salir de la aplicacion
            salida_aplicacion()

            break

        elif ((opcion_ingresada > '0') and (opcion_ingresada < str(len(opciones_menu_productos)))):

            # Accede a las funciones de Carga, Modificacion, Eliminacion, Busqueda 
            # y Listados de Productos
            opcion_ingresada = seleccionar_opciones_menu_productos(opcion_ingresada)

        else:

            # Muestra un mensaje en pantalla
            mostrar_mensaje("Opción inválida...")
            opcion_ingresada = 1
