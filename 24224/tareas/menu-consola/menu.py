# menu.py

def menu():
    print("Menú Principal")
    print("--------------")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("-----------")
    print("0. Salir")

def run_menu(option1_func, option2_func, option3_func):
    while True:
        menu()
        
        selection = input("Selecciona una opción (1-4): ")
        
        if selection == '1':
            option1_func()
        elif selection == '2':
            option2_func()
        elif selection == '3':
            option3_func()
        elif selection == '0':
            print("", end="")
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")
