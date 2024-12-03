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
    print("Escriba el número de la opción que desea seleccionar o 'q' para salir.\n")

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

def main():
    seleccion_actual = 0  # Comenzar en la primera opción del menú

    while True:
        mostrar_menu(seleccion_actual)
        user_input = input("Seleccione una opción o use 'w' para subir, 's' para bajar: ")

        if user_input == 'w':  # Simula la tecla de flecha arriba
            seleccion_actual = (seleccion_actual - 1) % len(menu_options)
        elif user_input == 's':  # Simula la tecla de flecha abajo
            seleccion_actual = (seleccion_actual + 1) % len(menu_options)
        elif user_input.isdigit():
            opcion_id = int(user_input)
            if 1 <= opcion_id <= len(menu_options):
                manejar_opcion(opcion_id - 1)
        elif user_input.lower() == 'q':
            print("Saliendo del menú...")
            break

if __name__ == "__main__":
    main()
