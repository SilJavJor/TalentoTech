# Agregar Productos

# Importaciones
# Importa desde datos
from gestor_base_datos import agregar_producto
# Importa desde el paquete de pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje


# Valida si el texto esta vacio 
def valida_texto_vacio( texto = ""):
    #
    if (not texto):
        #
        return False

    else:
        #
        return True


# Valida el largo minimo 
def valida_largo_minimo(texto = "", largo_minimo = 1):
    #
    if (len(texto) >= int(largo_minimo)):
        #
        return True

    else:
        #
        return False


# Valida si el texto esta vacio 
def valida_largo_maximo(texto = "", largo_maximo = 1):
    #
    if (len(texto) <= int(largo_maximo)):
        #
        return True

    else:
        #
        return False


# Ingreso de la cantidad del producto
def ingresa_nombre():
    #
    #largo_minimo = 1
    #
    largo_maximo = 30

    # Valida el ingreso de nombre   
    while True:
        # Obtiene el nombre, eliminando los espacios a derecha es izquierda alltim()
        nombre = input("\n Nombre : ").strip().upper()

        #
        if (valida_texto_vacio(nombre)):
            #
            if (valida_largo_maximo(nombre, largo_maximo)):
                # Devuelve  la variable nombre
                return nombre

            else:
                #
                mostrar_mensaje(f"El nombre no puede ser mayor a {largo_maximo} caracteres...")
        else:
            #
            mostrar_mensaje(f"El nombre no pude estar vacio...")

"""
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
"""

# Ingreso el nombre del producto
def ingresar_descripcion():
    #
    #largo_minimo = 1
    #
    largo_maximo = 50

    # Valida el ingreso de descripcion   
    while True:
        # Obtiene la descripcion, eliminando los espacios a derecha es izquierda alltim()
        descripcion = input("\n Descripcion : ").strip().upper()

        #
        if (valida_texto_vacio(descripcion)):
            #
            if (valida_largo_maximo(descripcion, largo_maximo)):
                # Devuelve  la variable descripcion
                return descripcion

            else:
                #
                mostrar_mensaje(f"El descripcion no puede ser mayor a {largo_maximo} caracteres...")

        else:
            #
            mostrar_mensaje(f"La descripcion no puede estar vacia...")

"""
        #
        if (len(descripcion) >= int(largo_minimo)):
            #
            if (len(descripcion) <= int(largo_maximo)):
                # Devuelve  la variable descripcion
                return descripcion

            else:
                #
                mostrar_mensaje(f"El descripcion no puede ser mayor a {largo_maximo} caracteres...")

        else:
            #
            mostrar_mensaje(f"La descripcion no puede estar vacia...")
"""

# Valida si es un entero y que no este vacio
def valida_entero(entero):
    # Verifica que no este vacio
    if (not entero):
        #
        mostrar_mensaje(f" La cantidad debe ser un número mayor a cero...")
        
        return False
        
    else:
        try:
            # Intenta convertir a entero
            int(entero)

            return True

        except ValueError:
            #
            mostrar_mensaje(f" La cantidad debe ser un número entero...")

            return False


# Ingreso la cantidad del producto
def ingresar_cantidad():
    #   
    while True:
        # Obtiene la cantidad en entero
        cantidad = input("\n Cantidad : ")

        # Valida la cantidad
        if (valida_entero(cantidad)):
            # Devuelve  la variable cantidad
            return int(cantidad)


# Ingreso el precio del producto
def ingresar_precio():
    while True:
        precio = input("\n Precio : ")

        # Valida la cantidad
        if (valida_entero(precio)):
            # Devuelve  la variable cantidad
            return int(precio)

        """
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
"""


# Ingreso de la cantidad del producto
# Valida el ingreso de nombre
def ingresar_categoria():
    #
    #largo_minimo = 1
    #
    largo_maximo = 30

    # Valida el ingreso de descripcion
    while True:
        # Obtiene la categoria, eliminando los espacios a derecha es izquierda alltim()
        categoria = input("\n Categoria : ").strip().upper()


        #
        if (valida_texto_vacio(descripcion)):
            #
            if (valida_largo_maximo(descripcion, largo_maximo)):
                # Devuelve  la variable nombre
                return categoria

            else:
                #
                mostrar_mensaje(f"El categoria no puede ser mayor a {largo_maximo} caracteres...")

        else:
            #
            mostrar_mensaje(f"La categoria no puede estar vacia...")

"""
        #
        if (len(categoria) >= int(largo_minimo)):
            #
            if (len(categoria) <= int(largo_maximo)):
                # Devuelve  la variable nombre
                return categoria

            else:
                #
                mostrar_mensaje(f"El categoria no puede ser mayor a {largo_maximo} caracteres...")
        else:
            #
            mostrar_mensaje(f"La categoria no puede estar vacia...")
"""


# Muestra el producto ingresado
def mostrar_producto_agregado( nombre, descripcion, cantidad, precio, categoria):
    # Muestra los datos del producto agregado
    print(f" \n Producto ingresado : ")
    print(f" - Nombre : {nombre}")
    print(f" - Descripcion : {descripcion}")
    print(f" - Cantidad : {cantidad}")
    print(f" - Precio : {precio}")
    print(f" - Categoria : {categoria}")


# Agrega productos al Inventario
def agregar_productos():
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

    # Agrega un producto
    agregado_correctamente = agregar_producto( 
                                                nombre = nombre, descripcion = descripcion,
                                                cantidad = cantidad, precio = precio,
                                                categoria = categoria
                                            )

    #
    if (agregado_correctamente):
        # Muestra el producto ingresado
        mostrar_producto_agregado( nombre, descripcion, cantidad, precio, categoria )
        
        # Muestra un mensaje en pantalla
        mostrar_mensaje("Producto agregado exitosamente...")        

    else:
        # Muestra un mensaje en pantalla
        mostrar_mensaje("Hubo un error al agregar el producto...")        
