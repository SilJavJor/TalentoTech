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
consulta_agregar_producto = """
                                INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
                                VALUES (?, ?, ?, ?, ?)
                            """


#
consulta_actualizar_producto = """
                                """


#
consulta_actualizar_cantidad_producto = """
                                            UPDATE productos SET cantidad = ? WHERE id = ?
                                        """


#
consulta_eliminar_producto = """
                                """


#
consulta_listar_todos_productos = """
                                        SELECT * FROM productos
                                """


#
consulta_leer_producto = """
                            SELECT * FROM productos WHERE id = ?
                        """