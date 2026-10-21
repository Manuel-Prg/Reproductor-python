import os
import tkinter as tk
from src.config.styles import COLOR_CARD_BG, ICONS_DIR

class CardCancion(tk.Frame):

    _icon_play = None

    def __init__( self, root, cancion, onplay, on_favorite):
        super().__init__(root,bg = COLOR_CARD_BG, bd=1, relief="solid", width=200, height=175)
        self.grid_propagate(False)

        cover = tk.Label(self, text= "[ Portada ]", bg= COLOR_CARD_BG, fg= COLOR_CARD_BG, font=("Arial", 12, "bold"))
        cover.pack(pady=10)

        footer= tk.Frame(self, bg= COLOR_CARD_BG, height= 55, padx= 8, pady= 6)
        footer.pack(side="bottom", fill="x")

        tk.Label(footer, text=cancion.titulo, bg= COLOR_CARD_BG, fg= COLOR_CARD_BG, font=("Arial", 10)).pack(side="left", padx=(0,6))

        info = tk.Frame(footer, bg= COLOR_CARD_BG)
        info.pack(side="left", fill="x", expand=True)

        titulo = cancion["titulo"]
        if len(titulo) > 16:
            titulo = titulo[:16] + "..."

        tk.Label(info, text=titulo, bg= COLOR_CARD_BG, fg= COLOR_CARD_BG, font=("Arial", 10)).pack(side="top", anchor="w")
        tk.Label(info, text=cancion["artista"], bg= COLOR_CARD_BG, fg= COLOR_CARD_BG, font=("Arial", 8)).pack(side="top", anchor="w")

        if CardCancion._icon_play is None:
            CardCancion._icon_play = tk.PhotoImage(file= os.path.join(ICONS_DIR, "play.svg"))
        self._icon_play = CardCancion._icon_play

        btn_play = tk.Button(
            footer,
            image= self._icon_play,
            bg= COLOR_CARD_BG,
            bd=0,
            padx=4,
            pady=2,
            cursor="hand2",
            command=lambda: onplay(cancion)
        )
        btn_play.image =self._icon_play
        btn_play.pack(side="right")