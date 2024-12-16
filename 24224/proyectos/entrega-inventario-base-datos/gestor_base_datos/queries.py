# 


# Querie de generacion de tabla
# Genera o crea la tabla de productos
consulta_creacion_tabla_productos = """
        CREATE TABLE IF NOT EXISTS productos (
            "id" INTEGER NOT NULL,
            "nombre" TEXT NOT NULL,
            "descripcion" TEXT NOT NULL,
            "cantidad" INTEGER NOT NULL,
            "precio" REAL,
            "categoria"	TEXT,
            PRIMARY KEY("id" AUTOINCREMENT)
        )
                                    """


#
consulta_agrega_producto = """
                                INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
                                VALUES (?, ?, ?, ?, ?)
                            """


#
consulta_actualiza_producto = """
                                """


#
consulta_actualiza_cantidad_producto = """
                                            UPDATE productos SET cantidad = ? WHERE id = ?
                                        """


#
consulta_lista_bajo_stock = """
                                SELECT * FROM productos WHERE cantidad < ?
                            """


#
consulta_elimina_producto = """
                                DELETE FROM productos WHERE id = ?
                            """


#
consulta_lista_todos_productos = """
                                        SELECT * FROM productos
                                """


#
consulta_lee_producto = """
                            SELECT * FROM productos WHERE id = ?
                        """