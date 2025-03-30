#!/usr/bin/python
#-*- coding: utf-8 -*-

import pygame
import random
import sys
from pygame import Surface, Rect
from pygame.font import Font
from Const import WIN_WIDHT, WIN_HEIGHT, COLOR_WHITE, EVENT_ENEMY, SPAWN_TIME
from Entity import Entity
from Enemy import Enemy
from EntityFactory import EntityFactory
from EntityMediator import EntityMediador
from Menu import MENU_OPTION

class Level:
    def __init__(self, window, name, game_mode, position=(0, 0)):
        self.timeout = 20000

        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.position = position
        self.entity_list: list[Entity]= []

        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.extend(EntityFactory.get_entity('Player1'))
        self.entity_list.extend(EntityFactory.get_entity('Enemy1'))
    


        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    running = False

            EntityMediador.verify_collision(self.entity_list)
            EntityMediador.verify_health(self.entity_list)

            enemy_count = sum(1 for ent in self.entity_list if isinstance(ent, Enemy))

            if enemy_count < 2:  
                self.entity_list.extend(EntityFactory.get_entity('Enemy1'))
                self.entity_list.extend(EntityFactory.get_entity('Enemy2'))

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', text_color=COLOR_WHITE, text_pos=(10, 5))
            self.level_text(text_size=14, text=f'fps: {clock.get_fps():.0f}', text_color=COLOR_WHITE, text_pos=(10, WIN_HEIGHT - 35))
            self.level_text(text_size=14, text=f'entidades: {len(self.entity_list)}', text_color=COLOR_WHITE, text_pos=(10, WIN_HEIGHT - 20))
            pygame.display.flip()


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf = text_font.render(text, True, text_color) 
        text_rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

