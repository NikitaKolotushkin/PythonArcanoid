import pygame
from random import randrange as rnd

WIDTH, HEIGHT = 1200, 800
fps = 60
platform_width = 330
platform_height = 35
platform_speed = 15
platform = pygame.Rect(WIDTH // 2 - platform_width // 2, HEIGHT - platform_height - 10, platform_width, platform_height)

pygame.init()

game = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
img = pygame.image.load('img/bg.png').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    game.blit(img, (0, 0))
    pygame.draw.rect(game, pygame.Color('darkblue'), platform)

    pygame.display.flip()
    clock.tick(fps)