import os
import shutil
import sys

def clear_screen():
    """Limpia la pantalla del terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    """Muestra el menú centrado en la pantalla."""
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns
    menu_text = """
Menú Principal
1. Opción 1
2. Opción 2
3. Opción 3
4. Salir
    """
    lines = menu_text.split('\n')
    centered_lines = [line.center(width) for line in lines]
    print('\n'.join(centered_lines))

def run_menu(option1_func, option2_func, option3_func):
    """Ejecuta el menú y maneja la selección del usuario."""
    while True:
        clear_screen()
        
        menu()
        
        selection = input("Selecciona una opción (1-4): ")
        
        if selection == '1':
            option1_func()
        elif selection == '2':
            option2_func()
        elif selection == '3':
            option3_func()
        elif selection == '0':
            print("Saliendo...")
            sys.exit
            break
        else:
            print("Opción no válida. Intenta nuevamente.")
