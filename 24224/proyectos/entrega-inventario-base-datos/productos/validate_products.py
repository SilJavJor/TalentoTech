# Validaciones de productos 

# Valida si el texto esta vacio 
def valida_texto_vacio( texto = ""):
    #
    if (texto):
        #
        return True

    return False


# Valida el largo minimo 
def valida_largo_minimo(texto = "", largo_minimo = 1):
    #
    if (len(texto) >= int(largo_minimo)):
        #
        return True

    return False


# Valida el largo maximo
def valida_largo_maximo(texto = "", largo_maximo = 1):
    #
    if (len(texto) <= int(largo_maximo)):
        #
        return True

    return False


# Valida si no esta vacio y si es mayor a cero
def valida_numero_vacio(numero):
    # Verifica que no este vacio
    if (numero):
        #
        return True

    return False


# Intenta convertir a entero 
# Valida si es un entero
def valida_entero(entero):
    #
    try:
        # Intenta convertir a entero
        int(entero)

        return True

    except ValueError:
        #
        return False


# Valida si el numero entero mayor a cero
def valida_entero_mayor_cero(numero):
    # Verifica que no este vacio
    if (numero):
        # Verifica que sea mayor a cero
        if (int(numero) > int(0)):
            #
            return True

    return False


# Intenta convertir a entero 
# Valida si es un entero
def valida_flotante(flotante):
    #
    try:
        # Intenta convertir a entero
        float(flotante)

        return True

    except ValueError:
        #
        return False


# Valida si el numero flotante mayor a cero
def valida_flotante_mayor_cero(flotante):
    # Verifica que no este vacio
    if (flotante):
        # Verifica que sea mayor a cero
        if (float(flotante) > float(0)):
            #
            return True

    return False
