import os
import pygame
import random

# LOAD IMAGES
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("SpaceInvaders", "green_spaceship.png"))
SPACE_ENEMY = pygame.image.load(os.path.join("SpaceInvaders""enemy.png"))
SPACE_UFO = pygame.image.load(os.path.join("ufo.png.png"))

# player ship
PLAYER_SPACE_SHIP = pygame.image.load(os.path.join("rocket-vector.png"))

# bullets
bullets = pygame.image.load(os.path.join("bullet.png"))

# BG
BG = pygame.image.load(os.path.join("glowing-sky.jpg"))

