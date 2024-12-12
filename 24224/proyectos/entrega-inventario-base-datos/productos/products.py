# Productos

# Importaciones
# Importa desde Colorama
from colorama import Style, Fore
# Importa desde Pantalla
from pantalla import mostrar_mensaje


# Titulo de Listados de Productos
def imprime_titulos_listados_completos():
    # Encabezados del listado de productos
    print(f"{Style.BRIGHT} {Fore.GREEN} {'ID':<5} {'Nombre':<20} {'Descripción':<20} {'Cantidad':>12} {'Precio':>15} {'Categoría':<20}")
    print("=" * 115)


# Imprime un producto horizontalmente
def imprime_un_producto_forma_horizontal(producto):
    # 0 = id, 1 = nombre, 2 = descripcion, 3 = cantidad, 4 = precio, 5 = categoria
    print(f"{producto[0]:<5} {producto[1]:<20} {producto[2]:<20} {producto[3]:>12} {producto[4]:>15f} {producto[5]:<20}")


# Imprime un producto verticalmente
def imprime_un_producto_forma_vertical(producto):
    # 0 = id, 1 = nombre, 2 = descripcion, 3 = cantidad, 4 = precio, 5 = categoria
    print(f" \n{Style.BRIGHT} {Fore.GREEN} Producto seleccionado : ")
    print(f"\n{Style.BRIGHT} {Fore.YELLOW} - Identificador : {Style.BRIGHT} {Fore.LIGHTWHITE_EX}{producto[0]:<5}")
    print(f"{Style.BRIGHT} {Fore.YELLOW} - Nombre : {Style.BRIGHT} {Fore.LIGHTWHITE_EX}{producto[1]:<30}")
    print(f"{Style.BRIGHT} {Fore.YELLOW} - Descripcion : {Style.BRIGHT} {Fore.LIGHTWHITE_EX}{producto[2]:<50}")
    print(f"{Style.BRIGHT} {Fore.YELLOW} - Cantidad : {Style.BRIGHT} {Fore.LIGHTWHITE_EX}{producto[3]:>10}")
    print(f"{Style.BRIGHT} {Fore.YELLOW} - Precio : {Style.BRIGHT} {Fore.LIGHTWHITE_EX}{producto[4]:>10.4f}")
    print(f"{Style.BRIGHT} {Fore.YELLOW} - Categoria : {Style.BRIGHT} {Fore.LIGHTWHITE_EX}{producto[5]:<30}")


# Controla y ejecuta las opciones del menu
def seleccionar_opciones_menu_productos(opcion_ingresada):
    # Importa desde Productos
    from productos import ( agregar_productos, mostrar_productos, modificar_cantidad, eliminar_productos, 
                            mostrar_producto, reporte_bajo_stock )

    if opcion_ingresada == '1':
        # Funcion Agregar Productos
        agregar_productos()

    elif opcion_ingresada == '2':
        # Muestra los productos del inventario
        mostrar_productos()

    elif opcion_ingresada == '3':
        # Funcion Modificar Productos
        modificar_cantidad()

    elif opcion_ingresada == '4':
        # Funcion Eliminaar Productos
        eliminar_productos()

    elif opcion_ingresada == '5':
        # Funcion Buscar Productos
        mostrar_producto()

    elif opcion_ingresada == '6':
        # Funcion Modificar Productos
        reporte_bajo_stock()

    else:
        # Muestra un mensaje en pantalla
        mostrar_mensaje("Opción inválida....")

        #
        opcion_ingresada = 1

    return opcion_ingresada
