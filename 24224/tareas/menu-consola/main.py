# main.py

from menu import menu
from functions import opcion1, opcion2, opcion3 

def main():
    while True:
        menu()

        seleccion = input("Selecciona una opción (1-4): ")
        
        if seleccion == '1':
            opcion1()
        elif seleccion == '2':
            opcion2()
        elif seleccion == '3':
            opcion3()
        elif seleccion == '0':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
