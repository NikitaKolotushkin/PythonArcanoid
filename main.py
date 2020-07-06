import pygame
from random import randrange as rnd

WIDTH, HEIGHT = 1200, 800
fps = 60

# PLATFORM
platform_width = 330
platform_height = 35
platform_speed = 15
platform = pygame.Rect(WIDTH // 2 - platform_width // 2, HEIGHT - platform_height - 10, platform_width, platform_height)

# BALL
ball_radius = 20
ball_speed = 6
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
dx, dy = 1, -1

pygame.init()

game = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
img = pygame.image.load('img/bg.png').convert()

# GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    game.blit(img, (0, 0))

    # DRAWING
    pygame.draw.rect(game, pygame.Color('darkblue'), platform)
    pygame.draw.circle(game, pygame.Color('white'), ball.center, ball_radius)

    # BALL MOVEMENT
    ball.x += ball_speed * dx
    ball.y += ball_speed * dy

    # BALL LEFT AND RIGHT COLLISION
    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
        dx = -dx
    
    # BALL TOP COLLISION
    if ball.centery < ball_radius:
        dy = -dy

    # BALL PLATFORM COLLISION
    if ball.colliderect(platform) and dy > 0:
        dy = -dy

    # CONTROL
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and platform.left > 0:
        platform.left -= platform_speed

    if key[pygame.K_RIGHT] and platform.right < WIDTH:
        platform.right += platform_speed

    # SCREEN UPDATING
    pygame.display.flip()
    clock.tick(fps)