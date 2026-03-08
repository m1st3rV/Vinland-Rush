import datetime
from datetime import datetime
import sys
from os import name

import pygame
import os

from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_GREEN_LIME, WIN_WIDTH, COLOR_BLACK, MENU_OPTION
from code.DBProxy import DBProxy


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load(os.path.join('./asset/nature_6/orig.png')).convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.menu_option = 0



    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/music/level1.wav')  # FILE PATH
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.score_text(50, 'FIM DE JOGO', COLOR_GREEN_LIME, (WIN_WIDTH/2, 50))
            if game_mode == MENU_OPTION[0] or game_mode == MENU_OPTION[1]:
                score = player_score[0]
                text = 'ENTER YOUR NAME (MAX 10 CHARACTERS)'
            if game_mode == MENU_OPTION[2]:
                while True:
                    self.score_text(50, 'FIM DE JOGO', COLOR_GREEN_LIME, (WIN_WIDTH / 2, 50))
                    self.score_text(30, 'Modo cooperativo não registra pontuação', COLOR_GREEN_LIME,
                                    (WIN_WIDTH / 2, 150))
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    return  # encerra aqui, sem salvar nada
            self.score_text(20, text, COLOR_GREEN_LIME, (WIN_WIDTH / 2, 80))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) <= 10:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) == 0:
                            name += event.unicode
            self.score_text(20, name, COLOR_GREEN_LIME, (WIN_WIDTH / 2, 90))

            pygame.display.flip()
            pass





    def show(self):
        pygame.mixer_music.load('./asset/music/level1.wav')  # FILE PATH
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()
            pass


    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect =  text_surf.get_rect(center=text_center_position)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime  = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%m/%d/%Y")
    return f"{current_time} - {current_date}"