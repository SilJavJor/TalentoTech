# Main
# Programa Principal

# Importaciones
# Importa Colorama (Libreria para dar colores, fuentes y fondos)
from colorama import init
# Importa desde Base de Datos
from gestor_base_datos import verifica_directorio_base_datos, DIRECTORIO_BASE_DATOS, BASE_DATOS
# Importa Inventario
from inventory import inventario

# Inicializa Colorama con autoreset
init(autoreset=True)


#
print("Iniciando el programa...")

#verifica_directorio_base_datos()
# Verificar si existe la base de datos o crearla
#verifica_base_datos(BASE_DATOS)


"""
Punto de entrada principal del programa.
"""
# Menu del inventario
if __name__ == "__main__":
    inventario()