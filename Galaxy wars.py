import os
import pygame
import time
import random


pygame.font.init()

# WIDTH AND HEIGHT
WIDTH, HEIGHT = 1367, 710
pygame.display.set_caption("Galaxy wars")


# window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# LOAD ENEMY SHIP IMAGES
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("green_spaceship.png"))
SPACE_ENEMY = pygame.image.load(os.path.join("enemy.png"))
SPACE_UFO = pygame.image.load(os.path.join("ufo.png"))

# player ship
PLAYER_SPACE_SHIP = pygame.image.load(os.path.join("rocket-vector.png"))

# bullets
bullets = pygame.image.load(os.path.join("bullet.png"))

# BG
BG = pygame.transform.scale(pygame.image.load(os.path.join("glowing-sky.jpg")), (WIDTH, HEIGHT))


class Ship:

    
    def __init__(self, x, y, health*100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.bullet_img = None
        self.cool_down_counter = 0

    def draw(self)
def main():
    run = True
    fps = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comics ans", 50)
    clock = pygame.time.Clock()

    def draw_window():
        WIN.blit(BG, (0, 0))
        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, "orange")
        level_label = main_font.render(f"Level: {level}", 1, "sky blue")
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        pygame.display.update()

    draw_window()

    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


main()
