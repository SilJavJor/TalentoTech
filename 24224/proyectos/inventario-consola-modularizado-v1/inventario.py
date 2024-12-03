# Inventario 

from pantalla import limpiar_pantalla
from menu import mostrar_menu, mostrar_ayuda, manejar_opciones_menu
from opcion_invalida import opcion_invalida
from textos_opciones_menu import opciones_menu
from salida import salida_aplicacion

# Función principal para manejar el menú
def inventario():
    # Inicializa la opcion_seleccionada
    opcion_seleccionada = 0

    while True:
        # Limpiar la pantalla
        limpiar_pantalla()

        # Muestra el menu principal
        mostrar_menu(opcion_seleccionada)

        # Muestra la ayuda
        mostrar_ayuda(opcion_seleccionada)

        # Captura la tecla ingresada
        opcion_ingresada = input("\n Seleccione una opción: ").lower()

        if (opcion_ingresada == 'q') or (opcion_ingresada == '9'):

            # Sale de la aplicacion
            salida_aplicacion()

            break

        if ((opcion_ingresada == 'w') and (opcion_seleccionada == 0)):

            # Subir
            opcion_seleccionada = len(opciones_menu) - 1

        elif ((opcion_ingresada == 'w') and (opcion_seleccionada > 0)):

            # Subir
            opcion_seleccionada -= 1

        elif ((opcion_ingresada == 's') and (opcion_seleccionada == (len(opciones_menu) - 1))):

            # Bajar
            opcion_seleccionada = 0

        elif ((opcion_ingresada == 's') and (opcion_seleccionada < (len(opciones_menu) - 1))):  # Bajar

            # Bajar
            opcion_seleccionada += 1

        elif ((opcion_ingresada == '')  or (opcion_ingresada >= '0') or (opcion_ingresada <= str(len(opciones_menu) - 1))):
            
            if (opcion_ingresada == ''):
                opcion_menu = str(opciones_menu[opcion_seleccionada][0])
            else:
                opcion_menu = opcion_ingresada

            manejar_opciones_menu(opcion_menu)

        else:

            # Muestra el mensaje de opción invalida
            opcion_invalida()