import tkinter as tk

def create_main_window():
    """Crea la ventana principal y configura su tamaño y posición."""
    root = tk.Tk()
    root.title("Menú Centralizado")

    # Obtener el tamaño de la pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana
    window_width = 300
    window_height = 200
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Configurar el tamaño y la posición de la ventana
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    return root
