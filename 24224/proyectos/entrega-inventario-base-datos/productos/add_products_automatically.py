# 

"""
pip install faker    
    
    
    from faker import Faker
import random
from datos.conexion import ConexionSQLite

def cargar_productos(cantidad=10):
    Carga una cantidad de productos generados aleatoriamente en la base de datos.
    
    # Instancia de Faker
    fake = Faker()

    # Conexión a la base de datos
    conexion_db = ConexionSQLite()
    conexion = conexion_db.conectar()

    if conexion:
        cursor = conexion.cursor()
        for _ in range(cantidad):
            # Generar datos aleatory
            nombre = fake.unique.word()[:30]
            descripcion = fake.sentence(nb_words=6)[:50]
            cantidad = random.randint(1, 100)
            precio = round(random.uniform(1.00, 100.00), 4)
            categoria = fake.word()[:30]

            # Insertar el producto en la base de datos
            cursor.execute("""
                #INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
                #VALUES (?, ?, ?, ?, ?)
            """, (nombre, descripcion, cantidad, precio, categoria))

        # Guardar cambios y cerrar la conexión
        conexion.commit()
        print(f"Se han cargado {cantidad} productos aleatorios en la base de datos.")
        conexion_db.cerrar_conexion(conexion)

    if __name__ == "__main__":
        # Carga 20 productos de ejemplo
        cargar_productos(20)

"""
