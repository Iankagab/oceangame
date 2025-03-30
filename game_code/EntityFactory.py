#!/usr/bin/python
# -*- coding: utf-8 -*-

from game_code.Background import Background
from Const import WIN_HEIGHT, WIN_WIDHT
from Enemy import Enemy
from Player import Player
import random

class EntityFactory:
    last_enemy_y = -1
    
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        list_bg = []  
    
        if entity_name == 'Level1Bg':
            for i in range(6):
                list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDHT, 0)))

            return list_bg  

        if entity_name == 'Player1':
            return [Player('Player1', (10, WIN_HEIGHT / 2 - 30))]  
        
        if entity_name == 'Enemy1':
            return [Enemy('Enemy1', (WIN_WIDHT + 10,random.randint(40, WIN_HEIGHT - 40)))] 
        if entity_name == 'Enemy2':
            return [Enemy('Enemy2', (WIN_WIDHT + 10,random.randint(40, WIN_HEIGHT - 40)))] 


