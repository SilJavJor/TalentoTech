# Muestra y maneja las opciones de los menus

from titulos import mostrar_titulo
from mostrar_teclas_ayuda import mostrar_ayuda_teclas_menu
from textos_opciones_menu import opciones_menu
from menu_clientes import mostrar_menu_clientes
from menu_productos import mostrar_menu_productos
from opcion_invalida import opcion_invalida

def mostrar_ayuda(opcion_seleccionada):
    id, item, ayuda = opciones_menu[opcion_seleccionada]
    print(f"\n Ayuda: {ayuda}\n")

def mostrar_menu(opcion_seleccionada):
    # Muestra el titulo de la aplicación
    mostrar_titulo()
    
    for idx, (id, item, ayuda) in enumerate(opciones_menu):
        if idx == opcion_seleccionada:

            # Resalta la opción seleccionada
            print(f"> {item}")

        else:

            # 
            print(f"  {item}")

    mostrar_ayuda_teclas_menu()

def manejar_opciones_menu(opcion_seleccionada):
    # Menú de Clientes
    if opcion_seleccionada == '1':

        # Muestra el menu de Clientes
        mostrar_menu_clientes()

    # Menú de Productos
    elif opcion_seleccionada == '2':

        # Muestra el menu de Productos
        mostrar_menu_productos()

    else:

        # Muestra el mensaje de opción invalida
        opcion_invalida()
