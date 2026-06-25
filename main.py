import os
import pygame as pg
import random
import sys

class TreasureHunters:

    def __init__(self):
        
        pg.init()
        pg.mixer.init() # Inicializa o sistema de som
        
        self.BASE_DIR = os.path.dirname(__file__)
        self.white        = (255, 255, 255)
        self.black        = (  0,   0,   0)
        self.purple_dark  = (181, 181, 255)
        self.purple_light = (230, 230, 255)
        self.green        = (  0, 255,   0)
        self.green_light  = (180, 255, 180)
        self.blue         = (  0,   0, 255)

        self.window = pg.display.set_mode((1280, 768))
        pg.display.set_caption("Treasure Hunters - Jogando")

        pg.font.init()
        self.font = pg.font.SysFont("Courier New", 50, bold=True)

        self.clock = pg.time.Clock()

        # ==========================================
        # SISTEMA DE SELEÇÃO DE FASES E MÚSICA
        # ==========================================
        # Captura a fase enviada pelo menu.py por argumento. Se não houver, assume a fase 1 por padrão.
        self.fase_atual = 1
        if len(sys.argv) > 1:
            try:
                self.fase_atual = int(sys.argv[1])
            except ValueError:
                self.fase_atual = 1

        # Dicionário de mapas global para consulta ao reiniciar/avançar de fase
       # ==========================================
        # CONFIGURAÇÃO DAS FASES (MAPAS)
        # ==========================================
        # ==========================================
        # CONFIGURAÇÃO DAS FASES (MAPAS)
        # ==========================================
        mapa_fase_1 = [
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M','M',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ','1','2','3',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ','1','2','3',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ','1','3',' ','1','2','3',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ','7','9',' ','4','5','6',' ',' ',' ','1','2','3',' ',' ',' ','1','2','3',' ',' ',' ','1','2','3',' ',' ',' ','1','2','3',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','7','8','9',' ',' ',' ',' ','4','5','6',' ',' ',' ','7','8','9',' ',' ',' ','7','8','9',' ',' ',' ','7','8','9',' ',' ',' ','7','8','9',' ',' ',' ','1','2','3',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4','5','6',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','F',' ',' ',' ',' '],
            ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','5','5','6',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ',' ',' ']
        ]

        mapa_fase_2 = [
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ','1','2','3',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ','1','2','3',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ','1','3',' ','1','2','3',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ','7','9',' ','4','5','6',' ',' ',' ','1','2','3',' ',' ',' ','1','2','3',' ',' ',' ','1','2','3',' ',' ',' ','1','2','3',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ','M',' ',' ',' ','M',' ',' ',' ','M',' ',' ',' ','M',' ',' ',' ','M',' ',' ',' ',' ',' ','M',' ',' ',' ',' ','M',' ',' ',' ','M',' ',' ',' ',' ','M',' ',' ',' ',' ','M',' ',' ',' ','M',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','7','8','9',' ',' ',' ',' ','4','5','6',' ',' ',' ','7','8','9',' ',' ',' ','7','8','9',' ',' ',' ','7','8','9',' ',' ',' ','7','8','9',' ',' ',' ','1','2','3',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4','5','6',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','F',' ',' ',' '],
            ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','5','5','6',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ',' ','2',' ',' ',' ',' ','2',' ',' ',' ',' ','2',' ',' ',' ',' ','2',' ',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ',' ','1','2','3',' ',' ']
        ]

        mapa_fase_3 = [
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ','1','2','3',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2',' ',' ','2',' ',' ',' ','2',' ',' ',' ','1','3',' ',' ',' ','2',' ',' ',' ','1','3',' ',' ',' ','2',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','2',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','3',' ',' ',' ','2',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ','1','2','3',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ','1','2','3',' ',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ','1','3',' ','1','2','3',' ',' ',' ',' ','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ','2',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ','7','9',' ','4','5','6',' ',' ',' ','1','2','3',' ',' ',' ','1','2','3',' ',' ',' ','1','2','3',' ',' ',' ','1','2','3',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ','2',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','7','8','9',' ',' ',' ',' ','4','5','6',' ',' ',' ','7','8','9',' ',' ',' ','7','8','9',' ',' ',' ','7','8','9',' ',' ',' ','7','8','9',' ',' ',' ','1','2','3',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ','2',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ','F',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4','5','6',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ','M',' ',' ',' ','M',' ',' ',' ','M',' ',' ',' ','M',' ',' ','M',' ',' ','M',' ',' ','M',' ',' ',' ','M',' ',' ',' ','M',' ',' ','M',' ',' ',' ','M',' ',' ','M',' ',' ',' ','M',' ',' ',' ',' ',' ',' ',' ',' ','2',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ','M',' ',' ',' ','M',' ',' ','M',' ',' ',' ','M',' ',' ',' ','M',' ',' ',' ','M',' ',' ',' ','M',' ',' ',' ','M',' ',' ',' ','M',' ',' ',' ','2',' ',' ',' ',' ','1','2','3',' '],
            ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','5','5','6',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ','2',' ',' ','2',' ',' ','2',' ',' ','2',' ',' ',' ','2',' ',' ',' ','2',' ',' ','2',' ',' ',' ','2',' ',' ','2',' ',' ',' ','2',' ',' ','1','2','3',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ',' ','2',' ',' ',' ','2',' ',' ','2',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        ]

        # 1. Primeiro declaramos o dicionário com o nome esperado pela função 'carregar_dados_fase'
        self.mapas_fases = {1: mapa_fase_1, 2: mapa_fase_2, 3: mapa_fase_3}
        
        # 2. Agora sim chamamos a função que carrega a fase atual (ela vai achar self.mapas_fases sem problemas)
        self.carregar_dados_fase()

        self.fases_mapas = {1: mapa_fase_1, 2: mapa_fase_2, 3: mapa_fase_3}
        self.map = self.fases_mapas[self.fase_atual]

        # Carrega o mapa dinamicamente baseado na fase selecionada
        self.carregar_dados_fase()

    def carregar_dados_fase(self):
        """Prepara e limpa todas as variáveis ao iniciar ou mudar de fase."""
        self.map = self.mapas_fases.get(self.fase_atual, self.mapas_fases[1])
        
        # Alinhamento automático das colunas para prevenir bugs de índice
        max_colunas = max(len(linha) for linha in self.map)
        for i in range(len(self.map)):
            while len(self.map[i]) < max_colunas:
                self.map[i].append(' ')

        # Reinicia a música e as variáveis de controle do jogo
        self.iniciar_musica_fase()
        self.gravity = 1
        self.big_clouds_pos = 0
        self.small_cloud_1_pos = 0
        self.small_cloud_2_pos = 0
        self.small_cloud_3_pos = 0
        
        self.player_animation = 0
        self.player_animation_frame = 0
        self.player_pos = [300, 600]
        self.player_jump_force = -22
        self.player_vertical_speed = 0
        self.player_box_colider = [46, 54]

        self.coins = 0
        self.bomb_warnings = []
        self.warning_timer = 0
        self.warning_interval = 45
        self.warning_time = 0
        self.bomb_speed = 25
        self.warning_duration = 30
        self.warning_delay = 180

        self.warning_surface = pg.Surface((40, 768), pg.SRCALPHA)
        self.warning_font = pg.font.SysFont("Arial", 60, bold=True)
        self.warning_active = False
        self.bombs = []
        self.explosions = []
        self.on_ground = False
        self.camera_x = 0
        self.camera_y = 0
        self.win = False
        self.game_over = False
        self.last_click_status = (False, False, False)

        # Imagens
        self.player_idle_1 = self.carregar_e_redimension_reserva(['Sprites', 'Captain Clown Nose', 'Captain Clown Nose without Sword', '01-Idle', 'Idle 01.png'], (128, 80), (255, 200, 0))
        self.player_idle_2 = self.carregar_e_redimension_reserva(['Sprites', 'Captain Clown Nose', 'Captain Clown Nose without Sword', '01-Idle', 'Idle 02.png'], (128, 80), (255, 200, 0))
        self.player_idle_3 = self.carregar_e_redimension_reserva(['Sprites', 'Captain Clown Nose', 'Captain Clown Nose without Sword', '01-Idle', 'Idle 03.png'], (128, 80), (255, 200, 0))
        self.player_idle_4 = self.carregar_e_redimension_reserva(['Sprites', 'Captain Clown Nose', 'Captain Clown Nose without Sword', '01-Idle', 'Idle 04.png'], (128, 80), (255, 200, 0))
        self.player_idle_5 = self.carregar_e_redimension_reserva(['Sprites', 'Captain Clown Nose', 'Captain Clown Nose without Sword', '01-Idle', 'Idle 05.png'], (128, 80), (255, 200, 0))
        
        self.player_idle_left_1 = self.player_idle_1
        self.player_idle_left_2 = self.player_idle_2
        self.player_idle_left_3 = self.player_idle_3
        self.player_idle_left_4 = self.player_idle_4
        self.player_idle_left_5 = self.player_idle_5

        self.player_right_1 = self.carregar_e_redimension_reserva(['Sprites', 'Captain Clown Nose', 'Captain Clown Nose without Sword', '02-Run', 'Run 01.png'], (128, 80), (255, 100, 0))
        self.player_right_2 = self.carregar_e_redimension_reserva(['Sprites', 'Captain Clown Nose', 'Captain Clown Nose without Sword', '02-Run', 'Run 02.png'], (128, 80), (255, 100, 0))
        self.player_right_3 = self.carregar_e_redimension_reserva(['Sprites', 'Captain Clown Nose', 'Captain Clown Nose without Sword', '02-Run', 'Run 03.png'], (128, 80), (255, 100, 0))
        self.player_right_4 = self.carregar_e_redimension_reserva(['Sprites', 'Captain Clown Nose', 'Captain Clown Nose without Sword', '02-Run', 'Run 04.png'], (128, 80), (255, 100, 0))
        self.player_right_5 = self.carregar_e_redimension_reserva(['Sprites', 'Captain Clown Nose', 'Captain Clown Nose without Sword', '02-Run', 'Run 05.png'], (128, 80), (255, 100, 0))
        self.player_right_6 = self.carregar_e_redimension_reserva(['Sprites', 'Captain Clown Nose', 'Captain Clown Nose without Sword', '02-Run', 'Run 06.png'], (128, 80), (255, 100, 0))

        self.player_left_1 = pg.transform.flip(self.player_right_1, True, False)
        self.player_left_2 = pg.transform.flip(self.player_right_2, True, False)
        self.player_left_3 = pg.transform.flip(self.player_right_3, True, False)
        self.player_left_4 = pg.transform.flip(self.player_right_4, True, False)
        self.player_left_5 = pg.transform.flip(self.player_right_5, True, False)
        self.player_left_6 = pg.transform.flip(self.player_right_6, True, False)

        self.background = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Background', 'BG Image.png'], (1280, 768), (100, 150, 240))
        self.big_clouds = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Background', 'Big Clouds.png'], (896, 202), (255, 255, 255))
        self.small_cloud_1 = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Background', 'Small Cloud 1.png'], (148, 48), (240, 240, 240))
        self.small_cloud_2 = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Background', 'Small Cloud 2.png'], (266, 70), (240, 240, 240))
        self.small_cloud_3 = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Background', 'Small Cloud 3.png'], (280, 78), (240, 240, 240))

        self.big_water_animation_frame = 0
        self.big_water_1 = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Background', 'Water Reflect Big 01.png'], (340, 20), (0, 100, 200))
        self.big_water_2 = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Background', 'Water Reflect Big 02.png'], (340, 20), (0, 100, 200))
        self.big_water_3 = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Background', 'Water Reflect Big 03.png'], (340, 20), (0, 100, 200))
        self.big_water_4 = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Background', 'Water Reflect Big 04.png'], (340, 20), (0, 100, 200))

        self.medium_water_animation_frame = 0
        self.medium_water_1 = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Background', 'Water Reflect Medium 01.png'], (106, 6), (0, 90, 190))
        self.medium_water_2 = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Background', 'Water Reflect Medium 02.png'], (106, 6), (0, 90, 190))
        self.medium_water_3 = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Background', 'Water Reflect Medium 03.png'], (106, 6), (0, 90, 190))
        self.medium_water_4 = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Background', 'Water Reflect Medium 04.png'], (106, 6), (0, 90, 190))

        self.small_water_animation_frame = 0
        self.small_water_1 = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Background', 'Water Reflect Small 01.png'], (70, 6), (0, 80, 180))
        self.small_water_2 = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Background', 'Water Reflect Small 02.png'], (70, 6), (0, 80, 180))
        self.small_water_3 = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Background', 'Water Reflect Small 03.png'], (70, 6), (0, 80, 180))
        self.small_water_4 = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Background', 'Water Reflect Small 04.png'], (70, 6), (0, 80, 180))

        self.ground_1 = self.carregar_terreno_seguro("ground_1.png", "1.png", (120, 70, 40))
        self.ground_2 = self.carregar_terreno_seguro("ground_2.png", "2.png", (120, 70, 40))
        self.ground_3 = self.carregar_terreno_seguro("ground_3.png", "3.png", (120, 70, 40))
        self.ground_4 = self.carregar_terreno_seguro("ground_4.png", "4.png", (100, 60, 30))
        self.ground_5 = self.carregar_terreno_seguro("ground_5.png", "5.png", (100, 60, 30))
        self.ground_6 = self.carregar_terreno_seguro("ground_6.png", "6.png", (100, 60, 30))
        self.ground_7 = self.carregar_terreno_seguro("ground_7.png", "7.png", (80, 50, 20))
        self.ground_8 = self.carregar_terreno_seguro("ground_8.png", "8.png", (80, 50, 20))
        self.ground_9 = self.carregar_terreno_seguro("ground_9.png", "9.png", (80, 50, 20))

        self.coin = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Objetos', 'moeda.png'], (64, 64), (255, 215, 0))
        self.flag = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Objetos', 'Bandeira_final.png'], (64, 64), (0, 200, 100))
        self.bomb_img = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Objetos', 'bomba.png'], (40, 40), (50, 50, 50))
        
        img_explosao = self.carregar_e_redimension_reserva(['Sprites', 'Palm Tree Island', 'Objetos', 'explosão.png'], (100, 100), (255, 50, 50))
        self.explosion_frames = [img_explosao]

    def iniciar_musica_fase(self):
        """Gerencia o áudio de fundo dinamicamente baseado na fase."""
        try:
            nome_musica = f"fase_{self.fase_atual}.mp3"
            caminho_musica = os.path.join(self.BASE_DIR, "Sprites", "Palm Tree Island", nome_musica)
            if not os.path.exists(caminho_musica):
                caminho_musica = os.path.join(self.BASE_DIR, "Sprites", "Palm Tree Island", "Super Mario Bros Theme.mp3")

            if os.path.exists(caminho_musica):
                pg.mixer.music.load(caminho_musica)
                pg.mixer.music.set_volume(0.2)
                pg.mixer.music.play(-1)
        except Exception as e:
            print(f"[AVISO] Não foi possível reproduzir a música: {e}")

    def carregar_e_redimension_reserva(self, caminhos, tamanho, cor_reserva):
        caminho_completo = os.path.join(self.BASE_DIR, *caminhos)
        if os.path.exists(caminho_completo):
            try:
                img = pg.image.load(caminho_completo).convert_alpha()
                return pg.transform.scale(img, tamanho)
            except Exception:
                pass
        surf = pg.Surface(tamanho, pg.SRCALPHA)
        surf.fill(cor_reserva)
        return surf

    def carregar_terreno_seguro(self, nome_principal, nome_alternativo, cor_reserva):
        caminho_p = os.path.join(self.BASE_DIR, 'Sprites', 'Palm Tree Island', 'Terrain', nome_principal)
        if os.path.exists(caminho_p):
            return pg.transform.scale(pg.image.load(caminho_p).convert_alpha(), (64, 64))
        
        caminho_a = os.path.join(self.BASE_DIR, 'Sprites', 'Palm Tree Island', 'Terrain', nome_alternativo)
        if os.path.exists(caminho_a):
            return pg.transform.scale(pg.image.load(caminho_a).convert_alpha(), (64, 64))
            
        surf = pg.Surface((64, 64))
        surf.fill(cor_reserva)
        return surf

    def mouse_has_clicked(self, input):
        if self.last_click_status == input:
            return (False, False, False)
        else:
            left_button = False
            center_button = False
            right_button = False
            if self.last_click_status[0] == False and input[0] == True:
                left_button = True
            if self.last_click_status[1] == False and input[1] == True:
                center_button = True
            if self.last_click_status[2] == False and input[2] == True:
                right_button = True
            return (left_button, center_button, right_button)

    def background_imgs(self):
        self.window.blit(self.background, (0, 0))
        if self.big_clouds_pos > -896:
            self.big_clouds_pos -= 0.05
        else:
            self.big_clouds_pos = 0
        self.window.blit(self.big_clouds, (self.big_clouds_pos, 315))
        self.window.blit(self.big_clouds, (self.big_clouds_pos + 896, 315))
        self.window.blit(self.big_clouds, (self.big_clouds_pos + (896 * 2), 315))
        
        if self.small_cloud_1_pos > -1500:
            self.small_cloud_1_pos -= 0.3
        else:
            self.small_cloud_1_pos = 0
        self.window.blit(self.small_cloud_1, (120 + self.small_cloud_1_pos, 100))
        self.window.blit(self.small_cloud_1, (120 + self.small_cloud_1_pos + 1500, 100))
        self.window.blit(self.small_cloud_1, (900 + self.small_cloud_1_pos, 50))
        self.window.blit(self.small_cloud_1, (900 + self.small_cloud_1_pos + 1500, 50))

        if self.small_cloud_2_pos > -1500:
            self.small_cloud_2_pos -= 0.2
        else:
            self.small_cloud_2_pos = 0
        self.window.blit(self.small_cloud_2, (250 + self.small_cloud_2_pos, 200))
        self.window.blit(self.small_cloud_2, (250 + self.small_cloud_2_pos + 1500, 200))
        self.window.blit(self.small_cloud_2, (1000 + self.small_cloud_2_pos, 150))
        self.window.blit(self.small_cloud_2, (1000 + self.small_cloud_2_pos + 1500, 150))

        if self.small_cloud_3_pos > -1500:
            self.small_cloud_3_pos -= 0.2
        else:
            self.small_cloud_3_pos = 0
        self.window.blit(self.small_cloud_3, (650 + self.small_cloud_3_pos, 250))
        self.window.blit(self.small_cloud_3, (650 + self.small_cloud_3_pos + 1500, 250))

        if self.big_water_animation_frame <= 12:
            self.window.blit(self.big_water_1, (300, 550))
        elif self.big_water_animation_frame <= 24:
            self.window.blit(self.big_water_2, (300, 550))
        elif self.big_water_animation_frame <= 36:
            self.window.blit(self.big_water_3, (300, 550))
        elif self.big_water_animation_frame <= 48:
            self.window.blit(self.big_water_4, (300, 550))
        self.big_water_animation_frame += 1
        if self.big_water_animation_frame > 48:
            self.big_water_animation_frame = 0

        if self.medium_water_animation_frame <= 12:
            self.window.blit(self.medium_water_1, (250, 600))
            self.window.blit(self.medium_water_1, (500, 625))
        elif self.medium_water_animation_frame <= 24:
            self.window.blit(self.medium_water_2, (250, 600))
            self.window.blit(self.medium_water_2, (500, 625))
        elif self.medium_water_animation_frame <= 36:
            self.window.blit(self.medium_water_3, (250, 600))
            self.window.blit(self.medium_water_3, (500, 625))
        elif self.medium_water_animation_frame <= 48:
            self.window.blit(self.medium_water_4, (250, 600))
            self.window.blit(self.medium_water_4, (500, 625))
        self.medium_water_animation_frame += 1
        if self.medium_water_animation_frame > 48:
            self.medium_water_animation_frame = 0

        if self.small_water_animation_frame <= 12:
            self.window.blit(self.small_water_1, (1000, 600))
            self.window.blit(self.small_water_1, (900, 625))
        elif self.small_water_animation_frame <= 24:
            self.window.blit(self.small_water_2, (1000, 600))
            self.window.blit(self.small_water_3, (900, 625))
        elif self.small_water_animation_frame <= 36:
            self.window.blit(self.small_water_3, (1000, 600))
            self.window.blit(self.small_water_3, (900, 625))
        elif self.small_water_animation_frame <= 48:
            self.window.blit(self.small_water_4, (1000, 600))
            self.window.blit(self.small_water_4, (900, 625))
        self.small_water_animation_frame += 1
        if self.small_water_animation_frame > 48:
            self.small_water_animation_frame = 0

    def tiles(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] != ' ':
                    px = x * 64 - self.camera_x
                    py = y * 64 - self.camera_y
                    if self.map[y][x] == '1': self.window.blit(self.ground_1, (px, py))
                    elif self.map[y][x] == '2': self.window.blit(self.ground_2, (px, py))
                    elif self.map[y][x] == '3': self.window.blit(self.ground_3, (px, py))
                    elif self.map[y][x] == '4': self.window.blit(self.ground_4, (px, py))
                    elif self.map[y][x] == '5': self.window.blit(self.ground_5, (px, py))
                    elif self.map[y][x] == '6': self.window.blit(self.ground_6, (px, py))
                    elif self.map[y][x] == '7': self.window.blit(self.ground_7, (px, py))
                    elif self.map[y][x] == '8': self.window.blit(self.ground_8, (px, py))
                    elif self.map[y][x] == '9': self.window.blit(self.ground_9, (px, py))
                    elif self.map[y][x] == 'F': self.window.blit(self.flag, (px, py))
                    elif self.map[y][x] == 'M': self.window.blit(self.coin, (px, py))

    def collect_coins(self):
        player_rect = pg.Rect(self.player_pos[0] + 40, self.player_pos[1] + 8, self.player_box_colider[0], self.player_box_colider[1])
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == 'M':
                    coin_rect = pg.Rect(x * 64, y * 64, 64, 64)
                    if player_rect.colliderect(coin_rect):
                        self.map[y][x] = ' '
                        self.coins += 1
    
    def draw_coins(self):
        text = self.font.render(f"FASE {self.fase_atual} | MOEDAS: {self.coins}", True, (255,255,255))
        self.window.blit(text, (20, 20))

    def draw_bomb_warnings(self):
        if not self.warning_active: return
        if self.warning_time % 20 < 10:
            self.warning_surface.fill((0,0,0,0))
            pg.draw.rect(self.warning_surface, (255,0,0,128), (0,0,40,768))
            for warning in self.bomb_warnings:
                self.window.blit(self.warning_surface, (warning["x"] - 20 - self.camera_x, 0))
                warning_text = self.warning_font.render("!", True, (255,255,255))
                self.window.blit(warning_text, (warning["x"] - warning_text.get_width()/2 - self.camera_x, 350))

    def create_warnings(self):
        self.bomb_warnings.clear()
        distancia_minima = 150
        tentativas = 0
        while len(self.bomb_warnings) < 5 and tentativas < 100:
            tentativas += 1
            x = random.randint(self.camera_x, self.camera_x + 1280)
            valido = True
            for warning in self.bomb_warnings:
                if abs(x - warning["x"]) < distancia_minima:
                    valido = False
                    break
            if valido:
                self.bomb_warnings.append({"x": x})

    def bomb_manager(self):
        self.warning_time += 1
        if not self.warning_active:
            if self.warning_time >= self.warning_delay:
                self.create_warnings()
                self.warning_active = True
                self.warning_time = 0
        else:
            if self.warning_time >= self.warning_duration:
                for warning in self.bomb_warnings:
                    self.bombs.append({"x": warning["x"], "y": -100, "speed": self.bomb_speed})
                self.bomb_warnings.clear()
                self.warning_active = False
                self.warning_time = 0

    def draw_bombs(self):
        for bomb in self.bombs:
            self.window.blit(self.bomb_img, (bomb["x"] - 20 - self.camera_x, bomb["y"] - 20 - self.camera_y))

    def draw_explosions(self):
        for explosion in self.explosions:
            self.window.blit(self.explosion_frames[0], (explosion["x"] - 50 - self.camera_x, explosion["y"] - 50 - self.camera_y))

    def update_bombs(self):
        bombs_to_remove = []
        player_rect = pg.Rect(self.player_pos[0] + 40, self.player_pos[1] + 8, self.player_box_colider[0], self.player_box_colider[1])
        for bomb in self.bombs:
            bomb["y"] += bomb["speed"]
            bomb_rect = pg.Rect(bomb["x"] - 20, bomb["y"] - 20, 40, 40)
            if bomb_rect.colliderect(player_rect):
                self.explosions.append({"x": bomb["x"], "y": bomb["y"], "frame": 0})
                self.game_over = True
                bombs_to_remove.append(bomb)
                continue

            tile_x = int(bomb["x"] // 64)
            tile_y = int((bomb["y"] + 20) // 64)
            
            if 0 <= tile_y < len(self.map):
                if 0 <= tile_x < len(self.map[tile_y]):
                    tile = self.map[tile_y][tile_x]
                    if tile in ['1','2','3','4','5','6','7','8','9']:
                        self.explosions.append({"x": bomb["x"], "y": bomb["y"], "frame": 0})
                        bombs_to_remove.append(bomb)
                        continue
                        
            if bomb["y"] > len(self.map) * 64 + 200:
                bombs_to_remove.append(bomb)
        for bomb in bombs_to_remove:
            if bomb in self.bombs: self.bombs.remove(bomb)

    def update_explosions(self):
        remove = []
        for explosion in self.explosions:
            explosion["frame"] += 1
            if explosion["frame"] > 20: remove.append(explosion)
        for explosion in remove: self.explosions.remove(explosion)
    
    def check_win(self):
        player_rect = pg.Rect(
            self.player_pos[0] + 40,
            self.player_pos[1] + 8,
            self.player_box_colider[0],
            self.player_box_colider[1]
        )

        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == 'F':
                    flag_rect = pg.Rect(x * 64, y * 64, 64, 64)
                    if player_rect.colliderect(flag_rect):
                        if not self.win:
                            self.win = True
                            
                            # Se passou da fase_atual, desbloqueia a seguinte (máximo fase 3)
                            nova_fase_desbloqueada = min(self.fase_atual + 1, 3)
                            self.salvar_progresso(nova_fase_desbloqueada)
                            print(f"Vitória! Fase {self.fase_atual} concluída. Nova fase máxima: {nova_fase_desbloqueada}")

    def salvar_progresso(self, nova_fase):
        import json
        caminho_save = os.path.join(self.BASE_DIR, "save.json")
        fase_maxima = nova_fase
        
        if os.path.exists(caminho_save):
            try:
                with open(caminho_save, "r") as f:
                    dados = json.load(f)
                    if dados.get("fase_maxima", 1) > fase_maxima:
                        fase_maxima = dados.get("fase_maxima", 1)
            except: 
                pass
        try:
            with open(caminho_save, "w") as f:
                json.dump({"fase_maxima": fase_maxima}, f)
        except Exception as e:
            print(f"Erro ao salvar progresso: {e}")

    def salvar_progresso(self, nova_fase):
        import json
        caminho_save = os.path.join(self.BASE_DIR, "save.json")
        fase_maxima = nova_fase
        
        # Se o arquivo já existir, garante que não vamos sobrescrever um progresso maior com um menor
        if os.path.exists(caminho_save):
            try:
                with open(caminho_save, "r") as f:
                    dados = json.load(f)
                    if dados.get("fase_maxima", 1) > fase_maxima:
                        fase_maxima = dados.get("fase_maxima", 1)
            except: 
                pass
        try:
            with open(caminho_save, "w") as f:
                json.dump({"fase_maxima": fase_maxima}, f)
        except Exception as e:
            print(f"Erro ao salvar progresso: {e}")
    def retornar_ao_menu(self):
        pg.mixer.music.stop()
        pg.quit()
        import subprocess
        subprocess.Popen([sys.executable, "menu.py"])
        sys.exit()

    def draw_win(self):
        dark = pg.Surface((1280, 768))
        dark.set_alpha(180)
        dark.fill((0, 0, 0))
        self.window.blit(dark, (0, 0))

        win_text = self.font.render('VOCE VENCEU!', True, (255, 255, 255))
        restart_text = self.font.render('M - MENU PRINCIPAL | R - PROXIMA FASE', True, (255, 255, 255))
        self.window.blit(win_text, (400, 250))
        self.window.blit(restart_text, (120, 350))

    def player_idle(self):
        if self.player_animation_frame <= 7: self.window.blit(self.player_idle_1, (self.player_pos[0] - self.camera_x, self.player_pos[1] - self.camera_y))
        elif self.player_animation_frame <= 14: self.window.blit(self.player_idle_2, (self.player_pos[0] - self.camera_x, self.player_pos[1] - self.camera_y))
        elif self.player_animation_frame <= 21: self.window.blit(self.player_idle_3, (self.player_pos[0] - self.camera_x, self.player_pos[1] - self.camera_y))
        elif self.player_animation_frame <= 28: self.window.blit(self.player_idle_4, (self.player_pos[0] - self.camera_x, self.player_pos[1] - self.camera_y))
        elif self.player_animation_frame <= 35: self.window.blit(self.player_idle_5, (self.player_pos[0] - self.camera_x, self.player_pos[1] - self.camera_y))
        self.player_animation_frame += 1
        if self.player_animation_frame > 35: self.player_animation_frame = 0

    def player_idle_left(self):
        self.player_idle()

    def player_right(self):
        if self.player_animation_frame <= 7: self.window.blit(self.player_right_1, (self.player_pos[0] - self.camera_x, self.player_pos[1] - self.camera_y))
        elif self.player_animation_frame <= 14: self.window.blit(self.player_right_2, (self.player_pos[0] - self.camera_x, self.player_pos[1] - self.camera_y))
        elif self.player_animation_frame <= 21: self.window.blit(self.player_right_3, (self.player_pos[0] - self.camera_x, self.player_pos[1] - self.camera_y))
        elif self.player_animation_frame <= 28: self.window.blit(self.player_right_4, (self.player_pos[0] - self.camera_x, self.player_pos[1] - self.camera_y))
        elif self.player_animation_frame <= 35: self.window.blit(self.player_right_5, (self.player_pos[0] - self.camera_x, self.player_pos[1] - self.camera_y))
        elif self.player_animation_frame <= 42: self.window.blit(self.player_right_6, (self.player_pos[0] - self.camera_x, self.player_pos[1] - self.camera_y))
        self.player_animation_frame += 1
        if self.player_animation_frame > 42: self.player_animation_frame = 0

    def player_left(self):
        if self.player_animation_frame <= 7: self.window.blit(self.player_left_1, (self.player_pos[0] - self.camera_x, self.player_pos[1] - self.camera_y))
        elif self.player_animation_frame <= 14: self.window.blit(self.player_left_2, (self.player_pos[0] - self.camera_x, self.player_pos[1] - self.camera_y))
        elif self.player_animation_frame <= 21: self.window.blit(self.player_left_3, (self.player_pos[0] - self.camera_x, self.player_pos[1] - self.camera_y))
        elif self.player_animation_frame <= 28: self.window.blit(self.player_left_4, (self.player_pos[0] - self.camera_x, self.player_pos[1] - self.camera_y))
        elif self.player_animation_frame <= 35: self.window.blit(self.player_left_5, (self.player_pos[0] - self.camera_x, self.player_pos[1] - self.camera_y))
        elif self.player_animation_frame <= 42: self.window.blit(self.player_left_6, (self.player_pos[0] - self.camera_x, self.player_pos[1] - self.camera_y))
        self.player_animation_frame += 1
        if self.player_animation_frame > 42: self.player_animation_frame = 0

    def player_collider(self):
        pos_x = self.player_pos[0] + 40
        pos_y = self.player_pos[1] + 8
        box = [[pos_x, pos_y],
                [pos_x + self.player_box_colider[0], pos_y],
                [pos_x, pos_y + self.player_box_colider[1]],
                [pos_x + self.player_box_colider[0], pos_y + self.player_box_colider[1]]]
        
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] in ['1','2','3','4','5','6','7','8','9']:
                    for i in range(len(box)):
                        if x * 64 <= box[i][0] and y * 64 <= box[i][1] and (x * 64) + 64 >= box[i][0] and (y * 64) + 64 >= box[i][1]:
                            return True
        return False

    def player(self):
        self.player_vertical_speed += self.gravity
        self.player_pos[1] += self.player_vertical_speed
        if self.player_pos[1] > len(self.map) * 64 + 300:
            self.game_over = True
        if self.player_collider():
            self.player_pos[1] -= self.player_vertical_speed
            self.player_vertical_speed = 0
            self.on_ground = True
        else:
            self.on_ground = False
        if self.player_animation == 0: self.player_idle()
        elif self.player_animation == 1: self.player_idle_left()
        elif self.player_animation == 2: self.player_right()
        elif self.player_animation == 3: self.player_left()

    def camera(self):
        map_width = len(self.map[0]) * 64
        map_height = len(self.map) * 64
        self.camera_x = self.player_pos[0] - 640
        self.camera_y = self.player_pos[1] - 384
        if self.camera_x < 0: self.camera_x = 0
        if self.camera_y < 0: self.camera_y = 0
        if self.camera_x > map_width - 1280: self.camera_x = map_width - 1280
        if self.camera_y > map_height - 768: self.camera_y = map_height - 768

    def move(self, array, key):
        if self.game_over or self.win: return
        buttom_press = False

        if array[100] == True or array[pg.K_RIGHT]:
            self.player_pos[0] += 5
            if self.player_collider(): self.player_pos[0] -= 5
            else:
                self.player_animation = 2
                buttom_press = True

        if array[97] == True or array[pg.K_LEFT]:
            self.player_pos[0] -= 5
            if self.player_collider(): self.player_pos[0] += 5
            else:
                self.player_animation = 3
                buttom_press = True

        if buttom_press == False and self.player_animation == 2: self.player_animation = 0
        elif buttom_press == False and self.player_animation == 3: self.player_animation = 1

        map_width = len(self.map[0]) * 64
        if self.player_pos[0] < 0: self.player_pos[0] = 0
        if self.player_pos[0] > map_width - 128: self.player_pos[0] = map_width - 128
        if self.player_pos[1] < 0: self.player_pos[1] = 0

        if key == 'space' and self.on_ground:
            self.player_vertical_speed = self.player_jump_force
            
    def draw_game_over(self):
        dark = pg.Surface((1280, 768))
        dark.set_alpha(180)
        dark.fill((0, 0, 0))
        self.window.blit(dark, (0, 0))

        game_over_text = self.font.render('GAME OVER', True, (255, 255, 255))
        restart_text = self.font.render('M - MENU PRINCIPAL | R - REINICIAR', True, (255, 255, 255))
        self.window.blit(game_over_text, (430, 250))
        self.window.blit(restart_text, (180, 350))


jogo = TreasureHunters()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            nome_tecla = pg.key.name(event.key)
            
            if jogo.game_over or jogo.win:
                if nome_tecla == 'r':
                    if jogo.win:
                        # Se venceu, a variável fase_atual mudou! Carregamos de forma limpa os dados da nova fase
                        jogo.carregar_dados_fase()
                    else:
                        # Se morreu, reinicia os dados da mesma fase atual
                        jogo.carregar_dados_fase()
                elif nome_tecla == 'm':
                    jogo.retornar_ao_menu()
                    
            jogo.move(pg.key.get_pressed(), nome_tecla)
            if nome_tecla == 'escape':
                jogo.retornar_ao_menu()

    mouse_position  = pg.mouse.get_pos()
    mouse_input = pg.mouse.get_pressed()
    mouse_click = jogo.mouse_has_clicked(mouse_input)

    jogo.clock.tick(60)
    jogo.move(pg.key.get_pressed(), '')
    jogo.camera()
    jogo.background_imgs()
    jogo.tiles()
    jogo.bomb_manager()
    jogo.draw_bomb_warnings()
    jogo.update_bombs()
    jogo.update_explosions()
    jogo.draw_bombs()
    jogo.draw_explosions()
    jogo.draw_coins()

    if not jogo.game_over and not jogo.win:
        jogo.player()
        jogo.collect_coins()
        jogo.check_win()

    if jogo.game_over:
        jogo.draw_game_over()

    if jogo.win:
        jogo.draw_win()

    jogo.last_click_status = mouse_input
    pg.display.update()