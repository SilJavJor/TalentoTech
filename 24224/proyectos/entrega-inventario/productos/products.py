# Productos

# Importaciones
from colorama import Style, Fore
from pantalla import mostrar_linea_separacion, limpiar_pantalla, mostrar_mensaje
from productos.add_products import agregar_productos
from productos.show_products import mostrar_productos
from productos.update_products import modificar_productos
from productos.remove_products import eliminar_productos
#from productos.search_products import buscar_productos
#from productos.report_add_products import reporte_bajo_stock


# Titulo de Agregar Productos
def mostrar_titulo_agregacion():
    mostrar_linea_separacion()
    print(f"{Style.BRIGHT}{Fore.CYAN}              Agregando Productos               \n")
    mostrar_linea_separacion()


# Titulo de Modificar Productos
def mostrar_titulo_modificacion():
    mostrar_linea_separacion()
    print(f"{Style.BRIGHT}{Fore.CYAN}             Modificando Productos              \n")
    mostrar_linea_separacion()


# Titulo de Eliminar Productos
def mostrar_titulo_eliminacion():
    mostrar_linea_separacion()
    print(f"{Style.BRIGHT}{Fore.CYAN}             Eliminando Productos               \n")
    mostrar_linea_separacion()


# Titulo de Buscar Productos
def mostrar_titulo_busquedas():
    mostrar_linea_separacion()
    print(f"{Style.BRIGHT}{Fore.CYAN}               Buscando Productos               \n")
    mostrar_linea_separacion()


# Titulo de Listar Productos
def mostrar_titulo_listados():
    mostrar_linea_separacion()
    print(f"{Style.BRIGHT}{Fore.CYAN}            Inventario de Productos             \n")
    mostrar_linea_separacion()


# Titulo de Listar Productos
def mostrar_titulo_reporte_bajo_stock():
    mostrar_linea_separacion()
    print(f"{Style.BRIGHT}{Fore.CYAN}          Reporte de Bajo Stock              \n")
    mostrar_linea_separacion()


# Controla y ejecuta las opciones del menu
def seleccionar_opciones_menu_productos(opcion_ingresada):
    if opcion_ingresada == '1':
        # Funcion Agregar Productos
        agregar_productos()

    elif opcion_ingresada == '2':
        # Muestra los productos del inventario
        mostrar_productos()

    elif opcion_ingresada == '3':
        # Funcion Modificar Productos
        modificar_productos()

    elif opcion_ingresada == '4':
        # Funcion Eliminaar Productos
        eliminar_productos()

    elif opcion_ingresada == '5':
        # Funcion Buscar Productos
        buscar_productos()

    elif opcion_ingresada == '6':
        # Funcion Modificar Productos
        reporte_bajo_stock()

    else:
        # Muestra un mensaje en pantalla
        mostrar_mensaje("Opción inválida....")
        opcion_ingresada = 1

    return opcion_ingresada


"""
# Valida el ingreso de nombre
def ingresar_nombre():
    while True:
        # Obtiene el nombre, eliminando los espacios a derecha es izquierda alltim()
        nombre = input("\n Nombre : ").strip().upper()

        if len(nombre) >= 1:
            if len(nombre) <= 30:
                # Devuelve  la variable nombre
                return nombre

            else:
                #
                print("El nombre no puede ser mayor a 30 caracteres....")

        else:
            #
            print("El nombre no pude estar vacio...")


# Valida el ingreso de nombre
def ingresar_descripcion():
    while True:
        # Obtiene la descripcion, eliminando los espacios a derecha es izquierda alltim()
        descripcion = input("\n Descripcion : ").strip().upper()

        if len(descripcion) >= 1:
            if len(descripcion) <= 50:
                # Devuelve  la variable descripcion
                return descripcion

            else:
                #
                print("La descripcion no puede ser mayor a 50 caracteres...")

        else:
            #
            print("La descripcion no pude estar vacia...")


# Valida el ingreso de la cantidad
def ingresar_cantidad():
    while True:
        # Obtiene la cantidad en entero
        cantidad = input("\n Cantidad : ")

        if cantidad.isdigit():
            if (int(cantidad) > 0):
                # Devuelve  la variable cantidad
                return int(cantidad)

            else:
                #
                print(" La cantidad debe ser un número mayor a cero...")

        else:
            #
            print(" La cantidad debe ser un número entero...")


# Valida el ingreso de la cantidad
def ingresar_precio():
    while True:
        precio = input("\n Precio : ")

        if (precio.isdecimal()):
            if (float(precio) > 0.0000):
                # Devuelve  la variable cantidad
                return float(precio)

            else:
                #
                print(" El precio debe ser un número mayor a cero...")

        else:
            #
            print(" El precio debe ser un número con decimales...")


# Agrega productos al Inventario
def agregar_productos():
    # Importamos el inventario de productos
    from inventory import inventario_productos
    
    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_agregacion()

    # Muestra el encabezado de los datos a ingresar 
    print("\n Datos del Producto a ingresar : ")#

    # Variables que se utilizan para cargar el producto
    # Ingreso y validacion de la variable nombre
    nombre = ingresar_nombre()

    # Ingreso y validacion de la variable precio
    descripcion = ingresar_descripcion()

    # Ingreso y validacion de la variable cantidad
    cantidad = ingresar_cantidad()

    # Ingreso y validacion de la variable precio
    precio = ingresar_precio()

    # 
    producto = { 'nombre': nombre, 'descripcion': descripcion, 'cantidad': cantidad, 'precio': precio }

    # Se agrega al inventario
    inventario_productos.append(producto)

    # Se informa el producto ingresado
    print(f" \n Producto ingresado : ")
    print(f" - Nombre : {nombre}")
    print(f" - Descripcion : {descripcion}")
    print(f" - Cantidad : {cantidad}")
    print(f" - Precio : {precio}")

    # Muestra un mensaje en pantalla
    mostrar_mensaje("Producto agregado exitosamente.")
"""

"""
# Imprime los productos en pantalla
def imprimir_productos():
    # Importamos el inventario de productos
    from inventory import inventario_productos

    # Encabezados del listado de productos
    print(f"{Style.BRIGHT} {Fore.GREEN} {'Nombre':<20} {'Descripción':<20} {'Cantidad':<8} {'Precio':<10}")
    print(f"=" * 60)

    for producto in inventario_productos:
        print(f"{producto['nombre']:<20} {producto['descripcion']:<20} {producto['cantidad']:<8} {producto['precio']:<6.4f}")

    # Se imprime el detalle de cada producto
    print(f"\n\n Cantidad Total de Productos : {(len(inventario_productos))}")


# Muestra por pantalla un listado de todos los productos
def mostrar_productos():
    # Importamos el inventario de productos
    from inventory import inventario_productos

    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_listados()

    # Imprime los productos en pantalla
    if (inventario_productos):
        # Imprime todos los productos en el inventario
        imprimir_productos()
    
        # Muestra un mensaje en pantalla
        mostrar_mensaje("")

    else:
        # Muestra un mensaje en pantalla
        mostrar_mensaje("No hay productos para mostrar.")


# Funcion de Modificacion de Productos
def modificar_productos():
    # Importamos el inventario de productos
    #from inventory import inventario_productos

    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_modificacion()

    # Muestra un mensaje en pantalla
    mostrar_mensaje("Opción no implementada...")
"""


"""
# Funcion de Eliminacion de Productos
def eliminar_productos():
    # Importamos el inventario de productos
    #from inventory import inventario_productos

    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_eliminacion()

    # Muestra un mensaje en pantalla
    mostrar_mensaje("Opción no implementada...")
"""

# Funcion para buscar productos
def buscar_productos():
    # Importamos el inventario de productos
    #from inventory import inventario_productos

    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_busquedas()

    # Muestra un mensaje en pantalla
    mostrar_mensaje("Opción no implementada...")


# Funcion para buscar productos
def reporte_bajo_stock():
    # Importamos el inventario de productos
    #from inventory import inventario_productos

    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_reporte_bajo_stock()

    # Muestra un mensaje en pantalla
    mostrar_mensaje("Opción no implementada...")
