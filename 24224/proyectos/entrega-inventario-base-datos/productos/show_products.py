# Mostrar Productos

# Importaciones
# Importa desde datos
from gestor_base_datos import listar_productos
# Importa desde Pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje

# Imprime los productos en pantalla
def imprime_productos(productos):
    # Titulo de total
    total_productos = " Total de Productos :"

    # Detalle del listado de productos
    for producto in productos:
        # 0 = id, 1 = nombre, 2 = descripcion, 3 = cantidad, 4 = precio, 5 = categoria
        print(f"{producto[1]:<30} {producto[2]:<30} {producto[3]:>12} {producto[4]:>15f} {producto[5]:<25}")

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
