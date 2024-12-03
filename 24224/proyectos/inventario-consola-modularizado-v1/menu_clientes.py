# Muestra y maneja las opciones de los menu de Clientes

from mostrar_teclas_ayuda import mostrar_ayuda_teclas_submenus
from pantalla import limpiar_pantalla
from titulos import mostrar_titulo_clientes, mostrar_titulo_productos
from textos_opciones_menu import opciones_menu, opciones_menu_clientes, opciones_menu_productos

def mostrar_ayuda_clientes(opcion_seleccionada):
    id, item, ayuda = opciones_menu_clientes[opcion_seleccionada]
    print(f"\n Ayuda: {ayuda}\n")

#def mostrar_menu_clientes(opcion_seleccionada):
def mostrar_menu_clientes():
    while True:
        # Limpia la pantalla
        limpiar_pantalla()

        # Muestra el titulo del menu de Clientes
        mostrar_titulo_clientes()

#        for idx, (id, item, ayuda) in enumerate(opciones_menu_clientes):
#            if idx == opcion_seleccionada:

                # Resalta la opción seleccionada
#               print(f"> {item}")

#            else:

                # 
#                print(f"  {item}")

        #mostrar_ayuda_teclas_submenus()
        
        #user_input = input("\n Seleccione una opción: ").lower()

        # Muestra la ayuda
        #mostrar_ayuda_clientes(opcion_seleccionada)

        # Captura la tecla ingresada
        opcion_ingresada = input("\n Seleccione una opción: ").lower()

        # Volver al menú principal
        #if user_input == '9':
        if opcion_ingresada == '9':
            break

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

        user_input = input("\n Seleccione una opción: ").lower()
        
        if user_input == '9':  # Volver al menú principal
            break
        # Aquí podrías agregar las funcionalidades correspondientes a cada opción.
        # Por ejemplo, llamar a agregar_producto(), modificar_producto(), etc.

def manejar_opciones_clientes(opcion_seleccionada):
    
    # Menú de Clientes
    if opcion_seleccionada == 1:

        # Muestra el menu de Clientes
        mostrar_menu_clientes()

    # Menú de Productos
    elif opcion_seleccionada == 2:

        # Muestra el menu de Productos
        mostrar_menu_clientes()

#def mostrar_menu_clientes():
#    while True:
        # Limpia la pantalla
#        limpiar_pantalla()
        
        # Muestra el titulo del menu de Clientes
#        mostrar_titulo_clientes()

#        for opcion in opciones_menu_clientes:
            # Desempaqueta la tupla en variables
#            id, item, ayuda = opcion
#            print(f"{item}")

#        mostrar_ayuda_tecla_submenus()
        
#        user_input = input("\n Seleccione una opción: ").lower()

        # Volver al menú principal
#        if user_input == '9':
#            break

#def mostrar_menu_productos():
#    while True:
        # Limpia la pantalla
#        limpiar_pantalla()

        # Muestra el titulo de productos
#        mostrar_titulo_productos()

#        for opcion in opciones_menu_productos:
#            # Desempaqueta la tupla en variables
#            id, item, ayuda = opcion
#            print(f"{item}")

#        for option in opciones_menu_productos:
#            print(f"{option['id']}. {option['item']}")
#            print(f"\nAyuda: {menu_options_principal[0]['ayuda']}")  # Muestra ayuda del primer item

#        mostrar_ayuda_tecla_submenus()

#        user_input = input("\n Seleccione una opción: ").lower()
        
#        if user_input == '9':  # Volver al menú principal
#            break
        # Aquí podrías agregar las funcionalidades correspondientes a cada opción.
        # Por ejemplo, llamar a agregar_producto(), modificar_producto(), etc.
