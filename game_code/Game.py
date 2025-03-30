#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('/home/iankagabriele/jogo/game_code')
from Const import WIN_WIDHT, WIN_HEIGHT, MENU_OPTION
import pygame

from Menu import Menu
from Level import Level  

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDHT, WIN_HEIGHT))

    def run(self):
        menu = Menu(self.window)  
        menu_return = menu.run()  

        if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2] ]:
            level = Level(self.window, 'EASY', menu_return)
            print(f"Classe de level: {type(level)}")   
            level_return = level.run()   

        pygame.quit()
        quit()
