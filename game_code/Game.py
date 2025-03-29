#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
sys.path.append('/home/iankagabriele/jogo/game_code')
from Const import WIN_WIDHT, WIN_HEIGHT
import pygame

from Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDHT, WIN_HEIGHT))

    def run(self):

        menu = Menu(self.window)
        menu.run()  

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  
        pygame.quit()  
