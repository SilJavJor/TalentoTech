# Limpia la pantalla

# Para obtener el S. O.
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
