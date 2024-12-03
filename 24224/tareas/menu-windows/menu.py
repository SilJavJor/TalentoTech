import tkinter as tk

def create_menu(root, show_message, exit_program):
    """Crea y configura el menú de la ventana principal."""
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    # Agregar un menú desplegable
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Archivo", menu=file_menu)
    
    file_menu.add_command(label="Opción 1", command=show_message)
    file_menu.add_command(label="Opción 2", command=show_message)
    file_menu.add_separator()
    file_menu.add_command(label="Salir", command=exit_program)

    # Agregar submenú
    sub_menu = tk.Menu(file_menu, tearoff=0)
    file_menu.add_cascade(label="Submenú", menu=sub_menu)
    sub_menu.add_command(label="Subopción 1", command=show_message)
    sub_menu.add_command(label="Subopción 2", command=show_message)
