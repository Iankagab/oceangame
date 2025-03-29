#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('/home/iankagabriele/jogo/game_code')
from Const import WIN_WIDHT, WIN_HEIGHT
import pygame

from Menu import Menu
from Level import shark  

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDHT, WIN_HEIGHT))

    def run(self):
        menu = Menu(self.window)  
        choice = menu.run()  

        if choice == "EASY": 
            shark_scene = shark(self.window) 
            shark_scene.run()
        elif choice == "MEDIUM":
            pass
            
        elif choice == "HARD":
            pass
            

        pygame.quit()

