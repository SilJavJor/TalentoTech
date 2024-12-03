#  Limpia la pantalla segun el S.O.

import os

# Limpiar la pantalla
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
