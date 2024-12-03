# Lista para almacenar productos
clientes = []

def agregar_clientes():
    print("====   Agregar Clienete   ====\n")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))

    cliente = {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }

    clientes.append(cliente)
    print("\nProducto agregado exitosamente.")
    input("\nPresione Enter para volver al menú principal...")

#def modificar_clientes():


#def eliminar_clientes():


#def buscar_clientes():


def listar_clientes():
    print("====   Listado de Clientes   ====\n")

    if not clientes:
        print("No hay productos para mostrar.")
    else:
        for idx, cliente in enumerate(clientes):
            print(f"{idx + 1}. Nombre: {cliente['nombre']}, Precio: {cliente['precio']}, Cantidad: {cliente['cantidad']}")

    input("\nPresione Enter para volver al menú...")
