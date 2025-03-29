#!/usr/bin/python
# -*- coding: utf-8 -*-

from Background import Background
class EntityFactory:
    
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name: 
            case 'Level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background)