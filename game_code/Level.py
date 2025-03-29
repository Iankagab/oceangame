#!/usr/bin/python
#-*- coding: utf-8 -*-

import pygame
from Const import WIN_WIDHT, WIN_HEIGHT

class shark:
    def __init__(self, window):
        self.window = window
        self.running = True

        self.background = pygame.image.load("./asset/backgrounds/background4/orig.png")  
        self.shark = pygame.image.load("./asset/shark.png")  
        self.shark_x = -100  
        self.shark_y = WIN_HEIGHT / 2  

    def run(self):
        clock = pygame.time.Clock()

        while self.running:
            self.window.blit(self.background, (0, 0))  

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.shark_x += 3
            if self.shark_x > WIN_WIDHT:
                self.shark_x = -100 

            self.window.blit(self.shark, (self.shark_x, self.shark_y))
            pygame.display.update()
            clock.tick(30)  

        pygame.quit()

