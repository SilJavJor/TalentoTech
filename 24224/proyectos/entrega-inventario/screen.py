# Screen

# Importaciones
# Importa libreria del Sistema Operativo
import os

# Limpia de la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


# Muestra un mensaje en pantalla
def mostrar_mensaje(mensaje):
    #
    if (mensaje != ''):
        print(f"\n\n {mensaje}")

    # 
    input("\n Presione cualquier tecla para continuar...")