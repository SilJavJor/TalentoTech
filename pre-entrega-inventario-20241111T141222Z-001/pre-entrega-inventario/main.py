# Main


# Archivo  -->  Pantalla
# Importa libreria del Sistema Operativo
import os


# Archivo  -->  Inventario
# Variable que se utiliza para la carga del inventario
inventario = []


# Archivo  -->  Inventario
# Variable que se utiliza para el ingreso de la opcion del menu
opcion_ingresada = '1'


# Archivo  -->  Pantalla
# Limpia de la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


# Archivo  -->  Inventario
# Muestra el titulo del sistema
def mostrar_titulo():
    print("====   Sistema de Inventario   ====\n")


# Archivo  -->  Menu
# Muestra las opciones de las teclas de la opcion del menu
def mostrar_teclas_ayuda_menu():
    print("\n\n Presione el número correspondiente para seleccionar.")
    print(" Presione '9' para Salir.")


# Archivo  -->  Menu
# Muestra la ayuda de los items del menu
def mostrar_ayuda_menu(id_opcion):
    print(f"\n Ayuda: {opciones_menu[id_opcion][3]}\n")


# Archivo  -->  Menu
# Muestra el menu
def mostrar_menu(opcion_ingresada):
    # Limpia la pantalla
    limpiar_pantalla()

    # Muestra el titulo de la aplicación
    mostrar_titulo()

    id_opcion = 0
    indice = 0 

    while (indice < len(opciones_menu)):

        # Muestra en pantalla la opcion del menu
        if (opciones_menu[indice][1] == int(opcion_ingresada)):

            print(f"> {opciones_menu[indice][2]}")
            id_opcion = indice 

        else: 

            print(f"  {opciones_menu[indice][2]}")

        # Actualizacion del indice
        indice += 1

    # Muestra las opciones de teclas
    mostrar_teclas_ayuda_menu()

    # Muestra la ayuda del menu
    mostrar_ayuda_menu(id_opcion)


# Salida de la aplicación
def salida_aplicacion():
    # Muestra un mensaje en pantalla
    mostrar_mensaje("Saliendo de la aplicación...")

    # Limpia la Pantalla
    limpiar_pantalla()


# Archivo  -->  Productos
# Opciones del menú
# id_lista, id_opcion, item, ayuda
opciones_menu = [
    [0, 1, " 1 - Agregar Productos   ", "Agrega un Producto"],
    [1, 2, " 2 - Modificar Productos ", "Modifica un Producto"],
    [2, 3, " 3 - Eliminar Productos  ", "Elimina un Producto"],
    [3, 4, " 4 - Buscar Productos    ", "Busca un Producto"],
    [4, 5, " 5 - Listar Productos    ", "Lista todos los Productos"],
    [5, 0, " ----------------------- ", ""],
    [6, 9, " 9 - Salir               ", "Salir de la Aplicación"]
]


# Muestra un mensaje en pantalla
def mostrar_mensaje(mensaje):
    #
    if (mensaje != ''):
        print(f"\n\n {mensaje}")

    # 
    input("\n Presione cualquier tecla para continuar...")


# Archivo  -->  Productos
# Titulo de Agregar Productos
def mostrar_titulo_agregacion():
    print("====   Agregando Productos  ====\n")


# Archivo  -->  Productos
# Titulo de Modificar Productos
def mostrar_titulo_modificacion():
    print("====   Modificando Productos  ====\n")


# Archivo  -->  Productos
# Titulo de Eliminar Productos
def mostrar_titulo_eliminacion():
    print("====   Eliminando Productos  ====\n")


# Archivo  -->  Productos
# Titulo de Buscar Productos
def mostrar_titulo_busquedas():
    print("====   Buscar Productos  ====\n")


# Archivo  -->  Productos
# Titulo de Listar Productos
def mostrar_titulo_listados():
    print("====   Listado Productos  ====\n")#

# Archivo  -->  Productos
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
                print(" El nombre no puede ser mayor a 50 caracteres....")

        else:

            #
            print(" El nombre no pude estar vacio...")


# Archivo  -->  Productos
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


# Archivo  -->  Productos
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


# Archivo  -->  Productos
# Agrega productos al Inventario
def agregar_productos():
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
    inventario.append(producto)

    # Se informa el producto ingresado
    print(f"\n\n Producto ingresado:\n - Nombre: {nombre}\n - Cantidad: {cantidad}\n - Precio: {precio}")
    
    # Muestra un mensaje en pantalla
    mostrar_mensaje("Producto agregado exitosamente.")


# Archivo  -->  Productos
# Modificar Productos
def modificar_productos():
    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_modificacion()

    # Muestra un mensaje en pantalla
    mostrar_mensaje("Opción no implementada...")


# Archivo  -->  Productos
# Eliminar Productos
def eliminar_productos():
    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_eliminacion()

    # Muestra un mensaje en pantalla
    mostrar_mensaje("Opción no implementada...")


# Archivo  -->  Productos
# Buscar Productos
def buscar_productos():
    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_busquedas()

    # Muestra un mensaje en pantalla
    mostrar_mensaje("Opción no implementada...")


# Archivo  -->  Productos
# Listado de Productos por pantalla
def listar_productos():
    # Limpiar pantalla
    limpiar_pantalla()

    # Muestra el titulo para la ventana de Agregacion
    mostrar_titulo_listados()

    # Verificar que el inventario no se encuentre vacio
    if (len(inventario) == 0):

        # Muestra un mensaje en pantalla
        mostrar_mensaje("No hay productos para mostrar.")

    else:

        # Inicializacion del indice
        indice = 0

        #
        while (indice < len(inventario)):
            # Se imprime el detalle de cada producto
            print(f" Producto : {inventario[indice]['nombre']}, Cantidad : {inventario[indice]['cantidad']}, Precio : {inventario[indice]['precio']}")

            # Actualizacion del indice
            indice += 1

        # Se imprime el detalle de cada producto
        print(f"\n\n Cantidad Total de Productos : {(len(inventario))}")

        # Muestra un mensaje en pantalla
        mostrar_mensaje("")


# Archivo  -->  Productos
# Maneja y ejecuta las opciones del menu
def manejar_opciones(opcion_ingresada):
    if opcion_ingresada == '1':

        # Agregar Productos
        agregar_productos()

    elif opcion_ingresada == '2':

        # Modificar Productos
        modificar_productos()

        
    elif opcion_ingresada == '3':

        # Eliminar Productos
        eliminar_productos()

    elif opcion_ingresada == '4':

        # Buscar Productos
        buscar_productos()

    elif opcion_ingresada == '5':

        # Listar Productos
        listar_productos()

    else:

        # Muestra un mensaje en pantalla
        mostrar_mensaje("Opción inválida....")
        opcion_ingresada = 0

# Archivo  -->  Inventario
while True:
    # Muestra el menu en pantalla
    mostrar_menu(opcion_ingresada)

    # Caputura el ingreso del teclado
    opcion_ingresada = input("\n Seleccione una opción: ").lower()

    if (opcion_ingresada == '9'):

        # Salir de la aplicacion
        salida_aplicacion()

        break

    elif ((opcion_ingresada > '0') and (opcion_ingresada < str(len(opciones_menu)))):

        # Accede a las funciones de Carga, Modificacion, Eliminacion, Busqueda 
        # y Listados de Productos
        manejar_opciones(opcion_ingresada)

    else:

        # Muestra un mensaje en pantalla
        mostrar_mensaje("Opción inválida...")
        opcion_ingresada = 0
