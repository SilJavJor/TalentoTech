#

import os

# from utils import clear_screen, show_title, display_options, get_user_input

from screen import clear_screen
from title import show_title
from display_options import display_options
from get_user_input import get_user_input

def navigate_menu(options):
    current_index = 0  # Índice de la opción actual

    while True:
        show_title()
        display_options(options, current_index)

        key = get_user_input()

        if key == 'w' and current_index > 0:
            current_index -= 1  # Mover hacia arriba
        elif key == 's' and current_index < len(options) - 1:
            current_index += 1  # Mover hacia abajo
        elif key == '':  # Enter para seleccionar
            return options[current_index]  # Devolver la opción seleccionada

def navigate_menu(options):
    current_index = 0  # Índice de la opción actual

    while True:
        show_title()
        display_options(options, current_index)

        key = get_user_input()

        if key == 'w' and current_index > 0:
            current_index -= 1  # Mover hacia arriba
        elif key == 's' and current_index < len(options) - 1:
            current_index += 1  # Mover hacia abajo
        elif key == '':  # Enter para seleccionar
            return options[current_index]  # Devolver la opción seleccionada