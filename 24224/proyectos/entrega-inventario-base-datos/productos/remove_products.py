# Eliminar Productos

# Importaciones
# Importa desde Colorama
from colorama import Style, Fore
# Importa desde el paquete de pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje
# Importa desde datos
from gestor_base_datos import eliminar_producto

# Actualizacion de la Cantidad
def elimina_producto(producto):
    # Actualiza la cantidad del producto
    eliminado_existosamente = eliminar_producto(producto[0],)

    #
    if (eliminado_existosamente):
        # Muestra un mensaje en pantalla
        mostrar_mensaje("Producto eliminado exitosamente...")        

    else:
        # Muestra un mensaje en pantalla
        mostrar_mensaje("Hubo un error al eliminar el producto...")       


# Titulo de Eliminar Productos
def mostrar_titulo_eliminacion():
    # Importa desde Pantalla
    from pantalla import mostrar_linea_separacion

    mostrar_linea_separacion()
    print(f"{Style.BRIGHT}{Fore.CYAN}             Eliminando Productos               \n")
    mostrar_linea_separacion()


# Funcion de Eliminacion de Productos
def eliminar_productos():
    # Importa desde Productos 
    from productos import buscar_productos, imprime_producto

    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_eliminacion()

    # Obtiene el Listado de los Productos
    producto = buscar_productos("Eliminar")    

    # Imprime los productos en pantalla
    if (producto):
        # Muestra los datos del producto
        imprime_producto(producto)

        # Elimina el producto seleccionado
        elimina_producto(producto)

    else:
        # Muestra un mensaje en pantalla
        mostrar_mensaje("Producto no encontrado...")


"""
    if producto:
        print(f"Producto encontrado: {producto}")
        confirmacion = input("¿Está seguro de que desea eliminar este producto? (s/n): ").strip().lower()
        if confirmacion == 's':
            eliminado = conexion_db.eliminar_producto(producto_id)
            if eliminado:
                print("El producto fue eliminado exitosamente.")
            else:
                print("No se pudo eliminar el producto.")
        else:
            print("Operación cancelada.")
    else:
        print("El producto no existe.")
"""