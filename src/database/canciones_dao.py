import sqlite3
from src.database.db_conexion import obtener_conexion

def insertar_o_actualizar_cacion():
    consulta = """
            INSERT INTO canciones (titulo, artista, album, duracion, ruta, favorito)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(ruta) DO UPDATE SET
            titulo = excluded.titulo,
            artista = excluded.artista,
            album = excluded.album,
            duracion = excluded.duracion,
            favorito = excluded.favorito;

            RETURTNING id;
            """
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(consulta, (titulo, artista, album, duracion, ruta, favorito))    
            fila = cursor.fetchone()
            conexion.commit()
            return fila[0] if fila else None
        
    except sqlite3.Error as e:
        print(f"[Error de tipo DAO canciones] No se pudo inssertar o actualizar la canción: {e}")
        return None

def sincronizar_canciones_carpeta(lista_canciones, ruta_db = None):
    consulta = """
        INSERT INTO canciones (titulo, artista, album, duracion, ruta, favorito)
                    VALUES (?, ?, ?, ?, ?, ?)
                    ON CONFLICT(ruta) DO UPDATE SET
                    titulo = excluded.titulo,
                    artista = excluded.artista,
                    
                """
    procesados = 0

    try:
        with obtener_conexion(ruta_db) as conexion:
            cursor = conexion.cursor()
            for cancion in lista_canciones:
                cursor.execute(consulta, (
                    cancion.get("titulo", "Sin título"),
                    cancion.get("artista", "Archivo Local"),
                    cancion.get("album", "Desconocido"),
                    cancion.get("duracion", "0:00"),
                    cancion.get("ruta")
                ))
                procesados += 1
            conexion.commit()
    except sqlite3.Error as error:
        print(f"[Error DAO Canciones] Error durante la sincronización masiva: {error}")

    return procesados

def obtener_todas_las_canciones(ruta_db= None):
    consulta = "SELECT * FROM canciones ORDER BY fecha_agregado DESC"

    try:
          with obtener_conexion(ruta_db) as conexion:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            filas = cursor.fetchall() 
            return [dict(f) for f in filas]
    except sqlite3.Error as error:
        print(f"[Error DAO Canciones] Error al obtener todas las canciones: {error}")
        return []

def obtener_cancion_por_id(cancion_id, ruta_db = None):
      
    consulta = "SELECT * FROM canciones WHERE id = ? LIMIT 1;"
    try:
        with obtener_conexion(ruta_db) as conexion:
            cursor = conexion.cursor()
            cursor.execute(consulta, (cancion_id,))
            fila = cursor.fetchone()
        return dict(fila) if fila else None
    
    except sqlite3.Error as error:
        print(f"[Error DAO Canciones] Error al buscar canción con ID {cancion_id}: {error}")
    return None
