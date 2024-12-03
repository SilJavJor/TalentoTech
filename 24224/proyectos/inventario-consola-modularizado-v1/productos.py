#

from opcion_no_implementada import opcion_no_implementada

# Lista para almacenar productos
productos = []

def agregar_productos():
    print("====   Agregar Producto   ====\n")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))

    producto = {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }

    productos.append(producto)
    print("\nProducto agregado exitosamente.")
    input("\nPresione Enter para volver al menú principal...")

def modificar_productos():
    # Muestra el mensaje de opción no implementada
    opcion_no_implementada()

def eliminar_productos():
    # Muestra el mensaje de opción no implementada
    opcion_no_implementada()

def buscar_productos():
    # Muestra el mensaje de opción no implementada
    opcion_no_implementada()

def listar_productos():
    print("====   Listado de Productos   ====\n")

    if not productos:
        print("No hay productos para mostrar.")
    else:
        for idx, producto in enumerate(productos):
            print(f"{idx + 1}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

    input("\nPresione Enter para volver al menú...")
