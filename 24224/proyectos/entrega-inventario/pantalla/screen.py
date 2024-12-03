# Screen

# Importaciones
# Importa libreria del Sistema Operativo
import os
import time
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


"""
Muestra una frase en pantalla con un efecto de parpadeo.

frase (str): La frase o palabra que debe parpadear.
duracion (int): Duracion total del efecto en segundos.
intervalo (float): Tiempo en segundos entre cada parpadeo.
"""
def parpadear(frase, duracion = 5, intervalo = 0.5):
    #    
    tiempo_inicial = time.time()
    mostrar = True

    while ((time.time() - tiempo_inicial) < duracion):
        #limpiar_pantalla()
        if mostrar:
            #print(frase)
            print(f"{Style.BRIGHT}{Fore.YELLOW} \n\n {frase}", end="\r") 
        mostrar = not mostrar
        time.sleep(intervalo)

    # Mostrar la frase al final del parpadeo
    #limpiar_pantalla()
    #print(frase)


# Muestra un mensaje en pantalla
def mostrar_mensaje(mensaje, parpadea = True):
    mensaje_presione_cualquier_tecla = 'Presione cualquier tecla para continuar...'

    #
    if (mensaje != ''):
        #
        if (parpadea):
            #
            print(f"{blink} {Style.BRIGHT}{Fore.YELLOW}\n\n {mensaje} {reset}")

        else:
            #
            print(f"{Style.BRIGHT}{Fore.YELLOW}\n\n {mensaje}")

    #
    if (parpadea):
        # 
        input(f"{blink} {Style.BRIGHT}{Fore.YELLOW} \n\n {mensaje_presione_cualquier_tecla} {reset}")

    else:
        # 
        input(f"{Style.BRIGHT}{Fore.YELLOW} \n\n {mensaje_presione_cualquier_tecla}")
