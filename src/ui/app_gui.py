import os
import tkinter as tk
from tkinter import filedialog
from src.config.styles import COLOR_PURPLE, COLOR_BG, COLOR_CARD_BG, ICONS_DIR
from src.core.audio_player import AudioPlayer
from src.ui.components.card_cancion import CardCancion
from src.ui.components.player_bar import PlayerBar
from src.ui.components.navbar import Navbar

class APPMusicPlayer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Reproductor de musica")
        self.geometry("800x600")
        self.minsize(800, 600)
        self.configure(bg=COLOR_BG)

        self.icon_abrir_direct = tk.PhotoImage(file=os.path.join(ICONS_DIR, "folder_open.svg"))
        self.icon_folder = tk.PhotoImage(file=os.path.join(ICONS_DIR, "folder.svg"))
        self.icon_add = tk.PhotoImage(file=os.path.join(ICONS_DIR, "add.svg"))

        #estado del audio
        self.audio = AudioPlayer()
        self.reproduciendo = False
        self.cancion_actual = None
        self.canciones = []

        #1. Barra de superior
        self.navbar = Navbar(self)
        self.navbar.pack(side="top", fill="x")

        #2. Barra de acciones
        frame_hub = tk.Frame(self, bg=COLOR_BG, height=40)
        frame_hub.pack(fill="x", padx=25, pady=(15, 0))

        tk.Button(
            frame_hub,
            image=self.icon_abrir_direct,
            bg = COLOR_PURPLE,
            bd = 0,
            relief = "flat",
            cursor="hand2",
            command=self.abrir_directorio
        ).pack(side="right", padx=10)

        #3. Barra inferior de los controles
        self.player_bar = PlayerBar(
            self,
            on_toggle_play=self.toggle_play,
            on_volume=self.set_volume
        )
        self.player_bar.pack(side="bottom", fill="x")

        #4. contenedor central de las cards y de las carpetas

        self.frame_grid = tk.Frame(self, bg=COLOR_BG, padx=20, pady=20)
        self.frame_grid.pack(fill="both", expand=True, padx=25, pady=(15, 0))

        #mostramos el estado incial de la app
        self.actualizar_vista_canciones()

        def abrir_directorio(self):

            ruta = filedialog.askdirectory(title="Seleccionar carpeta de música")
            if not ruta:
                return

            formatos = (".mp3", ".wav", ".ogg", ".flac")
            self.canciones = []

            try: 
                for i, archivos in enumerate(os.listdir(ruta)):
                    if archivos.lower().endswith(formatos):
                        nombre = os.path.splitext(archivos)[0]
                        self.canciones.append(
                            {
                                "id": i,
                                "titulo": nombre,
                                "artistra": "Arvhivo Local",
                                "ruta": os.path.join(ruta, archivos)
                            }
                        )
            except Exception as e:
                print(f"hubo un error en leer el directorio seleccionado: {e}")

            self.actualizar_vista_canciones()

        def actualizar_vista_canciones(self):
            #limpiar el frame de las cards 

            for widget in self.frame_grid.winfo_children():
                widget.destroy()

            #si no hay canciones, mostramos un mensaje al usuario para agregar la carpeta de musica

            if not self.canciones:
                frame_vacio = tk.Frame(self.frame_grid, bg=COLOR_BG)
                frame_vacio.place(relx=0.5, rely=0.5, anchor="center")

                tk.Label(
                    frame_vacio, 
                    image = self.icon_folder,
                    bg = COLOR_BG   
                ).pack(pady=(0, 8))

                tk.Label(
                    frame_vacio, 
                    text = "No hay canciones disponibles.\nAgrega una carpeta de música para comenzar.",
                    font = ("Segoe UI", 12),
                    bg = COLOR_BG,  
                    fg = "FFFFFF"
                ).pack(pady=(0, 8))

                tk.Label(
                    frame_vacio, 
                    image = self.icon_add,
                    text = "agregue una ruta de Música.",
                    font = ("Segoe UI", 12),
                    bd=0,
                    pady=8,
                    padx=16,
                    cursor="hand2",
                    bg = COLOR_BG,  
                    fg = "FFFFFF"
                ).pack(pady=(0, 8))

                tk.Button(
                    frame_vacio,
                    image = self.icon_abrir_direct,
                    bg = COLOR_PURPLE,
                    bd = 0,
                    relief = "flat",
                    cursor="hand2",
                    command=self.abrir_directorio
                ).pack()
                return

        columnas  = 4

        for idx, cancion in enumerate(self.canciones):
            f = idx // columnas
            c = idx // columnas
            card = CardCancion(self.frame_grid, cancion, self.reproduciendo)
            card.grid(row=f, column=c, padx=10, pady=10, sticky="nsew")

        for c in range(columnas):
            self.frame_grid.grid_columnconfigure(c, weight=1)

        filas = (len(self.canciones) + columnas - 1) // columnas

        for f in range(filas):
            self.frame_grid.grid_rowconfigure(f, weight=1)

    def reproducir_cancion(self, cancion):
        self.cancion_actual = cancion
        self.reproduciendo = True
        self.audio.reproducir(cancion["ruta"])
        self.player_bar.set_play_icon(True)


    def toggle_play(self):

        if not  self.cancion_actual and self.canciones:
            self.reproducir_cancion(self.canciones[0])
            return

        if not self.reproduciendo:
            self.reproduciendo = True
            self.player_bar.set_play_icon(True)
            self.audio.reanudar()
        else:
            self.reproduciendo = False
            self.player_bar.set_play_icon(False)
            self.audio.pausar()

AppGui = APPMusicPlayer    