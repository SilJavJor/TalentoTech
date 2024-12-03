#

#from menu_navigate import navigate_menu

#def menu():
#    options = [
#        (1, "Agregar producto", "A�ade un nuevo producto al inventario."),
#        (2, "Eliminar producto", "Elimina un producto del inventario."),
#        (3, "Mostrar inventario", "Muestra todos los productos en el inventario."),
#        (4, "Buscar producto", "Busca un producto espec�fico en el inventario."),
#        (5, "Salir", "Cierra el sistema.")
#    ]

#    while True:
#        selected_option = navigate_menu(options)
#        print(f"\nSeleccionaste: {selected_option[1]}")
        
#        if selected_option[1] == "Salir":
#            break  # Salir del men�
        
#        input("Presiona Enter para continuar...")

from menu_navigate import navigate_menu
#from menu_options import options_menu  # Importar las opciones de men�

def inventory_menu():
#    options = menu_options  # Usar las opciones de men� desde el archivo de textos
    options = [
        (1, " 1 - Agregar producto    ", "Añade un nuevo producto al inventario."),
        (2, " 2 - Eliminar producto   ", "Elimina un producto del inventario."),
        (3, " 3 - Modifica producto   ", "Modifica un producto del inventario."),
        (4, " 4 - Buscar producto     ", "Busca un producto específico en el inventario."),
        (5, " 5 - Mostrar inventario  ", "Muestra todos los productos en el inventario."),
        (9, " 9 - Salir               ", "Cierra el sistema.")
        (0, "                         ", ""),
        (0, "-------------------------", ""),
        (0, "                         ", ""),
        (0, "Seleccione una opcion :  ", "Selecciona una oocion del menu."),
        (0, "                         ", ""),
    ]
    
    while True:
        selected_option = navigate_menu(options)
        print(f"\nSeleccionaste: {selected_option[1]}")
        
        if selected_option[1] == "Salir":
            break  # Salir del men�
        
        input("Presiona Enter para continuar...")
