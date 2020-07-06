import pygame

WIDTH, HEIGHT = 1200, 800
fps = 60

pygame.init()

game = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
img = pygame.image.load('img/bg.png').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    game.blit(img, (0, 0))

    pygame.display.flip()
    clock.tick(fps)