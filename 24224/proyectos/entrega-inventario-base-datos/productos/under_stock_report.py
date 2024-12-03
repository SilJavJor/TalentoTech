# Reporte Bajo Sotck

# Importaciones
# Importa desde el paquete de pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje

# Funcion para buscar productos
def reporte_bajo_stock():
    # Importamos el inventario de productos
    from inventory import inventario_productos
    # Importa el Titulo 
    from productos import mostrar_titulo_reporte_bajo_stock
    
    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_reporte_bajo_stock()

    # Muestra un mensaje en pantalla
    mostrar_mensaje("Opción no implementada...")
