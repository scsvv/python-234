import pygame
from sys import exit
from random import randint
from local import *

pygame.init()
pygame.display.set_caption("Snake")

# ? Local
window = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()


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

    if snake[0].bottom > WINDOW_SIZE[1]:
        snake[0].bottom = 0
    elif snake[0].top < 0:
        snake[0].top = WINDOW_SIZE[1]
    elif snake[0].left < 0:
        snake[0].right = WINDOW_SIZE[0]
    elif snake[0].left > WINDOW_SIZE[0]:
        snake[0].left = 0

    for i in range(len(snake)-1, 0, -1):
        snake[i].x = snake[i-1].x
        snake[i].y = snake[i-1].y

    snake[0].move_ip(DIRECTION)


def pickup(apple, snake, score):
    if snake[0].colliderect(apple):
        apple.x = randint(30, WINDOW_SIZE[0])
        apple.y = randint(30, WINDOW_SIZE[1])
        snake.append(snake[1].copy())
        score += 10
        return score
    return score


def isPlay(snake):
    for shape in snake[1:]:
        if snake[0].colliderect(shape):
            return False
    return True


def display_score(score):
    font = pygame.font.SysFont(None, 16)
    text = font.render(f'SCORE: {score}', True, (255, 255, 255))
    text_rect = text.get_rect(left=5, top=5)
    window.blit(text, text_rect)


def display_message(message):
    font = pygame.font.SysFont(None, 64)
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect(center=(WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2))
    window.blit(text, text_rect)


if __name__ == "__main__":
    DIRECTION = [SPEED, 0]
    GAME_SCORE = 0

    head_image, head_rect = load_png('./img/head.png', 400, 300)
    apple_image, apple_rect = load_png('./img/apple.png', 200, 200)
    body_image, body_rect = load_png('./img/body.png', 370, 300)

    snake = [head_rect, body_rect]

    while True:
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        if isPlay(snake):
            move(snake, pygame.key.get_pressed())
            GAME_SCORE = pickup(apple_rect, snake, GAME_SCORE)
            display_score(GAME_SCORE)
            window.blit(head_image, head_rect)
            window.blit(apple_image, apple_rect)

            for body in snake[1:]:
                window.blit(body_image, body)
        else:
            display_message('GAME OVER')

        pygame.display.update()
        clock.tick(10)
