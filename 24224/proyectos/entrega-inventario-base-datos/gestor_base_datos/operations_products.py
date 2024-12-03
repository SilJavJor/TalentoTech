# Operaciones de Productos
# Con Base de Datos

# Importaciones
# Importa desde sqlite3
import sqlite3
# Importa desde el paquete de pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje
# Importa desde el paquete de conexion
from gestor_base_datos import conectar, desconectar, verifica_conexion
#Importa desde Productos
#from productos import imprime_titulos_listados_completos


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
def insertar_producto():
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

# Inserta un producto
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
def listar_productos():
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
    Obtiene todos los productos de la base de datos.
    Devuelve una lista con los productos y una vacia si no existen productos cargados
    """
    #    
    conn = conectar()

    if not verifica_conexion(conn):
        return []

    cursor = conn.cursor()

    try:
        # pasar a variable
        # Querie de Listado de productos
        cursor.execute("SELECT * FROM productos")

        #
        productos = cursor.fetchall()

        return productos


    except sqlite3.Error:
        return []

    finally:
        desconectar(conn)
