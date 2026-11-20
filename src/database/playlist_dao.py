import sqlite3
from src.database.db_conexion import obtener_conexion

def crear_playlist(nombre, descripcion, ruta_db=None):
    consulta = """
        INSERT INTO lista_reproduccion(nombre, descripcion) VALUES(?, ?)
        """
    try: 
        with obtener_conexion(ruta_db) as conexion:
            cursor = conexion.cursor()
            cursor.execute(consulta, (nombre, descripcion))
            fila = cursor.fetchone()  # Obtener la fila insertada
            conexion.commit()
            return fila["id"] if fila else None
    except sqlite3.Error as e:
        print(f"Error al crear la playlist: {e}")
        return None

def obtener_playlists(ruta_db=None):

    consulta = """
        SELECT
            p.id,
            p.nombre,
            p.descripcion,
            p.fecha_creacion,
            COUNT(pc.cancion_id) AS total_canciones
        FROM listas_reproduccion p
        LEFT JOIN playlist_canciones pc ON p.id = pc.playlist_id
        GROUP BY p.id
        ORDER BY p.nombre COLLATE NOCASE ASC;
    """
    try:
        with obtener_conexion(ruta_db) as conexion:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            filas = cursor.fetchall()
            return [dict(f) for f in filas]
    except sqlite3.Error as error:
        print(f"[Error DAO Playlists] Error al consultar listas de reproducción: {error}")
        return []

def obtener_playlist_por_id(playlist_id, ruta_db=None):
    consulta = """
        SELECT * FROM listas_reproduccion WHERE id = ?
            """
    try:
        with obtener_conexion(ruta_db) as conexion:
            cursor = conexion.cursor()
            cursor.execute(consulta, (playlist_id,))
            fila = cursor.fetchone()
            return dict(fila) if fila else None
    except sqlite3.Error as error:
        print(f"[Error DAO Playlists] Error al consultar la lista de reproducción por ID: {error}")
        return None

def agregar_cancion_a_playlist(playlist_id, cancion_id, orden=None, ruta_db=None):

    try:
        with obtener_conexion(ruta_db) as conexion:
            cursor = conexion.cursor()

            if orden is None:
                cursor.execute (
                    """
                        SELECT COALESCE(MAX(orden), 0) + 1 AS siguiente FROM playlist_canciones WHERE playlist_id = ?,
                    """
                    (playlist_id,)
                )
                fila_orden = cursor.fetchone()
                orden = fila_orden["siguiente"] if fila_orden else 1

            consulta = """
                    INSERT INTO playlist_canciones(playlist_id, cancion_id, orden)
                    VALUES(?, ?, ?)
                    ON CONFLICT(playlist_id, cancion_id) DO NOTHING;
                    """
            cursor.execute(consulta, (playlist_id, cancion_id, orden))
            conexion.commit()
            return cursor.rowcount > 0
    except sqlite3.Error as error:
        print(f"[Error DAO Playlists] Error al agregar canción a la lista de reproducción: {error}")
        return False


def obtener_canciones_de_playlist(playlist_id, ruta_db=None):
    """Recupera todas las canciones que pertenecen a una lista de reproducción, en su orden definido.

    Realiza un JOIN entre 'canciones' y 'playlist_canciones'.

    Parámetros:
        playlist_id (int): Identificador de la lista a consultar.
        ruta_db (str, opcional): Ruta a la base de datos SQLite.

    Retorna:
        list[dict]: Canciones pertenecientes a la lista ordenadas según su posición.
    """
    consulta = """
        SELECT
            c.id,
            c.titulo,
            c.artista,
            c.album,
            c.duracion,
            c.ruta,
            c.favorito,
            pc.orden
        FROM canciones c
        INNER JOIN playlist_canciones pc ON c.id = pc.cancion_id
        WHERE pc.playlist_id = ?
        ORDER BY pc.orden ASC;
    """
    try:
        with obtener_conexion(ruta_db) as conexion:
            cursor = conexion.cursor()
            cursor.execute(consulta, (playlist_id,))
            filas = cursor.fetchall()
            return [dict(f) for f in filas]
    except sqlite3.Error as error:
        print(f"[Error DAO Playlists] Error al obtener canciones de playlist {playlist_id}: {error}")
        return []


def eliminar_cancion_de_playlist(playlist_id, cancion_id, ruta_db=None):
    """Remueve una canción de una lista de reproducción sin eliminar el archivo ni la canción de la BD.

    Parámetros:
        playlist_id (int): Identificador de la lista.
        cancion_id (int): Identificador de la canción a desvincular.
        ruta_db (str, opcional): Ruta a la base de datos SQLite.

    Retorna:
        bool: True si fue removida, False si no formaba parte de la lista.
    """
    consulta = "DELETE FROM playlist_canciones WHERE playlist_id = ? AND cancion_id = ?;"
    try:
        with obtener_conexion(ruta_db) as conexion:
            cursor = conexion.cursor()
            cursor.execute(consulta, (playlist_id, cancion_id))
            conexion.commit()
            return cursor.rowcount > 0
    except sqlite3.Error as error:
        print(f"[Error DAO Playlists] Error al desvincular canción {cancion_id} de lista {playlist_id}: {error}")
        return False


def eliminar_playlist(playlist_id, ruta_db=None):
    """Elimina una lista de reproducción por completo.

    Las relaciones en 'playlist_canciones' se eliminan en cascada gracias a ON DELETE CASCADE.

    Parámetros:
        playlist_id (int): Identificador de la lista a eliminar.
        ruta_db (str, opcional): Ruta a la base de datos SQLite.

    Retorna:
        bool: True si la lista fue eliminada, False de lo contrario.
    """
    consulta = "DELETE FROM listas_reproduccion WHERE id = ?;"
    try:
        with obtener_conexion(ruta_db) as conexion:
            cursor = conexion.cursor()
            cursor.execute(consulta, (playlist_id,))
            conexion.commit()
            return cursor.rowcount > 0
    except sqlite3.Error as error:
        print(f"[Error DAO Playlists] Error al eliminar playlist ID {playlist_id}: {error}")
        return False
