# Paquete de Productos

# Importaciones
# Importa desde Menu Productos
from .menu_products import mostrar_menu_productos, opciones_menu_productos
# Importa desde Productos
from .products import ( seleccionar_opciones_menu_productos, imprime_titulos_listados_completos,
                        imprime_un_producto_forma_horizontal, imprime_un_producto_forma_vertical )
# Importa desde Agregar Productos
from .add_products import agregar_productos
# Importa desde Busqueda de Productos
from .search_products import buscar_productos
# Importa desde Eliminar Productos
from .remove_products import eliminar_productos
# Importa desde Actualizar Productos
from .update_products import modificar_productos
# Importa desde Mostrar Productos
from .show_products import mostrar_productos
# Importa desde Mostrar Productos
from .show_product import mostrar_producto
# Importa desde Reporte Bajo Stock
from .under_stock_report import reporte_bajo_stock
# Importa desde Validaciones de Productos
from .validate_products import( valida_texto_vacio, valida_largo_minimo, valida_largo_maximo, valida_numero_vacio,
                                valida_entero, valida_entero_mayor_cero, valida_flotante, valida_flotante_mayor_cero )


#
print("Inicializando el paquete de Productos")