from colorama import Style, Fore
from pantalla import limpiar_pantalla, mostrar_mensaje


# Imprime los productos en pantalla
def imprimir_productos():
    # Importamos el inventario de productos
    from inventory import inventario_productos

    # Encabezados del listado de productos
    print(f"{Style.BRIGHT} {Fore.GREEN} {'Nombre':<20} {'Descripción':<20} {'Cantidad':<8} {'Precio':<10}")
    print(f"=" * 60)

    for producto in inventario_productos:
        print(f"{producto['nombre']:<20} {producto['descripcion']:<20} {producto['cantidad']:<8} {producto['precio']:<6.4f}")

    # Se imprime el detalle de cada producto
    print(f"\n\n Cantidad Total de Productos : {(len(inventario_productos))}")


# Muestra por pantalla un listado de todos los productos
def mostrar_productos():
    # Importamos el inventario de productos
    from inventory import inventario_productos
    #
    from productos.products import mostrar_titulo_listados 
        
    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_listados()

    # Imprime los productos en pantalla
    if (inventario_productos):
        # Imprime todos los productos en el inventario
        imprimir_productos()
    
        # Muestra un mensaje en pantalla
        mostrar_mensaje("")

    else:
        # Muestra un mensaje en pantalla
        mostrar_mensaje("No hay productos para mostrar.")
