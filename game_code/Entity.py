#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from Const import ENTITY_HEALTH
import pygame

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/background/' + name + '.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]

    
    @abstractmethod
    def move(self,):
        pass