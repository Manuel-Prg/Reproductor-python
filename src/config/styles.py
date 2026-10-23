import os

COLOR_BG = "#EDDEE0"
COLOR_NAVBAR_BG = "#36445D"
COLOR_PURPLE = "#9300FF"
COLOR_PURPLE_LIGHT = "#B155F1"
COLOR_ACCENT = "#5E46A0"
COLOR_GRID_BG = "#DC8079"
COLOR_CARD_BG = "#03627E"
COLOR_BAR_BG = "#2A1E5C"
COLOR_COVER_BG = "#8F5D94"

#RUTAS DE RECURSOS DEL PROYECTO
#Confriguración de los iconos:

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
#se optiene la ruta mediante el metodo path 
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
ICONS_DIR = os.path.join(ASSETS_DIR, "icons")

#condifugarción para la base de datos
DB_DIR = os.path.join(BASE_DIR, "database")
DB_PATH = os.path.join(DB_DIR, "database.db")