import os
import tkinter as tk
from turtle import left, right
from src.config.styles import COLOR_BAR_BG, ICONS_DIR

class PlayerBar(tk.Frame):
    def __init__(self, root, on_toggle_play, on_volume):
        super().__init__(root, bg=COLOR_BAR_BG, height=60)
        self.pack_propagate(tk.FALSE)

        self.icon_corazon = tk.PhotoImage(file=os.path.join(ICONS_DIR, "heart.svg"))
        self.icon_anterior = tk.PhotoImage(file=os.path.join(ICONS_DIR, "previous.svg"))
        self.icon_reproducir = tk.PhotoImage(file=os.path.join(ICONS_DIR, "play.svg"))
        self.icon_pausar = tk.PhotoImage(file=os.path.join(ICONS_DIR, "pause.svg"))
        self.icon_siguiente = tk.PhotoImage(file=os.path.join(ICONS_DIR, "next.svg"))
        self.icon_volumen = tk.PhotoImage(file=os.path.join(ICONS_DIR, "volume.svg"))

        #CONTROLES CENTRALES
        controles = tk.Frame(self, bg=COLOR_BAR_BG)
        controles.pack(pady=(6,2))

        #Botones controls
        btn_corazon = tk.Button(
            controles,image = self.icon_corazon, bd=0, relief="flat", bg = COLOR_BAR_BG, cursor="hand2", font=("Arial",10,"bold")
        ).grid(row=0, column=0, padx=8)

        btn_anterior = tk.Button(
            controles,image = self.icon_anterior, bd=0, relief="flat", bg = COLOR_BAR_BG, cursor="hand2", font=("Arial",10,"bold")
        ).grid(row=0, column=1, padx=6)

        self.btn_play = tk.Button(
            controles,image = self.icon_reproducir, bd=0, relief="flat", bg = COLOR_BAR_BG, cursor="hand2", font=("Arial",10,"bold")
        ).grid(row=0, column=2, padx=8)

        btn_siguiente = tk.Button(
            controles,image = self.icon_siguiente, bd=0, relief="flat", bg = COLOR_BAR_BG, cursor="hand2", font=("Arial",10,"bold")
        ).grid(row=0, column=3, padx=6)

        btn_volumen = tk.Button(
            controles,image = self.icon_volumen, bd=0, relief="flat", bg = COLOR_BAR_BG, cursor="hand2", font=("Arial",10,"bold")
        ).grid(row=0, column=4, padx=8)


        #Tiempo y barra de progreso
        track = tk.Frame(self, bg=COLOR_BAR_BG)
        track.pack(fill="x", padx=30, pady=(2, 6))

        tk.Label(track, text="0:00", bg= COLOR_BAR_BG, font= ("Arial", 10, "bold")).pack(side=left, padx = 5 )
        tk.Scale(track, from_=0, to=100, orient="horizontal", showvalue=False).pack(side="center", extend=True, padx=8)
        tk.Label(track, text="0:00", bg= COLOR_BAR_BG, font= ("Arial", 10, "bold")).pack(side=right, padx = 5 )

        def set_play_icon(self, reproduciendo):
            nuevo_icono = self.icon_pausar if reproduciendo else self.icon_reproducir
            self.btn_play.config(image = nuevo_icono)
            self.btn_play.image = nuevo_icono
            
#el botón de pausa tiene ser una función tiene que escuchar la variable reproduciendo
#btn_play con una condicional if else
        '''
        tk.Button(controles, text="❤️", bg= "#2222222", bg= 0, font=('Arial', 12), cursor="hand2" ).grid(row=0, column=0, padx=8)
        tk.Button(controles, text="⏮️", bg= "#2222222", bg= 0, font=('Arial', 12), cursor="hand2" ).grid(row=0, column=1, padx=6)

        self.btn_play = tk.Button(
            controles, text="▶️", bg="#222222", fg="#ffffff", bg=1, relief="ridge", font=("Arial", 14, "bold"), width=3, height=1, 
            command=on_toggle_play
        ).grid(row=0, column=2, padx=8)

        tk.button(controles, text="⏭️", bg="#222222", font=("Arial", 12), relief="flat").grid(row=0, column=3, padx=6)
        '''