# Reporte Bajo Sotck

# Importaciones
# Importa desde Colorama
from colorama import Style, Fore
# Importa desde el paquete de pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje

# Titulo de Reporte de Bajo Stock
def mostrar_titulo_reporte_bajo_stock():
    # Importa desde Pantalla
    from pantalla import mostrar_linea_separacion

    mostrar_linea_separacion()
    print(f"{Style.BRIGHT}{Fore.CYAN}          Reporte de Bajo Stock              \n")
    mostrar_linea_separacion()


# Funcion para buscar productos
def reporte_bajo_stock():
    
    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_reporte_bajo_stock()

    # Muestra un mensaje en pantalla
    #mostrar_mensaje("Opción no implementada....")



    """
        def productos_por_debajo_de_limite(self, limite):
    
        Lista los productos cuya cantidad está por debajo del límite especificado.

        :param limite: Valor límite para la cantidad.
        :return: Lista de productos que cumplen con la condición.
        
        conexion = self.conectar()
        if not conexion:
            return []

        cursor = conexion.cursor()

        try:
            cursor.execute("SELECT * FROM productos WHERE cantidad < ?", (limite,))
            productos = cursor.fetchall()

            return [
                {
                    "id": producto[0],
                    "nombre": producto[1],
                    "descripcion": producto[2],
                    "cantidad": producto[3],
                    "precio": producto[4],
                    "categoria": producto[5],
                }
                for producto in productos
            ]
        except sqlite3.Error as e:
            print(f"Error al generar el reporte: {e}")
            return []
        finally:
            self.cerrar_conexion(conexion)
            
            
    
    def generar_reporte():
    conexion_db = ConexionSQLite()

    # Solicitar el límite al usuario
    try:
        limite = int(input("Ingrese el límite para la cantidad de productos: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    # Obtener los productos debajo del límite
    productos = conexion_db.productos_por_debajo_de_limite(limite)

    if productos:
        # Cabecera del reporte
        print(f"\nProductos con cantidad menor a {limite}:")
        print(f"{'ID':<5} {'Nombre':<30} {'Cantidad':>10} {'Precio':>10} {'Categoría':<30}")
        print("=" * 80)

        # Mostrar los productos
        for producto in productos:
            print(
                f"{producto['id']:<5} "
                f"{producto['nombre']:<30} "
                f"{producto['cantidad']:>10} "
                f"{producto['precio']:>10.4f} "
                f"{producto['categoria']:<30}"
            )
    else:
        print(f"No hay productos con cantidad menor a {limite}.")
    """