import time

# Definición de opciones del menú
menu_options = [
    {'id': 1, 'item': 'Opción 1', 'ayuda': 'Ayuda para Opción 1'},
    {'id': 2, 'item': 'Opción 2', 'ayuda': 'Ayuda para Opción 2'},
    {'id': 3, 'item': 'Opción 3', 'ayuda': 'Ayuda para Opción 3'},
]

def mostrar_menu():
    print("\nSeleccione una opción:")
    for option in menu_options:
        print(f"{option['id']}. {option['item']}")

def mostrar_ayuda(opcion):
    ayuda = opcion['ayuda']
    print(f"\nAyuda: {ayuda}")

def main():
    seleccion = None

    while seleccion != 'q':
        mostrar_menu()  # Mostrar menú en cada ciclo
        seleccion = input("\nIngrese el número de la opción (o 'q' para salir): ")

        if seleccion.isdigit():
            seleccion = int(seleccion)
            opcion = next((item for item in menu_options if item['id'] == seleccion), None)

            if opcion:
                print(f"\nOpción seleccionada: {opcion['item']}")
                mostrar_ayuda(opcion)
                time.sleep(2)  # Pausa antes de volver al menú
            else:
                print("Opción no válida. Intente de nuevo.")
        elif seleccion.lower() == 'q':
            print("Saliendo del menú...")
            time.sleep(1)
        else:
            print("Entrada no válida. Use un número o 'q' para salir.")

if __name__ == "__main__":
    main()
