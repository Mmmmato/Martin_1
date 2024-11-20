import pygame
import os

pygame.font.init()
pygame.mixer.init()
WIDTH, HEIGHT = 1365, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship Battle")

PURPLE = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)
BULLET_HIT_SOUND = pygame.mixer.Sound("electro_hit.wav")
BULLET_FIRE_SOUND = pygame.mixer.Sound("laser_shot.wav")

HEALTH_FONT = pygame.font.SysFont("comics ans", 40)
WINNER_FONT = pygame.font.SysFont("calibre", 100)

FPS = 60
VEL = 5

BULLET_VEL = 7
MAX_BULLETS = 5

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_HIT = pygame.USEREVENT + 1
PURPLE_HIT = pygame.USEREVENT + 2

SPACESHIP_1_IMAGE = pygame.image.load(os.path.join("space_ship1.png"))
SPACESHIP_1 = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_1_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
                                      270)
SPACESHIP_2_IMAGE = pygame.image.load(os.path.join("space_ship2.png"))
SPACESHIP_2 = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_2_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
                                      90)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join("space.jpg")), (WIDTH, HEIGHT))


def draw_window(purple, yellow, purple_bullets, yellow_bullets, purple_health, yellow_health):
    WIN.blit(SPACE, (0, 0))
    purple_health_text = HEALTH_FONT.render("Health :" + str(purple_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health :" + str(yellow_health), 1, WHITE)
    WIN.blit(purple_health_text, (WIDTH - purple_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(SPACESHIP_1, (yellow.x, yellow.y))
    WIN.blit(SPACESHIP_2, (purple.x, purple.y))
    for bullet in purple_bullets:
        pygame.draw.rect(WIN, PURPLE, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 10:  # DOWN
        yellow.y += VEL


def purple_handle_movement(keys_pressed, purple):
    if keys_pressed[pygame.K_LEFT] and purple.x - VEL > BORDER.x + BORDER.width:  # LEFT
        purple.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and purple.x + VEL + purple.width < WIDTH:  # RIGHT
        purple.x += VEL
    if keys_pressed[pygame.K_UP] and purple.y - VEL > 0:  # UP
        purple.y -= VEL
    if keys_pressed[pygame.K_DOWN] and purple.y + VEL + purple.height < HEIGHT - 10:  # DOWN
        purple.y += VEL


def handle_bullets(yellow_bullets, purple_bullets, yellow, purple):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if purple.colliderect(bullet):
            pygame.event.post(pygame.event.Event(PURPLE_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in purple_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            purple_bullets.remove(bullet)
        elif bullet.x < 0:
            purple_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(2000)


def main():
    purple = pygame.Rect(1250, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    purple_bullets = []
    yellow_bullets = []

    purple_health = 10
    yellow_health = 10
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(purple_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(purple.x, purple.y + purple.height // 2 - 2, 10, 5)
                    purple_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            if event.type == PURPLE_HIT:
                purple_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
        winner_text = ""
        if purple_health <= 0:
            winner_text = "Yellow wins"
        if yellow_health <= 0:
            winner_text = "Purple wins"
        if winner_text != "":
            draw_winner(winner_text)
            break
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        purple_handle_movement(keys_pressed, purple)

        handle_bullets(yellow_bullets, purple_bullets, yellow, purple)
        draw_window(purple, yellow, purple_bullets, yellow_bullets, purple_health, yellow_health)
    main()


if __name__ == "__main__":
    main()
