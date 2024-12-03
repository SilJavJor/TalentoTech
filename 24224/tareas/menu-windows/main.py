from ui import create_main_window
from menu import create_menu
from functions import show_message, exit_program

def main():
    """Función principal para ejecutar la aplicación."""
    root = create_main_window()
    create_menu(root, show_message, exit_program)
    root.mainloop()

if __name__ == "__main__":
    main()

