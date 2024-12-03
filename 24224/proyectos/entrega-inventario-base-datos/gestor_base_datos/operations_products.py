# Operaciones de Productos
# Con Base de Datos

# Importaciones
# Importa desde sqlite3
import sqlite3
# Importa desde el paquete de pantalla
#from pantalla import limpiar_pantalla, mostrar_mensaje
# Importa desde el paquete de conexion
from gestor_base_datos import conectar, desconectar, verifica_conexion,guardar_cambios_desconectar



# Leer un producto
def leer_producto():
    #
    conn = conectar()

    #
    if (conn):
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO productos (nombre, precio) VALUES (?, ?)
        ''', (nombre, precio)) # type: ignore

        conn.commit()
        conn.close()

        print(f"Producto '{nombre}' agregado con éxito.") # type: ignore


# Inserta un producto
def agregar_producto(nombre, descripcion, cantidad, precio, categoria):
    """
    agrega un nuevo producto en la base de datos.

    :parametros
        nombre: Nombre del producto (maximo 30 caracteres).
        descripcion: Descripción del producto (maximo 50 caracteres).
        cantidad: Cantidad disponible del producto.
        precio: Precio del producto (con hasta 4 decimales).
        categoria: Categoría del producto (maximo 30 caracteres).
        True si se inserto correctamente, False  si se inserto incorrectamente.
    """
    # Importa desde el paquete de base de datos
    from gestor_base_datos import consulta_agregar_producto


    # Obtiene la conexion    
    cnn = conectar()

    #
    if not verifica_conexion(cnn):
        #
        return False

    #
    cursor = cnn.cursor()

    #
    try:
        # Querie de Agregado de productos
        cursor.execute( consulta_agregar_producto, (nombre[:30], descripcion[:50], cantidad, round(precio, 4), 
                        categoria[:30]))

        #
        guardar_cambios_desconectar(cnn)

        return True
        
    except sqlite3.Error:

        #
        return False

    finally:
        desconectar(cnn)


# Actualizar un producto
def actualizar_producto():
    #
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO productos (nombre, precio) VALUES (?, ?)
        ''', (nombre, precio)) # type: ignore
        conn.commit()
        conn.close()
        print(f"Producto '{nombre}' agregado con éxito.") # type: ignore


# Elimina un producto
def eliminar_producto():
    #
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO productos (nombre, precio) VALUES (?, ?)
        ''', (nombre, precio)) # type: ignore
        conn.commit()
        conn.close()
        print(f"Producto '{nombre}' agregado con éxito.") # type: ignore


# Listar productos
def listar_producto():
    #
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO productos (nombre, precio) VALUES (?, ?)
        ''', (nombre, precio)) # type: ignore
        conn.commit()
        conn.close()
        print(f"Producto '{nombre}' agregado con éxito.") # type: ignore


# Listar productos
def listar_productos():
    """
    obtiene todos los productos de la base de datos.
    devuelve una lista con los productos y una vacia si no existen productos cargados
    """
    # Importa desde el paquete de base de datos
    from gestor_base_datos import consulta_listar_todos_productos

    # Obtiene la conexion    
    cnn = conectar()

    #
    if not verifica_conexion(cnn):
        return []

    #
    cursor = cnn.cursor()

    #
    try:
        # Querie que devuelve el Listado de productos
        cursor.execute(consulta_listar_todos_productos)

        #
        productos = cursor.fetchall()

        return productos

    except sqlite3.Error:
        return []

    finally:
        desconectar(cnn)
