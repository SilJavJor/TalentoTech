# Actualizar Productos

# Importaciones
# Importa Colorama
from colorama import Style, Fore
# Importa desde el paquete de pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje
# Importa desde datos
from gestor_base_datos import actualizar_cantidad_producto


# Actualizacion de la Cantidad
def actualiza_cantidad(producto):
    # Importa desde Pantalla
    from productos import ingresa_cantidad

    # Ingreso y validacion de la variable cantidad
    cantidad = ingresa_cantidad()

    # Actualiza la cantidad del producto
    cantidad_actualizada_existosamente = actualizar_cantidad_producto(producto[0], cantidad = cantidad)

    #
    if (cantidad_actualizada_existosamente):
        # Muestra el producto ingresado
        #mostrar_producto_agregado(nombre, descripcion, cantidad, precio, categoria)

        # Muestra un mensaje en pantalla
        mostrar_mensaje("Producto actualizado exitosamente...")        

    else:
        # Muestra un mensaje en pantalla
        mostrar_mensaje("Hubo un error al agregar el producto...")       


# Imprime los productos en pantalla
def imprime_producto(producto):
    # Importa desde Productos 
    from productos import imprime_un_producto_forma_vertical 

    # Imprime un producto de forma Vertical
    imprime_un_producto_forma_vertical(producto)


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
    from productos import buscar_productos, ingresa_cantidad

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

        actualiza_cantidad(producto)

    else:
                # Muestra un mensaje en pantalla
        mostrar_mensaje("Producto no encontrado...")



"""
def main():
    conexion_db = ConexionSQLite()

    # Solicitar el ID del producto a actualizar
    producto_id = int(input("Ingrese el ID del producto que desea actualizar: "))

    # Buscar el producto
    producto = conexion_db.buscar_producto_por_id(producto_id)

    if producto:
        print(f"Producto encontrado: {producto}")

        # Solicitar los nuevos datos (o mantener los existentes)
        nombre = input(f"Nombre [{producto['nombre']}]: ").strip() or producto['nombre']
        descripcion = input(f"Descripción [{producto['descripcion']}]: ").strip() or producto['descripcion']
        cantidad = input(f"Cantidad [{producto['cantidad']}]: ").strip()
        cantidad = int(cantidad) if cantidad else producto['cantidad']
        precio = input(f"Precio [{producto['precio']}]: ").strip()
        precio = float(precio) if precio else producto['precio']
        categoria = input(f"Categoría [{producto['categoria']}]: ").strip() or producto['categoria']

        # Actualizar el producto
        actualizado = conexion_db.actualizar_producto(
            producto_id, nombre, descripcion, cantidad, precio, categoria
        )

        if actualizado:
            print("El producto fue actualizado exitosamente.")
        else:
            print("No se pudo actualizar el producto.")
    else:
        print("El producto no existe.")
"""

"""
    from datos.conexion import ConexionSQLite

def main():
    conexion_db = ConexionSQLite()

    # Solicitar el ID del producto a actualizar
    producto_id = int(input("Ingrese el ID del producto que desea actualizar: "))

    # Buscar el producto
    producto = conexion_db.buscar_producto_por_id(producto_id)

    if producto:
        print(f"Producto encontrado: {producto}")

        # Solicitar los nuevos datos (o mantener los existentes)
        nombre = input(f"Nombre [{producto['nombre']}]: ").strip() or producto['nombre']
        descripcion = input(f"Descripción [{producto['descripcion']}]: ").strip() or producto['descripcion']
        cantidad = input(f"Cantidad [{producto['cantidad']}]: ").strip()
        cantidad = int(cantidad) if cantidad else producto['cantidad']
        precio = input(f"Precio [{producto['precio']}]: ").strip()
        precio = float(precio) if precio else producto['precio']
        categoria = input(f"Categoría [{producto['categoria']}]: ").strip() or producto['categoria']

        # Actualizar el producto
        actualizado = conexion_db.actualizar_producto(
            producto_id, nombre, descripcion, cantidad, precio, categoria
        )

        if actualizado:
            print("El producto fue actualizado exitosamente.")
        else:
            print("No se pudo actualizar el producto.")
    else:
        print("El producto no existe.")

if __name__ == "__main__":
    main()



class ConexionSQLite:
    # ... (el resto del código permanece igual)

    def actualizar_producto(self, producto_id, nombre=None, descripcion=None, cantidad=None, precio=None, categoria=None):
        
        Actualiza un producto en la base de datos.

        :param producto_id: ID del producto a actualizar.
        :param nombre: Nuevo nombre del producto (opcional).
        :param descripcion: Nueva descripción del producto (opcional).
        :param cantidad: Nueva cantidad del producto (opcional).
        :param precio: Nuevo precio del producto (opcional).
        :param categoria: Nueva categoría del producto (opcional).

        conexion = self.conectar()
        if not conexion:
            return False

        cursor = conexion.cursor()
        
        # Crear la consulta dinámica
        campos = []
        valores = []

        if nombre is not None:
            campos.append("nombre = ?")
            valores.append(nombre[:30])

        if descripcion is not None:
            campos.append("descripcion = ?")
            valores.append(descripcion[:50])

        if cantidad is not None:
            campos.append("cantidad = ?")
            valores.append(cantidad)

        if precio is not None:
            campos.append("precio = ?")
            valores.append(precio)

        if categoria is not None:
            campos.append("categoria = ?")
            valores.append(categoria[:30])

        # Agregar el ID al final de los valores
        valores.append(producto_id)

        consulta = f"UPDATE productos SET {', '.join(campos)} WHERE id = ?"
        
        try:
            cursor.execute(consulta, valores)
            conexion.commit()
            print(f"Producto con ID {producto_id} actualizado correctamente.")
            return True
        except sqlite3.Error as e:
            print(f"Error al actualizar el producto: {e}")
            return False
        finally:
            self.cerrar_conexion(conexion)

    
    """
    
    
