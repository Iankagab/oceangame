#!/usr/bin/python
#-*- coding: utf-8 -*-

import pygame
from Const import WIN_WIDHT, WIN_HEIGHT
from Entity import Entity
from EntityFactory import EntityFactory

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity]= []

        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run (self,):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    running = False

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            pygame.display.flip()

        pygame.quit()

