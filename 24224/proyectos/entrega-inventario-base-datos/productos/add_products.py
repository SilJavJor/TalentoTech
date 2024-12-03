# Agregar Productos

# Importaciones
# Importa desde el paquete de pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje


# Valida el ingreso de nombre
def ingresar_nombre():
    #
    largo_minimo = 1
    #
    largo_maximo = 30

    # Valida el ingreso de nombre   
    while True:
        # Obtiene el nombre, eliminando los espacios a derecha es izquierda alltim()
        nombre = input("\n Nombre : ").strip().upper()

        #
        if (len(nombre) >= int(largo_minimo)):
            #
            if (len(nombre) <= int(largo_maximo)):
                # Devuelve  la variable nombre
                return nombre

            else:
                #
                mostrar_mensaje(f"El nombre no puede ser mayor a {largo_maximo} caracteres...")

        else:
            #
            mostrar_mensaje(f"El nombre no pude estar vacio...")


# Valida el ingreso de nombre
def ingresar_descripcion():
    #
    largo_minimo = 1
    #
    largo_maximo = 50

    # Valida el ingreso de descripcion   
    while True:
        # Obtiene la descripcion, eliminando los espacios a derecha es izquierda alltim()
        descripcion = input("\n Descripcion : ").strip().upper()

        #
        if (len(descripcion) >= int(largo_minimo)):
            #
            if (len(descripcion) <= int(largo_maximo)):
                # Devuelve  la variable descripcion
                return descripcion

            else:
                #
                #print("La descripcion no puede ser mayor a 50 caracteres...")
                mostrar_mensaje(f"El descripcion no puede ser mayor a {largo_maximo} caracteres...")

        else:
            #
            #print("La descripcion no puede estar vacia...")
            mostrar_mensaje(f"La descripcion no puede estar vacia...")


# Valida el ingreso de la cantidad
def ingresar_cantidad():
    while True:
        # Obtiene la cantidad en entero
        cantidad = input("\n Cantidad : ")

        # Verifica si es un digito
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
    #
    largo_minimo = 1
    #
    largo_maximo = 30

    # Valida el ingreso de descripcion
    while True:
        # Obtiene la categoria, eliminando los espacios a derecha es izquierda alltim()
        categoria = input("\n Categoria : ").strip().upper()

        #
        if (len(categoria) >= int(largo_minimo)):
            #
            if (len(categoria) <= int(largo_maximo)):
                # Devuelve  la variable nombre
                return categoria

            else:
                #
                #print("La categoria no puede ser mayor a 30 caracteres....")
                mostrar_mensaje(f"El categoria no puede ser mayor a {largo_maximo} caracteres...")
        else:
            #
            #print("La categoria no pude estar vacio...")
            mostrar_mensaje(f"La categoria no puede estar vacia...")



# Agrega productos al Inventario
def agregar_productos():
    # Importamos el inventario de productos
    from inventory import inventario_productos
    # Importa el Titulo 
    from productos import mostrar_titulo_agregacion 
    
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
    print(f" - Categoria : {categoria}")

    # Muestra un mensaje en pantalla
    mostrar_mensaje("Producto agregado exitosamente.")
