# Crear Tablas

# Importaciones
# Importa desde el paquete de conexion
from gestor_base_datos import conectar, guardar_cambios_desconectar
# Importa desde el paquete de pantalla
from pantalla import mostrar_mensaje


# Crea la tabla de productos
def crear_tabla_productos():
    # 
    conn = conectar()

    #
    if (conn):
        #
        nombre_tabla = "productos"

        #
        mostrar_mensaje("Creando tabla de '{nombre_tabla}'...")

        #
        cursor = conn.cursor()

        # esta es la querie consulta_creacion_tabla_productos
        #
        cursor.execute( '''
                            CREATE TABLE IF NOT EXISTS productos (
                                "id" INTEGER NOT NULL,
                                "nombre" TEXT NOT NULL,
                                "descripcion" TEXT,
                                "cantidad" INTEGER NOT NULL,
                                "precio" REAL,
                                "categoria"	TEXT,
                                PRIMARY KEY("id" AUTOINCREMENT)
                        ''' )

        #
        guardar_cambios_desconectar()


        #conexion.commit()
        #conexion.close()

        #
        #print("Tabla 'productos' creada o ya existente.")
        #mostrar_mensaje("Tabla de 'productos' creada o ya existente...")
        mostrar_mensaje("Tabla de '{nombre_tabla}' creada o ya existente...")
