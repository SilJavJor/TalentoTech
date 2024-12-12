# Agregar Productos

# Importaciones
# Importa Colorama
from colorama import Style, Fore
# Importa desde datos
from gestor_base_datos import agregar_producto
# Importa desde el paquete de pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje, limpia_mostrar_mensaje


# Ingresa el nombre
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

        limpia_mostrar_mensaje(8, 8)


# Ingreso la descripcion
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

        limpia_mostrar_mensaje(8, 8)


# Ingreso la cantidad
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

        limpia_mostrar_mensaje(8, 8)


# Ingreso el precio
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

        limpia_mostrar_mensaje(8, 8)


# Ingreso la categoria
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

        limpia_mostrar_mensaje(8, 8)
