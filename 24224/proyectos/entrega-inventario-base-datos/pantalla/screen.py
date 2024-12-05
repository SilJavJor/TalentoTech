# Screen

# Importaciones
# Importa libreria S.O.
import os
# Importa libreria Time
#import time
# Importa libreria Sys
import sys
# Importa libreria Colorama
from colorama import Style, Fore


# Secuencia ANSI para parpadeo
blink = '\033[5m'
reset = '\033[0m'


# Limpia de la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


# Mustra una linea de separacion
def mostrar_linea_separacion():
    print(f"{Style.BRIGHT}{Fore.CYAN}   ------------------------------------------   \n")


# Muestra un mensaje de presione una tecla para continuar
def mostrar_mensaje_presione_cualquier_tecla(parpadea_mensaje = False):
    mensaje_presione_cualquier_tecla = 'Presione cualquier tecla para continuar...'

    #
    if (parpadea_mensaje):
        # 
        input(f"{blink} {Style.BRIGHT}{Fore.YELLOW} \n\n {mensaje_presione_cualquier_tecla} {reset}")

    else:
        # 
        input(f"{Style.BRIGHT}{Fore.YELLOW} \n\n {mensaje_presione_cualquier_tecla}")


# Muestra un mensaje en pantalla
def mostrar_mensaje(mensaje, parpadea_mensaje = True, muestra_mensaje_presione_cualquier_tecla = True):
    #
    if (mensaje != ''):
        #
        if (parpadea_mensaje):
            #
            print(f"{blink} {Style.BRIGHT}{Fore.YELLOW}\n\n {mensaje} {reset}")

        else:
            #
            print(f"{Style.BRIGHT}{Fore.YELLOW}\n\n {mensaje}")

    #
    if (muestra_mensaje_presione_cualquier_tecla):
        mostrar_mensaje_presione_cualquier_tecla()


# Regresa n cantidad de lineas hacia atras en la pantalla
def lineas_regresar(lineas_regresar = 1):
# Mueve el cursor hacia arriba
    for _ in range(lineas_regresar):
        # Mueve el cursor una línea hacia arriba
        sys.stdout.write("\033[F")
