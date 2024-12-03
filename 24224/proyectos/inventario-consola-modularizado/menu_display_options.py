# Muestra las opciones del menu

from screen import clear_screen
from title import show_title

# Muestra las 
def display_options(options, current_index):
    # Limpia la pantalla
    clear_screen()

    # Muestra el titulo
    show_title()

    # 
    for index, (id, option, help_text) in enumerate(options):
        # Muestra un signo indicador del cursor, en que renglon se encuentra el cursor
        prefix = "-> " if index == current_index else "   "
        
        # Muestra unicamente el item
        print(f"{prefix}{option}")

    # Informacion de teclas 
    print("\nUsa las teclas ↑ (arriba), ↓ (abajo) para navegar.")
    print("Presione 'Enter o el numero informado' para seleccionar, o '9' para salir.")

    # Mostrar la ayuda debajo del menú
    print("\n\nAyuda : ", options[current_index][2])

    print("Seleccione una opción: ")
