# Muestra y maneja las opciones de los menus

from titulos import mostrar_titulo_productos
from mostrar_teclas_ayuda import mostrar_ayuda_teclas_submenus
from pantalla import limpiar_pantalla
from textos_opciones_menu import opciones_menu_productos
from productos import agregar_productos, listar_productos
from opcion_invalida import opcion_invalida

def mostrar_ayuda_productos(opcion_seleccionada):
    id, item, ayuda = opciones_menu_productos[opcion_seleccionada]
    print(f"\n Ayuda: {ayuda}\n")

def mostrar_menu(opcion_seleccionada):
    for idx, (id, item, ayuda) in enumerate(opciones_menu_productos):
        if idx == opcion_seleccionada:

            # Resalta la opción seleccionada
            print(f"> {item}")

        else:

            # 
            print(f"  {item}")

    mostrar_ayuda_teclas_submenus()


def manejar_opciones_productos(opcion_seleccionada):
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

def manejar_opciones_productos(opcion_seleccionada):
    
    # Menú de Clientes
    if opcion_seleccionada == 1:

        # 
        mostrar_menu_productos()

    # Menú de Productos
    elif opcion_seleccionada == 2:

        # 
        mostrar_menu_productos()

def mostrar_menu_productos():
    while True:
        # Limpia la pantalla
        limpiar_pantalla()

        # Muestra el titulo de productos
        mostrar_titulo_productos()

        for opcion in opciones_menu_productos:
            # Desempaqueta la tupla en variables
            id, item, ayuda = opcion
            print(f"{item}")

#        for option in opciones_menu_productos:
#            print(f"{option['id']}. {option['item']}")
#            print(f"\nAyuda: {menu_options_principal[0]['ayuda']}")  # Muestra ayuda del primer item

        mostrar_ayuda_teclas_submenus()

        opcion_ingresada = input("\n Seleccione una opción: ").lower()

        # Volver al menú anterior
        if ((opcion_ingresada == 'q') or (opcion_ingresada == '9')):
            
            break
        
        else:

            # Muestra el mensaje de opción invalida
            opcion_invalida()
