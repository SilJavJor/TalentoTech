# Mostrar Productos

# Importaciones
# Importa desde datos
from gestor_base_datos import listar_productos
# Importa desde Pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje

# Imprime los productos en pantalla
def imprime_productos(productos):
    # Importa desde Productos 
    from productos import imprime_un_producto_forma_horizontal 
    
    # Titulo de total
    total_productos = " Total de Productos :"

    # Detalle del listado de productos
    for producto in productos:
        # Imprime un producto de forma horizontal (en linea)
        imprime_un_producto_forma_horizontal(producto)

    # Imprime el total de productos
    print(f"\n\n {total_productos} {(len(productos))}")


# Muestra por pantalla un listado de todos los productos
def mostrar_productos():
    # Importa desde Productos 
    from productos import mostrar_titulo_listados, imprime_titulos_listados_completos 

    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_listados()

    # Obtiene el Listado de los Productos
    productos = listar_productos()

    # Imprime los productos en pantalla
    if (productos):
        # Imprime encabezados
        imprime_titulos_listados_completos()

        # Imprime todos los productos en el inventario
        imprime_productos(productos)

        # Muestra un mensaje en pantalla
        mostrar_mensaje("")

    else:
        # Muestra un mensaje en pantalla
        mostrar_mensaje("No hay productos para mostrar...")
