import readchar
import os
import time

# Definición de opciones del menú
menu_options = [
    {'id': 1, 'item': 'Opción 1', 'ayuda': 'Ayuda para Opción 1'},
    {'id': 2, 'item': 'Opción 2', 'ayuda': 'Ayuda para Opción 2'},
    {'id': 3, 'item': 'Opción 3', 'ayuda': 'Ayuda para Opción 3'},
]

# Función para limpiar la pantalla según el sistema operativo
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar el menú con el título y la opción seleccionada
def mostrar_menu(seleccion_actual):
    limpiar_pantalla()  # Limpia la pantalla antes de mostrar el menú
    # Título del menú
    print("====   Sistema de Inventario   ====")
    print("Use las teclas de flecha arriba/abajo para moverse. Presione Enter para seleccionar.\n")

    # Mostrar opciones del menú con la selección actual resaltada
    for idx, option in enumerate(menu_options):
        if idx == seleccion_actual:
            print(f"> {option['id']}. {option['item']}")  # Resalta la opción actual
        else:
            print(f"  {option['id']}. {option['item']}")
    print(f"\nAyuda: {menu_options[seleccion_actual]['ayuda']}")  # Muestra ayuda de la opción actual

def main():
    seleccion_actual = 0  # Comenzar en la primera opción del menú
    mostrar_menu(seleccion_actual)

    while True:
        key = readchar.readkey()

        if key == readchar.key.UP:
            seleccion_actual = (seleccion_actual - 1) % len(menu_options)
            mostrar_menu(seleccion_actual)
        elif key == readchar.key.DOWN:
            seleccion_actual = (seleccion_actual + 1) % len(menu_options)
            mostrar_menu(seleccion_actual)
        elif key == readchar.key.ENTER:
            print(f"\nOpción seleccionada: {menu_options[seleccion_actual]['item']}")
            print(f"Ayuda: {menu_options[seleccion_actual]['ayuda']}")
            break
        elif key == 'q':
            print("Saliendo del menú...")
            break
        time.sleep(0.1)  # Pequeña pausa para evitar múltiples entradas rápidas

if __name__ == "__main__":
    main()
