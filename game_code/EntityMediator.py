#!/usr/bin/python
# -*- coding: utf-8 -*-

from Entity import Entity
from Enemy import Enemy

class EntityMediador:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
    
    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            teste_entity = entity_list[i]
            EntityMediador.__verify_collision_window(teste_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)