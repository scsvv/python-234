import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()
pygame.display.set_caption("Snake")

# ? Local
WINDOW_SIZE = (1080, 720)
window = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 16)


def load_png(src, x, y):
    image = pygame.image.load(src).convert()
    image = pygame.transform.scale(image, (30, 30))
    rect = image.get_rect(center=(x, y))
    trasparent = image.get_at((0, 0))
    image.set_colorkey(trasparent)

    return image, rect


def move(snake, keys):
    global DIRECTION, SPEED

    if (keys[K_UP] or keys[K_w]) and DIRECTION[0]:
        DIRECTION = [0, -SPEED]
    elif (keys[K_DOWN] or keys[K_s]) and DIRECTION[0]:
        DIRECTION = [0, SPEED]
    elif (keys[K_RIGHT] or keys[K_d]) and DIRECTION[1]:
        DIRECTION = [SPEED, 0]
    elif (keys[K_LEFT] or keys[K_a]) and DIRECTION[1]:
        DIRECTION = [-SPEED, 0]

    if snake.bottom > WINDOW_SIZE[1]:
        snake.bottom = 0
    elif snake.top < 0:
        snake.top = WINDOW_SIZE[1]
    elif snake.left < 0:
        snake.right = WINDOW_SIZE[0]
    elif snake.left > WINDOW_SIZE[0]:
        snake.left = 0

    snake.move_ip(DIRECTION)


def pickup(apple, snake):
    global GAME_SCORE
    if snake.colliderect(apple):
        apple.x = randint(30, WINDOW_SIZE[0])
        apple.x = randint(30, WINDOW_SIZE[1])
        GAME_SCORE += 10


def display_score(score):
    text = font.render(f'SCORE: {score}', True, (255, 255, 255))
    text_rect = text.get_rect(left=5, top=5)
    window.blit(text, text_rect)


if __name__ == "__main__":
    SPEED = 30
    DIRECTION = [SPEED, 0]
    GAME_SCORE = 0

    head_image, head_rect = load_png('./img/head.png', 400, 300)
    apple_image, apple_rect = load_png('./img/apple.png', 200, 200)
    body_image, body_rect = load_png('./img/body.png', 200, 200)

    while True:
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        move(head_rect, pygame.key.get_pressed())
        pickup(apple_rect, head_rect)
        display_score(GAME_SCORE)
        window.blit(head_image, head_rect)
        window.blit(apple_image, apple_rect)
        pygame.display.update()
        clock.tick(10)
