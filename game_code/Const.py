import pygame

# C
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_BLACK = (0,0,0)
COLOR_GREEN = (0,100,0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 1,
    'Level1Bg2' : 2,
    'Level1Bg3' : 3,
    'Level1Bg4' : 4,
    'Level1Bg5' : 5,
    'Player1' : 3,
    'Enemy1' : 3,
    'Enemy2' : 3,
}


ENTITY_HEALTH = {
    'Level1Bg0' : 999,
    'Level1Bg1' : 999,
    'Level1Bg2' : 999,
    'Level1Bg3' : 999,
    'Level1Bg4' : 999,
    'Level1Bg5' : 999,
    'Player1' : 300,
    'Enemy1' : 50,
    'Enemy2' : 50,
}

# M
MENU_OPTION = ('EASY',
               'MEDIUM' ,
               'HARD' ,
               'EXIT')

# P
PLAYER_KEY_SHOOT = {
    'Player1' : pygame.K_RCTRL
}

# S
SPAWN_TIME = 4000

# W
WIN_WIDHT = 576
WIN_HEIGHT = 324