# Actualiza la Cantidad de un Producto

# Importaciones
# Importa Colorama
from colorama import Style, Fore
# Importa desde el paquete de pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje
# Importa desde datos
from gestor_base_datos import actualiza_cantidad_producto


# Actualizacion de la Cantidad
def actualiza_cantidad(producto):
    # Importa desde Pantalla
    from productos import ingresa_cantidad

    # Ingreso y validacion de la variable cantidad
    cantidad = ingresa_cantidad()

    # Actualiza la cantidad del producto
    cantidad_actualizada_existosamente = actualiza_cantidad_producto(producto[0], cantidad = cantidad)

    #
    if (cantidad_actualizada_existosamente):
        # Muestra un mensaje en pantalla
        mostrar_mensaje("Producto actualizado exitosamente...")        

    else:
        # Muestra un mensaje en pantalla
        mostrar_mensaje("Hubo un error al actualizar la cantidad...")       


# Titulo de Modificar Productos
def mostrar_titulo_actualizacion_cantidad():
    # Importa desde Pantalla
    from pantalla import mostrar_linea_separacion

    mostrar_linea_separacion()
    print(f"{Style.BRIGHT}{Fore.CYAN}             Actualizando Cantidad              \n")
    mostrar_linea_separacion()


# Funcion de Modificacion de Productos
def modificar_cantidad():
    # Importa desde Productos 
    from productos import buscar_productos, imprime_producto

    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_actualizacion_cantidad()

    # Obtiene el Listado de los Productos
    producto = buscar_productos("Actualizar")    

    # Imprime los productos en pantalla
    if (producto):
        # Muestra los datos del producto
        imprime_producto(producto)

        # Actualiza la cantidad
        actualiza_cantidad(producto)

    else:
        # Muestra un mensaje en pantalla
        mostrar_mensaje("Producto no encontrado...")
