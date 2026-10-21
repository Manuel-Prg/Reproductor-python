# Reproductor de Música 🎵

Estructura modular del reproductor de música desarrollado en Python con **Tkinter** y **Pygame**.

## Estructura del Proyecto

```text
reproductor_musica/
│
├── assets/
│   ├── covers/
│   └── icons/
│
├── database/
│
├── src/
│   ├── __init__.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── styles.py
│   │
│   ├── database/
│   │   └── __init__.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   └── audio_player.py
│   │
│   └── ui/
│       ├── __init__.py
│       ├── app_gui.py
│       └── components/
│           ├── __init__.py
│           ├── navbar.py
│           ├── card_cancion.py
│           └── player_bar.py
│
├── docs/
│
├── main.py
├── requirements.txt
└── README.md
```

## Ejecución

1. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

2. Ejecutar la aplicación:
   ```bash
   python main.py
   ```
