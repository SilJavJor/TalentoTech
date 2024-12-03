# Productos

# Importaciones
from screen import limpiar_pantalla, mostrar_mensaje


# Titulo de Agregar Productos
def mostrar_titulo_agregacion():
    print("====   Agregando Productos  ====\n")


# Titulo de Modificar Productos
def mostrar_titulo_modificacion():
    print("====   Modificando Productos  ====\n")


# Titulo de Eliminar Productos
def mostrar_titulo_eliminacion():
    print("====   Eliminando Productos  ====\n")


# Titulo de Buscar Productos
def mostrar_titulo_busquedas():
    print("====   Buscar Productos  ====\n")


# Titulo de Listar Productos
def mostrar_titulo_listados():
    print("====   Listado Productos  ====\n")#


# Valida el ingreso de nombre
def ingresar_nombre():

    while True:
        # Obtiene el nombre, eliminando los espacios a derecha es izquierda alltim()
        nombre = input("\n Nombre : ").strip()

        if len(nombre) >= 1:

            if len(nombre) <= 50:

                # Devuelve  la variable nombre
                return nombre

            else:

                #
                print("El nombre no puede ser mayor a 50 caracteres....")

        else:

            #
            print("El nombre no pude estar vacio...")


# Valida el ingreso de la cantidad
def ingresar_cantidad():

    while True:
        # Obtiene la cantidad en entero
        cantidad = input(" Cantidad : ")

        if cantidad.isdigit():

            if int(cantidad) > 0:

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
        precio = input(" Precio : ")

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

    # Ingreso y validacion de la variable cantidad
    cantidad = ingresar_cantidad()

    # Ingreso y validacion de la variable precio
    precio = ingresar_precio()

    # 
    producto = {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }

    # Se agrega al inventario
    #inventario.append(producto)
    inventario_productos.append(producto)

    # Se informa el producto ingresado
    print(f" Producto ingresado:\n - Nombre: {nombre}\n - Cantidad: {cantidad}\n - Precio: {precio}")

    # Muestra un mensaje en pantalla
    mostrar_mensaje("Producto agregado exitosamente.")


#
def modificar_productos():
    # Importamos el inventario de productos
    #from inventory import inventario_productos

    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_modificacion()

    # Muestra un mensaje en pantalla
    mostrar_mensaje("Opción no implementada...")


# Archivo  -->  Productos
#
def eliminar_productos():
    # Importamos el inventario de productos
    #from inventory import inventario_productos

    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_eliminacion()

    # Muestra un mensaje en pantalla
    mostrar_mensaje("Opción no implementada...")


#
def buscar_productos():
    # Importamos el inventario de productos
    #from inventory import inventario_productos

    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_busquedas()

    # Muestra un mensaje en pantalla
    mostrar_mensaje("Opción no implementada...")


# Listado de Productos por pantalla
def listar_productos():
    # Importamos el inventario de productos
    from inventory import inventario_productos

    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_listados()

    # Verificar que el inventario no se encuentre vacio
    #if (len(inventario) == 0):
    if (len(inventario_productos) == 0):
        # Muestra un mensaje en pantalla
        mostrar_mensaje("No hay productos para mostrar.")

    else:

        # Inicializacion del indice
        indice = 0

        #
        #while (indice < len(inventario)):
        while (indice < len(inventario_productos)):
            # Se imprime el detalle de cada producto
            #print(f" Producto : {inventario[indice]['nombre']}, Cantidad : {inventario[indice]['cantidad']}, Precio : {inventario[indice]['precio']}")
            print(f" Producto : {inventario_productos[indice]['nombre']}, Cantidad : {inventario_productos[indice]['cantidad']}, Precio : {inventario_productos[indice]['precio']}")

            # Actualizacion del indice
            indice += 1

        # Se imprime el detalle de cada producto
        #print(f"\n\n Cantidad Total de Productos : {(len(inventario))}")
        print(f"\n\n Cantidad Total de Productos : {(len(inventario_productos))}")

        # Muestra un mensaje en pantalla
        mostrar_mensaje("")
