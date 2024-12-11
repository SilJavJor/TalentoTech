# Eliminar Productos

# Importaciones
# Importa desde Colorama
from colorama import Style, Fore
# Importa desde el paquete de pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje


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
    from productos import buscar_productos

    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_eliminacion()

    # Muestra un mensaje en pantalla
    #mostrar_mensaje("Opción no implementada....")
    # Muestra el titulo para la ventana de Agregacion
    #mostrar_titulo_busquedas()

    # Obtiene el Listado de los Productos
    producto = buscar_productos("Eliminar")    

    # Imprime los productos en pantalla
    if (producto):
        # Imprime un producto del inventario
        #imprime_producto(producto)

        # Muestra un mensaje en pantalla
        mostrar_mensaje("")

    else:
                # Muestra un mensaje en pantalla
        mostrar_mensaje("Producto no encontrado...")


"""
def main():

    cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
    
    # Solicitar el ID del producto a eliminar
    producto_id = int(input("Ingrese el ID del producto que desea eliminar: "))

    # Buscar el producto
    producto = conexion_db.buscar_producto_por_id(producto_id)

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