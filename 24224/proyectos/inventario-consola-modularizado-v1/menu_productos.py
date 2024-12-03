# Muestra y maneja las opciones de los menus

from titulos import mostrar_titulo_productos
from mostrar_teclas_ayuda import mostrar_ayuda_teclas_submenus
from pantalla import limpiar_pantalla
from textos_opciones_menu import opciones_menu_productos
from productos import agregar_productos, modificar_productos, eliminar_productos, buscar_productos, listar_productos
from opcion_invalida import opcion_invalida

def mostrar_ayuda_productos(opcion_seleccionada):
    id, item, ayuda = opciones_menu_productos[opcion_seleccionada]
    print(f"\n Ayuda: {ayuda}\n")

def mostrar_menu_productos():
    opcion_ingresada = 0
    
    while True:
        # Limpia la pantalla
        limpiar_pantalla()

        # Muestra el titulo de productos
        mostrar_titulo_productos()

        for opcion in opciones_menu_productos:
            # Desempaqueta la tupla en variables
            id, item, ayuda = opcion
            print(f"{item}")

        mostrar_ayuda_teclas_submenus()

        mostrar_ayuda_productos(opcion_ingresada)
        
        opcion_ingresada = input("\n Seleccione una opción: ").lower()

        # Volver al menú anterior
        if ((opcion_ingresada == 'q') or (opcion_ingresada == '9')):
            
            break
        
        if ((opcion_ingresada == '')  or (opcion_ingresada >= '0') or (opcion_ingresada <= str(len(opciones_menu_productos) - 1))):
            
            #if (opcion_ingresada == ''):
            #    opcion_menu = str(opciones_menu[opcion_seleccionada][0])
            #else:
            #    opcion_menu = opcion_ingresada

            manejar_opciones_productos(opcion_ingresada)
        else:

            # Muestra el mensaje de opción invalida
            opcion_invalida()

def manejar_opciones_productos(opcion_seleccionada):
    if opcion_seleccionada == '1':

        # 
        agregar_productos()

    elif opcion_seleccionada == '2':

        # 
        modificar_productos()

    elif opcion_seleccionada == '3':

        # 
        eliminar_productos()

    elif opcion_seleccionada == '4':

        # 
        buscar_productos()

    elif opcion_seleccionada == '5':

        # 
        listar_productos()

    else:

        # Muestra el mensaje de opción invalida
        opcion_invalida()
