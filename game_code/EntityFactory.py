#!/usr/bin/python
# -*- coding: utf-8 -*-

from game_code.Background import Background
from Const import WIN_HEIGHT, WIN_WIDHT
class EntityFactory:
    
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        if entity_name == 'Level1Bg':
            list_bg = []
        for i in range(6):
            list_bg.append(Background(f'Level1Bg{i}', (0,0)))
            list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDHT,0)))
            
        return list_bg  