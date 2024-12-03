import os

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
    print("Use las teclas de flecha arriba/abajo para moverse. Presione Enter para seleccionar o 'q' para salir.\n")

    # Mostrar opciones del menú con la selección actual resaltada
    for idx, option in enumerate(menu_options):
        indicador = ">" if idx == seleccion_actual else " "
        print(f"{indicador} {option['id']}. {option['item']}")
    print(f"\nAyuda: {menu_options[seleccion_actual]['ayuda']}")  # Muestra ayuda de la opción actual

def manejar_opcion(opcion_seleccionada):
    """Maneja la lógica de lo que sucede al seleccionar una opción del menú."""
    opcion = menu_options[opcion_seleccionada]
    print(f"\nOpción seleccionada: ID {opcion['id']} - {opcion['item']}")
    print(f"Ayuda: {opcion['ayuda']}")
    input("\nPresione Enter para volver al menú...")  # Espera a que el usuario presione Enter

def obtener_input():
    """Lee el input y detecta flechas."""
    print("Seleccione una opción usando flechas y presione Enter: ")
    key = input()  # Captura la entrada de teclado

    if key == '\x1b[A':  # Código de escape para flecha arriba
        return 'UP'
    elif key == '\x1b[B':  # Código de escape para flecha abajo
        return 'DOWN'
    elif key == '\r':  # Enter
        return 'ENTER'
    elif key.lower() == 'q':  # Salir
        return 'q'
    else:
        return key  # Devolver cualquier otro input para seleccion directa de opción

def main():
    seleccion_actual = 0  # Comenzar en la primera opción del menú

    while True:
        mostrar_menu(seleccion_actual)
        user_input = obtener_input()

        if user_input == 'UP':  # Flecha arriba
            seleccion_actual = (seleccion_actual - 1) % len(menu_options)
        elif user_input == 'DOWN':  # Flecha abajo
            seleccion_actual = (seleccion_actual + 1) % len(menu_options)
        elif user_input == 'ENTER':
            manejar_opcion(seleccion_actual)  # Manejar la opción seleccionada
        elif user_input.isdigit():
            opcion_id = int(user_input)
            if 1 <= opcion_id <= len(menu_options):
                manejar_opcion(opcion_id - 1)
        elif user_input == 'q':
            print("Saliendo del menú...")
            break

if __name__ == "__main__":
    main()
