# Ejecucion de las opciones del menu

def process_option_menu(option):
    
    # Ejecuta las opciones del menu
    match option:
        case "Opción 1":
            print("Ejecutando la opción agregar productos...")
        case "Opción 2":
            print("Ejecutando la opción eliminar producto...")
        case "Opción 3":
            print("Ejecutando la opción mostrar inventario...")
        case "Opción 4":
            print("Ejecutando la opción buscar producto...")
        case "Opción 5":
            print("Opción no implementada...")
        case "Opción 6":
            print("Opción no implementada...")
        case "Opción 7":
            print("Opción no implementada...")
        case "Opción 8":
            print("Opción no implementada...")
        case "Salir":
            print("Saliendo del sistema...")
        case _:
            print("Opción no válida")
