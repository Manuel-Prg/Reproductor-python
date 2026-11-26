import os
import tkinter as tk
from tkinter import tk
from tkinter import filedialog
from src.config.styles import (
    COLOR_BG,
    COLOR_NAVBAR_BG,
    COLOR_PURPLE,
    COLOR_PURPLE_LIGHT,
    DB_PATH,
    ICONS_DIR,
)
from src.core.audio_player import AUDIO


class configDialog(tk.Toplevel):
    def __init__(self, master, total_caciones=0, total_favoritos=0, total_playlists=0, on_select_folder=None):

        super().__init__(master)
        self.title("Configuración")
        self.geometry("460x300")
        self.resizable(False, False)
        self.configure(bg=COLOR_BG)

        self.transient(master)
        self.grab_set()

        self.on_select_folder = on_select_folder
        self._construir_ui(total_caciones, total_favoritos, total_playlists)

    def _construir_ui(self, total_caciones, total_favoritos, total_playlists):

        #encabrado del dialogo
        header = tk.Frame(self, bg=COLOR_PURPLE, height=50, padx=10, pady=10)
        header.pack(fill="X")

        tk.Label(
            header,
            text="configuración del reproductor",
            bg=COLOR_PURPLE,
            fg="#FFFFFF",
            font=("Arial", 14, "bold"),
        ).pack(anchor="w")

        #cuerpo del dia(logo
        body = tk.Frame(self, bg=COLOR_NAVBAR_BG, padx=18, pady=18)
        body.pack(fill="both", expand=True, padx=16, pady=16)

        estado_audio = "ACTIVO (pygame Mixter)" if AUDIO else "No disponible"

        self._agregar_fila_info(body, "Motor de audio:", estado_audio)
        self._agregar_fila_info(body, "Canciones en la biblioteca",str(total_caciones))
        self._agregar_fila_info(body, "Favoritos en la biblioteca",str(total_favoritos))
        self._agregar_fila_info(body, "total de playlist en la biblioteca",str(total_playlists))
        self._agregar_fila_info(body, "Base de datos SQlite", DB_PATH, wrap=260)

        acciones = tk.Frame(self, bg=COLOR_BG)
        acciones.pack(fill="x", padx=16, pady=(0,14))

        if self.on_select_folder:
            self.icon_folder = tk.PhotoImage(
                file=os.path.join(ICONS_DIR, "folder_open.png"))
'''
            btn_carpeta = tk.Button( 
                                bg = COLOR_PURPLE,
                                bd = 0,
                                relief = "flat",
                                cursor="hand2",
                                command=self.abrir_directorio,
                                ).pack(side="right", padx=10)


                    
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


'''



