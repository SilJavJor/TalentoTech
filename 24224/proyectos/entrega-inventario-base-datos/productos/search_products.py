# Search Products

# Importaciones
# Importa desde Colorama
from colorama import Style, Fore
# Importa desde Pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje


# Funcion para buscar productos
def buscar_productos():
    # Importa el Titulo 
    from productos import mostrar_titulo_busquedas 

    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_busquedas()

    # Muestra un mensaje en pantalla
    mostrar_mensaje("Opción no implementada...")



    """




    class ConexionSQLite:
    # ... (el resto del código permanece igual)

    def buscar_producto_por_id(self, producto_id):
        
        Busca un producto por su ID en la base de datos.

        :param producto_id: ID del producto a buscar.
        :return: Diccionario con los datos del producto si se encuentra, None en caso contrario.
        
        conexion = self.conectar()
        if not conexion:
            return None

        cursor = conexion.cursor()

        try:
            cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
            producto = cursor.fetchone()

            if producto:
                # Convertir a diccionario para facilitar su uso
                return {
                    "id": producto[0],
                    "nombre": producto[1],
                    "descripcion": producto[2],
                    "cantidad": producto[3],
                    "precio": producto[4],
                    "categoria": producto[5],
                }
            else:
                print(f"No se encontró un producto con ID {producto_id}.")
                return None
        except sqlite3.Error as e:
            print(f"Error al buscar el producto: {e}")
            return None
        finally:
            self.cerrar_conexion(conexion)


from datos.conexion import ConexionSQLite

def main():
    conexion_db = ConexionSQLite()

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

if __name__ == "__main__":
    main()


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

    """