# Opciones de nevegacion del menu

from screen import clear_screen
from title import show_title
from menu_display_options import display_options
from menu_get_user_input_option import get_user_input_option

def navigate_menu(options):
    # Índice de la opción actual
    current_index = 0

    while True:
        # Muestra las opciones del menu
        display_options(options, current_index)
        
        # Obtiene la tecla presionada        
        key = get_user_input_option()

        # Flecha arriba
        if key == 'up':
        
            # Mueve el cursor hacia arriba
            current_index = (current_index - 1) % len(options)
        
        # Flecha abajo
        elif key == 'down':
            
            # Mueve el cursor hacia abajo
            current_index = (current_index + 1) % len(options)
            
        # Enter para seleccionar
        elif key == 'enter':
            
            # Retornar la opcion del menu seleccionada
            return options[current_index]
        
        # Opción para salir
        elif key == '9':
            # Seleccionar salir manualmente
            return ('', 'Salir', '')
