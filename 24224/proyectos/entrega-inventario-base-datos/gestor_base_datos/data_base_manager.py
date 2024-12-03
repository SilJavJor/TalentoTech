# Conexion

# Importaciones
# Importa desde SqLite
import sqlite3
# Importa desde Os
#import os
# Importa desde Screen funciones independientes para el manejo de la pantalla
from pantalla import mostrar_mensaje
# Importa desde Base de Datos
from gestor_base_datos import DATA_BASE, DIRECTORIO_BASE_DATOS


# Verificar que el directorio exista
#os.makedirs(directorio, exist_ok = True)
# Asegurarse de que el directorio existe
#if not os.path.exists(DIRECTORIO_BASE_DATOS):
    
#    os.makedirs(DIRECTORIO_BASE_DATOS)



def verifica_directorio_base_datos(cnn):
    #
    if (cnn):
        #
        return True

    #
    return False

def conectar():
    #
    try:
        # Conectar a la base de datos SQLite
        #conn = sqlite3.connect(DATA_BASE)
        cnn = sqlite3.connect(DATA_BASE)

        #
        return cnn

    except sqlite3.Error:

        #
        #mostrar_mensaje(f" Error al conectar con la base de datos : {nombre_base_datos}")
        mostrar_mensaje(f" Error al conectar con la base de datos : {DATA_BASE}")

        #
        return None


def desconectar(cnn):
    #
    if not (cnn):
        # Desconectar de la base de datos
        cnn.close()


def verifica_conexion(cnn):
    #
    if (cnn):
        #
        return True

    #
    return False


def guardar_cambios(cnn):
    #
    #if (conn):
    if verifica_conexion(cnn):
        # Hace Commit en la base de datos
        cnn.commit()


def guardar_cambios_desconectar(cnn):
    #
    if verifica_conexion(cnn):
        # 
        guardar_cambios(cnn)

        # 
        desconectar(cnn)
