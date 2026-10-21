import os

try: 
    import pygame
    pygame.mixer.init()
    AUDIO = True
except Exception:
    AUDIO = False

#Clase que se encarga de la reproduccion de audio
class AudioPlayer:

    #Metodo que se encarga de reproducir la musica
    def reproducir(self, ruta):
        if AUDIO and ruta and os.path.exists(ruta):
            pygame.mixer.music.load(ruta)
            pygame.mixer.music.play()
    
    #Metodo que se encarga de pausar la musica
    def pausar(self):
        if AUDIO:
            pygame.mixer.music.pause()
    
    #Metodo que se encarga de reanudar la musica
    def reudar(self):
        if AUDIO:
            pygame.mixer.music.unpause()

    #Metodo que se encarga de ajustar el volumen de la musica
    def ajustar_volumen(self, valor):
        if AUDIO:
            pygame.mixer.music.set_volume(float(valor))
