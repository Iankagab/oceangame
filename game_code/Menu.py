#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from Const import WIN_WIDHT, WIN_HEIGHT, MENU_OPTION, COLOR_YELLOW, COLOR_WHITE, COLOR_BLACK, COLOR_GREEN

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/backgrounds/background4/orig.png')
        self.rect = self.surf.get_rect()
        self.selected_option = 0  

    def run(self):

        pygame.mixer_music.load('./asset/music.mp3')
        pygame.mixer_music.play(-1, 0.0)  

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    running = False  
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  
                        self.selected_option = (self.selected_option + 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_UP:  
                        self.selected_option = (self.selected_option - 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_RETURN: 
                        self.execute_option()
                        if MENU_OPTION[self.selected_option] == "EASY":
                            return "EASY"

            
            self.window.fill(COLOR_YELLOW)

            
            self.window.blit(self.surf, self.rect)

            
            self.menu_text(80, "Ocean Game", COLOR_GREEN, (WIN_WIDHT / 2, 90))

            
            self.display_menu_options()

            
            pygame.display.update()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)

    def display_menu_options(self):
        font = pygame.font.SysFont("Lucida Sans Typewriter", 40)
        spacing = 60  
        initial_y = 140 
        for i, option in enumerate(MENU_OPTION):
            
            color = COLOR_YELLOW if i == self.selected_option else COLOR_BLACK
            text_surf = font.render(option, True, color)
            text_rect = text_surf.get_rect(center=(WIN_WIDHT / 2, initial_y + i * spacing))
            if text_rect.bottom > WIN_HEIGHT:
                break
            self.window.blit(text_surf, text_rect)

    def execute_option(self):
        if MENU_OPTION[self.selected_option] == 'EXIT':
            pygame.quit() 
        elif MENU_OPTION[self.selected_option] == 'EASY':
            print("Iniciar jogo em modo EASY")
        elif MENU_OPTION[self.selected_option] == 'MEDIUM':
            print("Iniciar jogo em modo MEDIUM")
        elif MENU_OPTION[self.selected_option] == 'HARD':
            print("Iniciar jogo em modo HARD")
