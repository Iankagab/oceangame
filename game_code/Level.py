#!/usr/bin/python
#-*- coding: utf-8 -*-

import pygame
import random
from Player import Player
import sys
from pygame import Surface, Rect
from pygame.font import Font
from Const import WIN_WIDHT, WIN_HEIGHT, COLOR_WHITE, EVENT_ENEMY, SPAWN_TIME, ENTITY_HEALTH, COLOR_GREEN
from Entity import Entity
from Enemy import Enemy
from EntityFactory import EntityFactory
from EntityMediator import EntityMediador
from Menu import Menu, MENU_OPTION
from game_code.PlayerShoot import PlayerShoot
from Gameover import GameOver
from Victory import Victory

class Level:
    def __init__(self, window, name, game_mode, position=(0, 0)):
        self.timeout = 10000

        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.position = position
        self.game_over = False
        self.start_time = pygame.time.get_ticks()
        self.game_won = False
        self.entity_list: list[Entity] = []

        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.extend(EntityFactory.get_entity('Player1'))
        self.entity_list.extend(EntityFactory.get_entity('Enemy1'))
        self.entity_list.extend(EntityFactory.get_entity('Enemy2'))

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(60)

            if self.game_over:
                game_over_screen = GameOver(self.window)
                game_over_screen.display()
                running = False
                self.run_menu()

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                if isinstance(ent, (Player)):
                    shoot = ent.shoot() if hasattr(ent, 'shoot') else None
                    if shoot is not None:
                        self.entity_list.append(shoot)

                    for enemy in [e for e in self.entity_list if isinstance(e, Enemy)]:
                        if ent.rect.colliderect(enemy.rect):
                            ent.lives -= 1

                            if ent.lives <= 0 and not self.game_over:
                                self.game_over = True
                                self.game_over_time = pygame.time.get_ticks()

                            enemy.reset_position()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for ent in self.entity_list:
                if isinstance(ent, Enemy) and ent.rect.right < 0:
                    ent.reset_position()

            EntityMediador.verify_collision(self.entity_list)
            EntityMediador.verify_health(self.entity_list)

            enemy_count = sum(1 for ent in self.entity_list if isinstance(ent, Enemy))

            if enemy_count < 1:
                self.entity_list.extend(EntityFactory.get_entity('Enemy1'))
                self.entity_list.extend(EntityFactory.get_entity('Enemy2'))

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', text_color=COLOR_WHITE, text_pos=(10, 5))
            self.level_text(text_size=14, text=f'fps: {clock.get_fps():.0f}', text_color=COLOR_WHITE, text_pos=(10, WIN_HEIGHT - 35))
            self.level_text(text_size=14, text=f'entidades: {len(self.entity_list)}', text_color=COLOR_WHITE, text_pos=(10, WIN_HEIGHT - 20))
            player = next((ent for ent in self.entity_list if isinstance(ent, Player)), None)
            if player:
                self.level_text(text_size=20, text=f'Vidas restantes: {player.lives}', text_color=COLOR_WHITE, text_pos=(WIN_WIDHT - 200, 5))

            elapsed_time = pygame.time.get_ticks() - self.start_time
            player = next((ent for ent in self.entity_list if isinstance(ent, Player)), None)
            if elapsed_time >= self.timeout and player and player.lives > 0:
                self.game_won = True
                self.display_victory()
                running = False  

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf = text_font.render(text, True, text_color)
        text_rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def display_victory(self):
        # Tela preta para o cenário de vitória
        black_surface = pygame.Surface((WIN_WIDHT, WIN_HEIGHT))
        black_surface.fill((0, 0, 0))  # Preenche com a cor preta
        self.window.blit(black_surface, (0, 0))
        
        font = pygame.font.SysFont('Arial', 72)
        victory_text = font.render('Você Venceu!', True, (255, 0, 0))
        text_rect = victory_text.get_rect(center=(WIN_WIDHT // 2, WIN_HEIGHT // 2))

        self.window.blit(victory_text, text_rect)
        pygame.display.flip()

        # Espera 2 segundos para o jogador ver a mensagem
        pygame.time.wait(2000)

        # Espera por qualquer tecla para voltar ao menu
        self.wait_for_key_press()

    def wait_for_key_press(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    waiting = False
                    self.run_menu()  # Chama o menu após pressionar uma tecla

    def display_game_over(self):
        # Tela preta para o cenário de Game Over
        black_surface = pygame.Surface((WIN_WIDHT, WIN_HEIGHT))
        black_surface.fill((0, 0, 0))  # Preenche com a cor preta
        self.window.blit(black_surface, (0, 0))

        font = pygame.font.SysFont('Arial', 72) 
        game_over_text = font.render('Game Over', True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(WIN_WIDHT // 2, WIN_HEIGHT // 2))

        self.window.blit(game_over_text, text_rect)
        pygame.display.flip()

        # Espera 2 segundos para o jogador ver a mensagem
        pygame.time.wait(2000)

        # Espera por qualquer tecla para voltar ao menu
        self.wait_for_key_press()

    def run_menu(self):
        menu = Menu(self.window)  
        selected_option = menu.run()
        
        if selected_option == 'EASY':
            self.reset_game()
        elif selected_option == 'EXIT':
            pygame.quit()
            quit()

    def reset_game(self):
        self.entity_list.clear()  
        self.__init__(self.window, 'Level 1', 'EASY')  
        self.run()
