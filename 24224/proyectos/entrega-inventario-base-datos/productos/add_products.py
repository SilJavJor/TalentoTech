# Agregar Productos

# Importaciones
# Importa Colorama
from colorama import Style, Fore
# Importa desde datos
from gestor_base_datos import agregar_producto
# Importa desde el paquete de pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje, limpia_error_mostrar_mensaje


# Ingreso de la cantidad del producto
def ingresa_nombre():
    # Importa el Validaciones 
    from productos import valida_texto_vacio, valida_largo_maximo

    #
    largo_maximo = 30

    # Valida el ingreso de nombre   
    while True:
        # Obtiene el nombre, eliminando los espacios a derecha es izquierda alltim()
        nombre = input(f"{Style.BRIGHT} {Fore.LIGHTYELLOW_EX}\n Nombre : {Style.BRIGHT} {Fore.WHITE}").strip().upper()

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

        limpia_error_mostrar_mensaje(8, 8)


# Ingreso el nombre del producto
def ingresa_descripcion():
        # Importa el Validaciones 
    from productos import valida_texto_vacio, valida_largo_maximo

    #
    largo_maximo = 50

    # Valida el ingreso de descripcion   
    while True:
        # Obtiene la descripcion, eliminando los espacios a derecha es izquierda alltim()
        descripcion = input(f"{Style.BRIGHT} {Fore.LIGHTYELLOW_EX}\n Descripcion : {Style.BRIGHT} {Fore.WHITE}").strip().upper()

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

        limpia_error_mostrar_mensaje(8, 8)


# Ingreso la cantidad del producto
def ingresa_cantidad():
    # Importa el Validaciones
    from productos import valida_numero_vacio, valida_entero, valida_entero_mayor_cero

    #   
    while True:
        # Obtiene la cantidad en entero
        cantidad = input(f"{Style.BRIGHT} {Fore.LIGHTYELLOW_EX}\n Cantidad : {Style.BRIGHT} {Fore.WHITE}")

        # Valida la cantidad
        if (valida_numero_vacio(cantidad)):
            #
            if (valida_entero(cantidad)):
                #
                if (valida_entero_mayor_cero(cantidad)):
                    # Devuelve  la variable cantidad
                    return int(cantidad)

            else:
                #
                mostrar_mensaje(f"La cantidad debe ser un número entero...")

        else:
            #
            mostrar_mensaje(f"La cantidad debe ser un número mayor a cero...")

        limpia_error_mostrar_mensaje(8, 8)


# Ingreso el precio del producto
def ingresa_precio():
    # Importa el Validaciones
    from productos import valida_numero_vacio, valida_flotante, valida_flotante_mayor_cero

    #
    while True:
        precio = input(f"{Style.BRIGHT} {Fore.LIGHTYELLOW_EX}\n Precio : {Style.BRIGHT} {Fore.WHITE}")

        # Valida el precio
        if (valida_numero_vacio(precio)):
            #
            if (valida_flotante(precio)):
                #
                if (valida_flotante_mayor_cero(precio)):
                    # Devuelve  la variable precio
                    return float(precio)

            else:
                #
                mostrar_mensaje("El precio debe ser un número con decimales...")

        else:
            #
            mostrar_mensaje(f"El precio debe ser un número mayor a cero...")

        limpia_error_mostrar_mensaje(8, 8)


# Ingreso de la cantidad del producto
def ingresa_categoria():
    # Importa el Validaciones 
    from productos import valida_texto_vacio, valida_largo_maximo    #

    #
    largo_maximo = 30

    # Valida el ingreso de descripcion
    while True:
        # Obtiene la categoria, eliminando los espacios a derecha es izquierda alltim()
        categoria = input(f"{Style.BRIGHT} {Fore.LIGHTYELLOW_EX}\n Categoria : {Style.BRIGHT} {Fore.WHITE}").strip().upper()

        #
        if (valida_texto_vacio(categoria)):
            #
            if (valida_largo_maximo(categoria, largo_maximo)):
                # Devuelve  la variable nombre
                return categoria

            else:
                #
                mostrar_mensaje(f"La categoria no puede ser mayor a {largo_maximo} caracteres...")

        else:
            #
            mostrar_mensaje(f"La categoria no puede estar vacia...")

        limpia_error_mostrar_mensaje(8, 8)


# Muestra el producto ingresado
def mostrar_producto_agregado( nombre, descripcion, cantidad, precio, categoria):
    # Muestra los datos del producto agregado
    print(f"{Style.BRIGHT} {Fore.YELLOW}\n Producto ingresado : ")
    print(f" - Nombre      : {nombre}")
    print(f" - Descripcion : {descripcion}")
    print(f" - Cantidad    : {cantidad}")
    print(f" - Precio      : {precio}")
    print(f" - Categoria   : {categoria}")


# Titulo de Agregar Productos
def mostrar_titulo_agregacion():
    # Importa desde Pantalla
    from pantalla import mostrar_linea_separacion
    
    mostrar_linea_separacion()
    print(f"{Style.BRIGHT}{Fore.CYAN}              Agregando Productos               \n")
    mostrar_linea_separacion()


# Agrega productos al Inventario
def agregar_productos():
    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_agregacion()

    # Muestra el encabezado de los datos a ingresar
    print(f"{Style.BRIGHT} {Fore.YELLOW}\n Datos del Producto a ingresar : ")

    # Variables que se utilizan para cargar el producto
    # Ingreso y validacion de la variable nombre
    nombre = ingresa_nombre()

    # Ingreso y validacion de la variable descripcion
    descripcion = ingresa_descripcion()

    # Ingreso y validacion de la variable cantidad
    cantidad = ingresa_cantidad()

    # Ingreso y validacion de la variable precio
    precio = ingresa_precio()

    # Ingreso y validacion de la variable categoria
    categoria = ingresa_categoria()

    # Agrega un producto
    agregado_existosamente = agregar_producto(nombre = nombre, descripcion = descripcion, cantidad = cantidad, precio = precio,
                                                categoria = categoria)

    #
    if (agregado_existosamente):
        # Muestra el producto ingresado
        mostrar_producto_agregado(nombre, descripcion, cantidad, precio, categoria)
        
        # Muestra un mensaje en pantalla
        mostrar_mensaje("Producto agregado exitosamente...")        

    else:
        # Muestra un mensaje en pantalla
        mostrar_mensaje("Hubo un error al agregar el producto...")        
