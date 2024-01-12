import pygame
from sys import exit
from random import randint
from local import *


class SnakeGame:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.DIRECTION = [SPEED, 0]
        self.GAME_SCORE = 0
        self.head_image, self.head_rect = self.load_png(
            './img/head.png', 400, 300)
        self.apple_image, self.apple_rect = self.load_png(
            './img/apple.png', 200, 200)
        self.body_image, self.body_rect = self.load_png(
            './img/body.png', 370, 300)
        self.snake = [self.head_rect, self.body_rect]

    def load_png(self, src, x, y):
        image = pygame.image.load(src).convert()
        image = pygame.transform.scale(image, (30, 30))
        rect = image.get_rect(center=(x, y))
        transparent = image.get_at((0, 0))
        image.set_colorkey(transparent)
        return image, rect

    def move(self, keys):
        if (keys[K_UP] or keys[K_w]) and self.DIRECTION[0]:
            self.DIRECTION = [0, -SPEED]
        elif (keys[K_DOWN] or keys[K_s]) and self.DIRECTION[0]:
            self.DIRECTION = [0, SPEED]
        elif (keys[K_RIGHT] or keys[K_d]) and self.DIRECTION[1]:
            self.DIRECTION = [SPEED, 0]
        elif (keys[K_LEFT] or keys[K_a]) and self.DIRECTION[1]:
            self.DIRECTION = [-SPEED, 0]

        if self.snake[0].bottom > WINDOW_SIZE[1]:
            self.snake[0].bottom = 0
        elif self.snake[0].top < 0:
            self.snake[0].top = WINDOW_SIZE[1]
        elif self.snake[0].left < 0:
            self.snake[0].right = WINDOW_SIZE[0]
        elif self.snake[0].left > WINDOW_SIZE[0]:
            self.snake[0].left = 0

        for i in range(len(self.snake)-1, 0, -1):
            self.snake[i].x = self.snake[i-1].x
            self.snake[i].y = self.snake[i-1].y

        self.snake[0].move_ip(self.DIRECTION)

    def pickup(self):
        if self.snake[0].colliderect(self.apple_rect):
            self.apple_rect.x = randint(30, WINDOW_SIZE[0])
            self.apple_rect.y = randint(30, WINDOW_SIZE[1])
            self.snake.append(self.snake[1].copy())
            self.GAME_SCORE += 10

    def is_play(self):
        for shape in self.snake[1:]:
            if self.snake[0].colliderect(shape):
                return False
        return True

    def display_score(self):
        font = pygame.font.SysFont(None, 16)
        text = font.render(f'SCORE: {self.GAME_SCORE}', True, (255, 255, 255))
        text_rect = text.get_rect(left=5, top=5)
        self.window.blit(text, text_rect)

    def display_message(self, message):
        font = pygame.font.SysFont(None, 64)
        text = font.render(message, True, (255, 255, 255))
        text_rect = text.get_rect(
            center=(WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2))
        self.window.blit(text, text_rect)

    def run(self):
        while True:
            self.window.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            if self.is_play():
                self.move(pygame.key.get_pressed())
                self.pickup()
                self.display_score()
                self.window.blit(self.head_image, self.head_rect)
                self.window.blit(self.apple_image, self.apple_rect)

                for body in self.snake[1:]:
                    self.window.blit(self.body_image, body)
            else:
                self.display_message('GAME OVER')

            pygame.display.update()
            self.clock.tick(10)


if __name__ == "__main__":
    game = SnakeGame()
    game.run()
