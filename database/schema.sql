PRAGMA foreign_keys = ON;

CREATE TABLE
    IF NOT EXISTS canciones (
        id INTERGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        artista TEXT DEFAULT 'Archivo Local',
        album TEXT DEFAULT 'Desconocido',
        duracion TEXT DEFAULT '0:00',
        ruta TEXT NOT NULL UNIQUE,
        favorito INTERGER DEFAULT 0,
        fecha_agregado TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

CREATE TABLE
    IF NOT EXISTS lista_reproduccion (
        id INTERGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL UNIQUE,
        descripcion TEXT DEFAULT '',
        fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

CREATE TABLE
    IF NOT EXISTS Playlist_canciones (
        id INTERGER PRIMARY KEY AUTOINCREMENT,
        playlist_id INTERGER NOT NULL,
        canciones_id INTERGET NOT NULL,
        orden INTERGER DEFAULT 0,
        fecha_agregado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (playlist_id) REFERENCES lista_reproduccion (id) ON DELETE CASCADE,
        FOREIGN KEY (cancion_id) REFERENCES canciones (id) ON DELETE CASCADE,
        UNIQUE (playlist_id, cancion_id)
    );

CREATE TABLE
    IF NOT EXISTS historial_reproduccion (
        id INTERGER PRIMARY KEY AUTOINCREMENT,
        cancion_id INTERGER NOT NULL,
        fecha_reproduccion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (cancion_id) REFERENCES canciones (id) ON DELETE CASCADE
    );

CREATE INDEX IF NOT EXISTS idx_canciones_titulo ON canciones (titulos);
CREATE INDEX IF NOT EXISTS idx_canciones_favorito ON canciones (favoritos);
CREATE INDEX IF NOT EXISTS idx_playlist_canciones_lista ON playlist_canciones (playlist_id);