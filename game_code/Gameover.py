#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from Const import WIN_WIDHT, WIN_HEIGHT, COLOR_BLACK

class GameOver:
    def __init__(self, window):
        self.window = window

    def display(self):
        
        black_surface = pygame.Surface((WIN_WIDHT, WIN_HEIGHT))
        black_surface.fill((COLOR_BLACK)) 
        self.window.blit(black_surface, (0, 0))  

    
        font = pygame.font.SysFont('Arial', 72)  
        game_over_text = font.render('Game Over', True, (255, 0, 0))  
        text_rect = game_over_text.get_rect(center=(WIN_WIDHT // 2, WIN_HEIGHT // 2)) 
        self.window.blit(game_over_text, text_rect)

        restart_font = pygame.font.SysFont('Arial', 25)
        restart_text = restart_font.render('Aperte qualquer tecla para reiniciar', True, (255, 0, 0))
        restart_text_rect = restart_text.get_rect(center=(WIN_WIDHT // 2, WIN_HEIGHT // 2 + 80))  
        self.window.blit(restart_text, restart_text_rect)


        pygame.display.flip()
        self.wait_for_restart()

    def wait_for_restart(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    waiting = False
                    return  