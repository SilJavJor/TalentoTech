# Importaciones
from screen import clear_screen
from title import show_title

# Función para mostrar el menú
def display_menu(options, current_index):
    # Limpiar la pantalla
    clear_screen()
    
    # Mostrar el título centrado
    show_title()
    
    for index, (id, option, help_text) in enumerate(options):
        prefix = "-> " if index == current_index else "   "
        print(f"{prefix}{id}. {option} - {help_text}")

# Función para manejar el menú
def inventory_menu():
    options = [
        (1, "Agregar producto", "Añade un nuevo producto al inventario."),
        (2, "Eliminar producto", "Elimina un producto del inventario."),
        (3, "Mostrar inventario", "Muestra todos los productos en el inventario."),
        (4, "Buscar producto", "Busca un producto específico en el inventario."),
        (5, "Salir", "Cierra el sistema.")
    ]
    
    # Índice de la opción actual
    current_index = 0

    while True:
        display_menu(options, current_index)

        # Obtener la entrada del usuario
        key = input("\nUsa las teclas 'w' y 's' para navegar y 'enter' para seleccionar: ").lower()

        if key == 'w' and current_index > 0:
            current_index -= 1  # Mover hacia arriba
        elif key == 's' and current_index < len(options) - 1:
            current_index += 1  # Mover hacia abajo
        elif key == '':  # Enter para seleccionar
            selected_option = options[current_index]
            print(f"\nSeleccionaste: {selected_option[1]}")
            if selected_option[1] == "Salir":
                break  # Salir del menú
            input("Presiona Enter para continuar...")
