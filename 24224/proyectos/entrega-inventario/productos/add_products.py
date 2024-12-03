# Agregar Productos

# Importaciones
from pantalla.screen import limpiar_pantalla, mostrar_mensaje


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
            print("La descripcion no puede estar vacia...")


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


# Valida el ingreso de nombre
def ingresar_categoria():
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


# Agrega productos al Inventario
def agregar_productos():
    # Importamos el inventario de productos
    from inventory import inventario_productos
    #
    from productos.products import mostrar_titulo_agregacion 
    
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

    # Ingreso y validacion de la variable precio
    categoria = ingresar_categoria()

    # 
    producto = {
                    'nombre': nombre,
                    'descripcion': descripcion, 
                    'cantidad': cantidad, 
                    'precio': precio, 
                    'categoria': categoria
                }

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
