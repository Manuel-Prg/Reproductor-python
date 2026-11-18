"""Ejercicio de implementación del DAO para listas de reproducción.

Complete los métodos utilizando SQLite y la función obtener_conexion.
"""

import sqlite3
from src.database.db_connection import obtener_conexion


def crear_playlist(nombre, descripcion="", ruta_db=None):
    """Crea una nueva lista de reproducción.

    Parámetros:
        nombre (str): Nombre único de la lista.
        descripcion (str, opcional): Descripción de la lista.
        ruta_db (str, opcional): Ruta a la base de datos SQLite.

    Retorna:
        int | None: ID de la nueva lista, o None si no pudo crearse.

    TODO:
        Inserte el nombre y la descripción en listas_reproduccion.
        Valide los valores que recibe y aplique commit.
        Capture sqlite3.Error y devuelva None ante un error.
    """
    pass

def obtener_playlist_por_id(playlist_id, ruta_db=None):
    """Obtiene una lista de reproducción por su ID.

    Parámetros:
        playlist_id (int): Identificador de la lista.
        ruta_db (str, opcional): Ruta a la base de datos SQLite.

    Retorna:
        dict | None: Datos de la lista o None si no existe.

    TODO:
        Consulte listas_reproduccion usando un parámetro enlazado.
        Capture sqlite3.Error y devuelva None ante un error.
    """
    pass


#tarea
def agregar_cancion_a_playlist(playlist_id, cancion_id, orden=None, ruta_db=None):
    """Asocia una canción existente a una lista de reproducción.

    Si orden es None, la canción se agrega al final de la lista.

    Parámetros:
        playlist_id (int): ID de la lista destino.
        cancion_id (int): ID de la canción.
        orden (int, opcional): Posición deseada en la lista.
        ruta_db (str, opcional): Ruta a la base de datos SQLite.

    Retorna:
        bool: True si se agregó; False si ya existía o ocurrió un error.

    TODO:
        Calcule el siguiente orden cuando no se proporcionó uno.
        Inserte la asociación evitando duplicados.
        Capture sqlite3.Error y devuelva False ante un error.
    """
    pass

#tarea
def obtener_canciones_de_playlist(playlist_id, ruta_db=None):
    """Obtiene las canciones de una playlist en su orden definido.

    Parámetros:
        playlist_id (int): Identificador de la lista.
        ruta_db (str, opcional): Ruta a la base de datos SQLite.

    Retorna:
        list[dict]: Canciones pertenecientes a la lista, ordenadas por posicion.

    TODO:
        Una canciones con playlist_canciones mediante INNER JOIN.
        Filtre por playlist_id y ordene por el campo orden ascendente.
        Capture sqlite3.Error y devuelva una lista vacía ante un error.
    """
    pass

#intento 
def eliminar_cancion_de_playlist(playlist_id, cancion_id, ruta_db=None):
    """Desasocia una canción de una lista sin eliminar la canción.

    Parámetros:
        playlist_id (int): Identificador de la lista.
        cancion_id (int): Identificador de la canción.
        ruta_db (str, opcional): Ruta a la base de datos SQLite.

    Retorna:
        bool: True si se removió; False si no formaba parte de la lista.

    TODO:
        Elimine únicamente la relación correspondiente a ambos IDs.
        Capture sqlite3.Error y devuelva False ante un error.
    """
    pass

#intento
def eliminar_playlist(playlist_id, ruta_db=None):
    """Elimina una lista de reproducción por completo.

    Las relaciones asociadas deben eliminarse mediante ON DELETE CASCADE.

    Parámetros:
        playlist_id (int): Identificador de la lista.
        ruta_db (str, opcional): Ruta a la base de datos SQLite.

    Retorna:
        bool: True si la lista fue eliminada; False de lo contrario.

    TODO:
        Elimine la playlist por su ID.
        Capture sqlite3.Error y devuelva False ante un error.
    """
    pass
