# Menu principal

from screen import clear_screen
from menu_navigate import navigate_menu

# Importar las opciones de menú
from menu_options_texts import texts_options_items

def main_menu():
    # Usa las opciones de menú desde el archivo de {% load textos_tags %} a futuro
    menu_options = texts_options_items

    while True:
        # Devuelve la opcion del menu seleccionada
        selected_option = navigate_menu(menu_options)
        
        # if selected_option[1] == "Salir":
        if selected_option[0] == 9 or selected_option[1] == "Salir":
            # Limpia la pantalla
            clear_screen()
        
            print(f"\n\n\nSeliendo de la aplicacion...")

            # Salir del menú
            break
