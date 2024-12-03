# Detectar las teclas precionadas

import keyboard

# Captura la opcion presionada por el usuario
def get_user_input_option():
    
    # Verifica que tecla fue flecha, enter o números ingresados por teclado
    #while True:
        if keyboard.is_pressed('up'):
            return 'up'
        elif keyboard.is_pressed('down'):
            return 'down'
        elif keyboard.is_pressed('enter'):
            return 'enter'
        elif keyboard.is_pressed('1'):
            return '1'
        elif keyboard.is_pressed('2'):
            return '2'
        elif keyboard.is_pressed('3'):
            return '3'
        elif keyboard.is_pressed('4'):
            return '4'
        elif keyboard.is_pressed('5'):
            return '5'
        elif keyboard.is_pressed('6'):
            return '6'
        elif keyboard.is_pressed('7'):
            return '7'
        elif keyboard.is_pressed('8'):
            return '8'
        elif keyboard.is_pressed('9'):
            return '9'