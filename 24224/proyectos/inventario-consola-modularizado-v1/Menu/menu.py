import os

# Opciones del menú
menu_options = [
    {'id': 1, 'item': 'Opción 1', 'ayuda': 'Ayuda para Opción 1'},
    {'id': 2, 'item': 'Opción 2', 'ayuda': 'Ayuda para Opción 2'},
    {'id': 3, 'item': 'Opción 3', 'ayuda': 'Ayuda para Opción 3'},
]

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar el menú y resaltar la opción seleccionada
def mostrar_menu(seleccion_actual):
    # limpiar_pantalla()
    print("====   Sistema de Inventario   ====\n")  # Línea en blanco añadida
    print("Use 'w' para subir, 's' para bajar y Enter para seleccionar.\n")
    for idx, option in enumerate(menu_options):
        indicador = ">" if idx == seleccion_actual else " "
        print(f"{indicador} {option['id']}. {option['item']}")
    print(f"\nAyuda: {menu_options[seleccion_actual]['ayuda']}")

# Función para manejar la opción seleccionada
def manejar_opcion(opcion_seleccionada):
    opcion = menu_options[opcion_seleccionada]
    print(f"\nOpción seleccionada: ID {opcion['id']} - {opcion['item']}")
    print(f"Ayuda: {opcion['ayuda']}")
    input("\nPresione Enter para volver al menú...")

# Función principal para manejar el menú
def main():
    seleccion_actual = 0

    while True:
        mostrar_menu(seleccion_actual)
        user_input = input("\nSeleccione una opción: ").lower()

        if user_input == 'w':  # Subir
            seleccion_actual = (seleccion_actual - 1) % len(menu_options)
        elif user_input == 's':  # Bajar
            seleccion_actual = (seleccion_actual + 1) % len(menu_options)
        elif user_input == '':  # Enter
            manejar_opcion(seleccion_actual)
        elif user_input == 'q':  # Salir
            print("Saliendo del menú...")
            break

if __name__ == "__main__":
    main()
