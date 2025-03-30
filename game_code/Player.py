#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from Entity import Entity
from Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDHT

class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_LEFT] and self.rect.left < 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDHT:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass
