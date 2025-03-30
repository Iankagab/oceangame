#!/usr/bin/python
# -*- coding: utf-8 -*-
from Const import ENTITY_SPEED, WIN_WIDHT, WIN_HEIGHT
from Entity import Entity
import random

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.reset_position()

    def reset_position(self):
        self.rect.x = WIN_WIDHT
        self.rect.y = random.randint(0, WIN_HEIGHT)
        self.speed = random.randint(1, 5)

    def move (self,):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        
