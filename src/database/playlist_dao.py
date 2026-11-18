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

def obtener_playlist_por_id(playlist_id, ruta_db=None):
    consulta = """

        SELECT 
        p.id,
        p.nombre,
        p.descripcion,
        p.fecha_creacion,

        COUNT(pc.cancion_id) AS total_canciones

        FROM lista_reproduccion p

        LEFT JOIN playlist_canciones pc ON p.id = pc.playlist_id

        GROUP BY p.id, p.nombre, p.descripcion, p.fecha_creacion
        
        ORDER BY p.nombre COLLECT NOCASE ASC;

        """
    try:
        with obtener_conexion(ruta_db) as conexion:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            fila = cursor.fetchone()
            return fila if fila else None

    except sqlite3.Error as e:
        print(f"Error al obtener la playlist: {e}")
        return None

