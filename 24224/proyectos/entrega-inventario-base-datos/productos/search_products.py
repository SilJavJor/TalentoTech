# Search Products

# Importaciones
# Importa desde Colorama
from colorama import Style, Fore
# Importa desde el paquete de pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje, limpia_mostrar_mensaje
# Importa desde datos
from gestor_base_datos import leer_producto

# Ingreso el identificador del producto
def ingresa_identificador(texto_funcion):
    # Importa el Validaciones
    from productos import valida_numero_vacio, valida_entero, valida_entero_mayor_cero

    #   
    while True:
        # Obtiene la cantidad en entero
        identificador = input(f"{Style.BRIGHT} {Fore.LIGHTYELLOW_EX}\n ID a {texto_funcion} : {Style.BRIGHT} {Fore.WHITE}")

        # Valida la cantidad
        if (valida_numero_vacio(identificador)):
            #
            if (valida_entero(identificador)):
                #
                if (valida_entero_mayor_cero(identificador)):
                    # Devuelve  la variable identificador
                    return int(identificador)

            else:
                #
                mostrar_mensaje(f"La identificador debe ser un número entero...")

        else:
            #
            mostrar_mensaje(f"La identificador debe ser un número mayor a cero...")

        limpia_mostrar_mensaje(8, 8)


# Funcion para buscar productos
def buscar_productos(texto_funcion):
    # Muestra el encabezado de los datos a ingresar
    print(f"{Style.BRIGHT} {Fore.YELLOW}\n Datos del Producto : ")

    # Variables que se utilizan para cargar el producto
    # Ingreso y validacion de la variable identificador
    identificador = ingresa_identificador(texto_funcion)
    
    # Busca un producto
    producto = leer_producto(identificador)

    #
    if (producto):

        return producto

    else:

        return []
