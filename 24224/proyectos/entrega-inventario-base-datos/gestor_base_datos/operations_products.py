# Operaciones de Productos
# Con Base de Datos

# Importaciones
# Importa desde sqlite3
import sqlite3
# Importa desde el paquete de conexion
from gestor_base_datos import conectar, desconectar, verifica_conexion,guardar_cambios_desconectar

# Lee un producto
def lee_producto(id):
    """
    Busca un producto por su ID en la base de datos.

    :parametros
        id: Identificador del producto a buscar.
        return: Si lo encuantra devuelve el producto, None si no lo encuentra.
    """
    # Importa desde el paquete de base de datos
    from gestor_base_datos import consulta_leer_producto

    # Obtiene la conexion    
    cnn = conectar()

    #
    if not verifica_conexion(cnn):
        return []

    #
    cursor = cnn.cursor()

    #
    try:
        # Query que devuelve el producto
        cursor.execute(consulta_leer_producto, (id,))

        #
        producto = cursor.fetchone()

        return producto

    except sqlite3.Error:
        return []

    finally:
        desconectar(cnn)


# Agrega un Producto
def agrega_producto(nombre, descripcion, cantidad, precio, categoria):
    """
    Agrega un nuevo producto en la base de datos.

    :parametros
        nombre : Nombre del producto (maximo 30 caracteres).
        descripcion : Descripción del producto (maximo 50 caracteres).
        cantidad : Cantidad disponible del producto.
        precio : Precio del producto (con hasta 4 decimales).
        categoria : Categoría del producto (maximo 30 caracteres).
        return : True si se inserto correctamente, False  si no se pudo insertar.
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
        # Query de Agregado de productos
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


# Actualiza la cantidad de un producto
def actualiza_cantidad_producto(id, cantidad):
    """
    Actualiza la cantidad del producto modificado.

    :parametros
        id : identificador del producto al cual se le desea modificar la cantidad
        cantidad : Cantidad disponible del producto.
        return : True si se inserto correctamente, False  si no se pudo insertar.
    """
    # Importa desde el paquete de base de datos
    from gestor_base_datos import consulta_actualizar_cantidad_producto

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
        # Query de Actualizacion de cantidad del producto
        cursor.execute(consulta_actualizar_cantidad_producto, (cantidad, id))

        #
        guardar_cambios_desconectar(cnn)

        #
        return True

    except sqlite3.Error:
        #
        return False

    finally:
        desconectar(cnn)


# Actualiza la cantidad de un producto
def lista_reporte_bajo_stock(limite = 1):
    """
    Lista los productos cuya cantidad estan por debajo del límite indicado.

    :parametros
        limite : Valor límite superior para la cantidad.
        return : Devuelve una lista con los productos, Una lista vacia si no existen productos debajo del limite
    """
    # Importa desde el paquete de base de datos
    from gestor_base_datos import consulta_lista_bajo_stock

    # Obtiene la conexion    
    cnn = conectar()

    #
    if not verifica_conexion(cnn):
        #
        return []

    #
    cursor = cnn.cursor()

    #
    try:
        # Query que devuelve el Listado de los Productos con Bajo Stock
        # Segun el limite ingresado
        cursor.execute(consulta_lista_bajo_stock, (limite,))
        
        #
        productos = cursor.fetchall()

        return productos
        
    except sqlite3.Error:
        return []

    finally:
        desconectar(cnn)


# Actualizar un producto
def actualiza_producto():
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
def elimina_producto(id):
    """
    Busca un producto por su ID en la base de datos.

    :parametros
        id: Identificador del producto a buscar.
        return : True si se elimino correctamente, False  si no se pudo eliminar.
    """
    # Importa desde el paquete de base de datos
    from gestor_base_datos import consulta_eliminar_producto

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
        # Query que devuelve el producto
        cursor.execute(consulta_eliminar_producto, (id,))

        #
        guardar_cambios_desconectar(cnn)

        #
        return True

    except sqlite3.Error:
        #
        return False

    finally:
        desconectar(cnn)


# Lista todos los Productos
def lista_productos():
    """
    Obtiene todos los productos de la base de datos.
    Devuelve una lista con los productos y una vacia si no existen productos cargados
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
        # Query que devuelve el Listado de productos
        cursor.execute(consulta_listar_todos_productos)

        #
        productos = cursor.fetchall()

        return productos

    except sqlite3.Error:
        return []

    finally:
        desconectar(cnn)
