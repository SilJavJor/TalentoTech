from tkinter import messagebox

def show_message():
    """Muestra un mensaje de información."""
    messagebox.showinfo("Opción seleccionada", "Has seleccionado una opción del menú")

def exit_program():
    """Termina la aplicación."""
    import tkinter as tk
    root = tk.Tk()
    root.quit()
    root.destroy()
