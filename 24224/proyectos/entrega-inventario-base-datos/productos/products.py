# Productos

# Importaciones
# Importa desde Colorama
from colorama import Style, Fore
# Importa desde Pantalla
from pantalla import mostrar_linea_separacion, mostrar_mensaje


# Titulo de Listados de Productos
def imprime_titulos_listados_completos():
    # Encabezados del listado de productos
    print(f"{Style.BRIGHT} {Fore.GREEN} {'ID':<5} {'Nombre':<30} {'Descripción':<30} {'Cantidad':>10} {'Precio':>15} {'Categoría':<30}")
    print("=" * 115)


# Imprime un producto horizontalmente
def imprime_un_producto_forma_horizontal(producto):
    # 0 = id, 1 = nombre, 2 = descripcion, 3 = cantidad, 4 = precio, 5 = categoria
    print(f"{producto[0]:>5} {producto[1]:<30} {producto[2]:<30} {producto[3]:>12} {producto[4]:>15f} {producto[5]:<25}")


# Imprime un producto verticalmente
def imprime_un_producto_forma_vertical(producto):
    # 0 = id, 1 = nombre, 2 = descripcion, 3 = cantidad, 4 = precio, 5 = categoria
    print(f" \n Producto seleccionado : ")
    print(f"\n - Identificador : {producto[0]:<5}")
    print(f" - Nombre : {producto[1]:<30}")
    print(f" - Descripcion : {producto[2]:<50}")
    print(f" - Cantidad : {producto[3]:>10}")
    print(f" - Precio : {producto[4]:>10.4f}")
    print(f" - Categoria : {producto[5]:<30}")


# Controla y ejecuta las opciones del menu
def seleccionar_opciones_menu_productos(opcion_ingresada):
    # Importa desde Productos
    from productos import ( agregar_productos, mostrar_productos, modificar_productos, eliminar_productos, 
                            mostrar_producto, reporte_bajo_stock )

    if opcion_ingresada == '1':
        # Funcion Agregar Productos
        agregar_productos()

    elif opcion_ingresada == '2':
        # Muestra los productos del inventario
        mostrar_productos()

    elif opcion_ingresada == '3':
        # Funcion Modificar Productos
        modificar_productos()

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
