# AGENTS.md — Contexto de Arquitectura y Aprendizaje

## 1. Propósito y Enfoque Pedagógico
Este proyecto es un reproductor multimedia de escritorio modular desarrollado en Python, orientado a aplicar:
- Programación Orientada a Objetos (POO): Clases, abstracción, separación de responsabilidades y encapsulamiento.
- Patrón DAO (Data Access Object) con persistencia local en SQLite.
- Motor de sonido con Pygame Mixer.
- Interfaz gráfica moderna y modular construida sobre Tkinter.

> **Pauta para el Asistente:** No entregues código resuelto directamente. Guía al usuario mediante conceptos, pistas sobre flujos de ejecución, inspección de variables y firmas de métodos para fortalecer su aprendizaje y depuración autónoma.

---

## 2. Estructura Real del Proyecto

```text
reproductor/
├── .github/
│   └── copilot-instructions.md   # Instrucciones del tutor para Copilot
├── assets/                       # Iconos, imágenes y recursos estáticos
├── database/                     # Scripts DDL y archivo de base de datos
│   ├── reproductor.db
│   └── schema.sql
├── docs/                         # Documentación del proyecto
├── src/
│   ├── config/
│   │   └── styles.py             # Constantes de colores, fuentes y medidas de la UI
│   ├── core/
│   │   └── audio_player.py       # Controlador del ciclo de vida de pygame.mixer
│   ├── database/
│   │   ├── db_connection.py      # Conexión/desconexión segura a SQLite (Context Manager)
│   │   ├── canciones_dao.py      # Operaciones CRUD para la tabla de canciones
│   │   └── playlist_dao.py       # Operaciones CRUD para las listas de reproducción
│   └── ui/
│       ├── components/           # Widgets compuestos derivados de tk.Frame
│       │   ├── card_cancion.py   # Tarjeta visual para listar una canción
│       │   ├── navbar.py         # Menú/barra de navegación lateral o superior
│       │   └── player_bar.py     # Controles inferiores (play, pausa, sliders, tiempo)
│       └── app_gui.py            # Ventana principal (orquesta componentes y vistas)
├── AGENTS.md                     # Este archivo de arquitectura
├── main.py                       # Punto de entrada (instancia App y arranca mainloop)
├── README.md
└── requirements.txt