#!/usr/bin/python
# -*- coding: utf-8 -*-

from Entity import Entity
from Const import WIN_HEIGHT, WIN_WIDHT, ENTITY_SPEED

class Background(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)


    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0 :
            self.rect.left = WIN_WIDHT
        pass