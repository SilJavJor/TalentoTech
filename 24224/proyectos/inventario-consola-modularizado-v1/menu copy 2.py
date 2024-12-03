import keyboard
import time

# Definición de opciones del menú
menu_options = [
    {'id': 1, 'item': 'Opción 1', 'ayuda': 'Ayuda para Opción 1'},
    {'id': 2, 'item': 'Opción 2', 'ayuda': 'Ayuda para Opción 2'},
    {'id': 3, 'item': 'Opción 3', 'ayuda': 'Ayuda para Opción 3'},
]

# Función para mostrar el menú con la opción seleccionada resaltada
def mostrar_menu(seleccion_actual):
    print("\nUse las teclas de flecha arriba/abajo para moverse. Presione Enter para seleccionar.")
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
        # Navegar por el menú usando las teclas de flecha
        if keyboard.is_pressed('down'):
            seleccion_actual = (seleccion_actual + 1) % len(menu_options)  # Baja una opción
            mostrar_menu(seleccion_actual)
            time.sleep(0.2)  # Pequeña pausa para evitar desplazamiento rápido
        elif keyboard.is_pressed('up'):
            seleccion_actual = (seleccion_actual - 1) % len(menu_options)  # Sube una opción
            mostrar_menu(seleccion_actual)
            time.sleep(0.2)
        elif keyboard.is_pressed('enter'):
            print(f"\nOpción seleccionada: {menu_options[seleccion_actual]['item']}")
            print(f"Ayuda: {menu_options[seleccion_actual]['ayuda']}")
            break  # Sale del bucle al seleccionar una opción
        elif keyboard.is_pressed('q'):
            print("Saliendo del menú...")
            break

if __name__ == "__main__":
    main()
