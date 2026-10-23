
import os
import sqlite3
from src.config.styles import  BASE_DIR, DB_PATH

def obtener_conexion():

    if ruta_db is None:
        ruta_db = DB_PATH

    directorio = os.path.dirname(ruta_db)

    if directorio and not os.path.exists(directorio):
        os.makedirs(directorio, exist_ok=True)

    conexion = sqlite3.connect(ruta_db)

    conexion.row_factory = sqlite3.Row

    conexion.execute("PRAGMA foreign_keys = ON;")

    return conexion

def inicializar_base_de_datos(ruta_db = None):

    ruta_schema = os.path.join(BASE_DIR, "database", "schema.sql")

    try:
        with obtener_conexion(ruta_db) as conexion:
            cursor = conexion.cursor()


            if os.path.exits(ruta_schema):
                with open (ruta_schema, "r", encoding="utf-8") as archivo_sql:
                    script_sql = archivo_sql.read()
                cursor.executescript(script_sql)
            else:
                cursor.executescript(
                    """
                        PRAGMA foreign_keys = ON;

                        CREATE TABLE IF NOT EXISTS canciones (
                            id INTERGER PRIMARY KEY AUTOINCREMENT,
                            titulo TEXT NOT NULL,
                            artista TEXT DEFAULT 'Archivo Local',
                            album TEXT DEFAULT 'Desconocido',
                            duracion TEXT DEFAULT '0:00' ,
                            ruta TEXT NOT NULL UNIQUE,
                            favorito INTERGER DEFAULT 0,
                            fecha_agregado TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        );

                        CREATE TABLE IF NOT EXISTS lista_reproduccion(
                            id INTERGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT NOT NULL UNIQUE,
                            descripcion TEXT DEFAULT '',
                            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                         );

                        CREATE TABLE IF NOT EXISTS Playlist_canciones(
                            id INTERGER PRIMARY KEY AUTOINCREMENT,
                            playlist_id INTERGER NOT NULL,
                            canciones_id INTERGET  NOT NULL,
                            orden INTERGER DEFAULT 0,
                            fecha_agregado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            FOREIGN KEY (playlist_id) REFERENCES lista_reproduccion (id) ON DELETE CASCADE,
                            FOREIGN KEY (cancion_id) REFERENCES canciones (id) ON DELETE CASCADE,
                            UNIQUE (playlist_id, cancion_id)
                        );

                        CREATE TABLE IF NOT EXISTS historial_reproduccion(
                            id INTERGER PRIMARY KEY AUTOINCREMENT,
                            cancion_id INTERGER NOT NULL,
                            fecha_reproduccion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            FOREIGN KEY (cancion_id) REFERENCES canciones (id) ON DELETE CASCADE
                        );

                        CREATE INDEX IF NOT EXISTS idx_canciones_titulo ON canciones(titulos);
                        CREATE INDEX IF NOT EXISTS idx_canciones_favorito ON canciones(favoritos);
                    """
                )
            conexion.commit()
            return True

    except sqlite3.Error as error:
        print(f"[Error de DB] Falló la inicialización de la Base de Datos: {error}")
    return False
