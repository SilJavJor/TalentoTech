# Agregar Productos

# Importaciones
# Importa Colorama
from colorama import Style, Fore
# Importa desde el paquete de pantalla
from pantalla import limpiar_pantalla, mostrar_mensaje
# Importa desde datos
from gestor_base_datos import agregar_producto

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
    # Importa desde Pantalla
    from productos import ingresa_nombre, ingresa_descripcion, ingresa_cantidad, ingresa_precio, ingresa_categoria

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
