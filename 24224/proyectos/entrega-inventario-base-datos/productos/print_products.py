# Impresion de Productos
# Importaciones
# Importa Colorama
from colorama import Style, Fore


# Titulo de Listados de Productos
def imprime_titulos_listados_completos():
    # Encabezados del listado de productos
    print(f"\n{Style.BRIGHT} {Fore.GREEN} {'ID':<5} {'Nombre':<15} {'Descripción':<20} {'Cantidad':>12} {'Precio':>15} {'Categoría':<20}")
    print("=" * 120)


# Imprime un producto horizontalmente
def imprime_un_producto_forma_horizontal(producto):
    # 0 = id, 1 = nombre, 2 = descripcion, 3 = cantidad, 4 = precio, 5 = categoria
    print(f"{producto[0]:<5} {producto[1]:<20} {producto[2]:<15} {producto[3]:>12} {producto[4]:>15f} {producto[5]:<20}")


# Imprime los productos en pantalla
def imprime_productos(productos):
    # Importa desde Productos 
    from productos import imprime_titulos_listados_completos, imprime_un_producto_forma_horizontal

    # Titulo de total
    total_productos = "Total de Productos :"

    # Imprime encabezados
    imprime_titulos_listados_completos()

    # Detalle del listado de productos
    for producto in productos:
        # Imprime un producto de forma horizontal (en linea)
        imprime_un_producto_forma_horizontal(producto)

    # Imprime el total de productos
    print(f"\n\n{Style.BRIGHT}{Fore.YELLOW} {total_productos}  {Style.BRIGHT}{Fore.LIGHTGREEN_EX}{(len(productos))}")


# Imprime un producto verticalmente
def imprime_un_producto_forma_vertical(producto):
    # 0 = id, 1 = nombre, 2 = descripcion, 3 = cantidad, 4 = precio, 5 = categoria
    print(f"\n{Style.BRIGHT} {Fore.GREEN} Producto seleccionado : ")
    print(f"\n{Style.BRIGHT} {Fore.YELLOW} - Identificador : {Style.BRIGHT} {Fore.LIGHTWHITE_EX}{producto[0]:<5}")
    print(f"{Style.BRIGHT} {Fore.YELLOW} - Nombre : {Style.BRIGHT} {Fore.LIGHTWHITE_EX}{producto[1]:<30}")
    print(f"{Style.BRIGHT} {Fore.YELLOW} - Descripcion : {Style.BRIGHT} {Fore.LIGHTWHITE_EX}{producto[2]:<50}")
    print(f"{Style.BRIGHT} {Fore.YELLOW} - Cantidad : {Style.BRIGHT} {Fore.LIGHTWHITE_EX}{producto[3]:>10}")
    print(f"{Style.BRIGHT} {Fore.YELLOW} - Precio : {Style.BRIGHT} {Fore.LIGHTWHITE_EX}{producto[4]:>10.4f}")
    print(f"{Style.BRIGHT} {Fore.YELLOW} - Categoria : {Style.BRIGHT} {Fore.LIGHTWHITE_EX}{producto[5]:<30}")


# Imprime los productos en pantalla
def imprime_producto(producto):
    # Importa desde Productos 
    from productos import imprime_un_producto_forma_vertical 

    # Imprime un producto de forma Vertical
    imprime_un_producto_forma_vertical(producto)
