# Main
# Programa Principal

# Importaciones
from colorama import init
from inventory import inventario


# Inicializa Colorama con autoreset
init(autoreset=True)


# Menu del inventario
if __name__ == "__main__":
    inventario()