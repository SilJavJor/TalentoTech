# Muestra y maneja las opciones de los menus




#from sistema import menu_options, ayuda_menu

#def mostrar_menu(seleccion_actual):
#    print("Use 'w' para subir, 's' para bajar y Enter para seleccionar.\n")
#    for idx, option in enumerate(menu_options):
#        indicador = ">" if idx == seleccion_actual else " "
#        print(f"{indicador} {option['id']}. {option['item']}")
#    print(f"\nAyuda: {ayuda_menu[seleccion_actual]}")

#def manejar_opcion(opcion_seleccionada):
#    if opcion_seleccionada == 0:  # Agregar Producto
#        agregar_producto()
#    elif opcion_seleccionada == 1:  # Ver Productos
#        ver_productos()
#    elif opcion_seleccionada == 2:  # Salir
#        print("Saliendo del menú...")
#        exit()

#from menu import mostrar_menu, manejar_opcion_principal


from mostrar_teclas_ayuda import mostrar_ayuda_tecla_menu, mostrar_ayuda_tecla_submenus
from pantalla import limpiar_pantalla
from titulos import mostrar_titulo_clientes, mostrar_titulo_productos
from textos_opciones_menu import opciones_menu, opciones_menu_clientes, opciones_menu_productos

#    print("Use 'w' para subir, 's' para bajar y Enter para seleccionar.\n")

def mostrar_ayuda(opcion_seleccionada):
    id, item, ayuda = opciones_menu[opcion_seleccionada]
    print(f"\n Ayuda: {ayuda}\n")

def mostrar_menu(opcion_seleccionada):
#    for option in opciones_menu:
#        print(f"{option['id']}. {option['item']}")

#    for opcion in opciones_menu:
#        # Desempaqueta la tupla en variables
#        id, item, ayuda = opcion
#        print(f"{item}")
        #mostrar_ayuda(option['ayuda'])

    for idx, (id, item, ayuda) in enumerate(opciones_menu):
        if idx == opcion_seleccionada:

            # Resalta la opción seleccionada
            print(f"> {item}")

        else:

            # 
            print(f"  {item}")

    mostrar_ayuda_tecla_menu()

def manejar_opcion(opcion_seleccionada):
    
    # Menú de Clientes
    if opcion_seleccionada == 1:

        # Muestra el menu de Clientes
        mostrar_menu_clientes()

    # Menú de Productos
    elif opcion_seleccionada == 2:

        # Muestra el menu de Productos
        mostrar_menu_productos()

def mostrar_menu_clientes():
    while True:
        # Limpia la pantalla
        limpiar_pantalla()
        
        # Muestra el menu de Clientes
        mostrar_titulo_clientes()

        for opcion in opciones_menu_clientes:
            # Desempaqueta la tupla en variables
            id, item, ayuda = opcion
            print(f"{item}")

#        for option in opciones_menu_clientes:
#            print(f"{option['id']}. {option['item']}")
            
#            print(f"\nAyuda: {menu_options_principal[0]['ayuda']}")  # Muestra ayuda del primer item

        #print("Use '0' para Clientes, '1' para Productos y '9' para Salir.\n")
        mostrar_ayuda_tecla_submenus()
        
        user_input = input("\nSeleccione una opción: ").lower()
        
        if user_input == '9':  # Volver al menú principal
            break
        # Aquí podrías agregar las funcionalidades correspondientes a cada opción.
        # Por ejemplo, llamar a agregar_cliente(), modificar_cliente(), etc.

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

        mostrar_ayuda_tecla_submenus()

        user_input = input("\nSeleccione una opción: ").lower()
        
        if user_input == '9':  # Volver al menú principal
            break
        # Aquí podrías agregar las funcionalidades correspondientes a cada opción.
        # Por ejemplo, llamar a agregar_producto(), modificar_producto(), etc.
