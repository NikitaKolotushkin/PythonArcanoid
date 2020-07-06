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

# BLOCKS
block_list = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(10) for j in range(4)]

pygame.init()

game = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
img = pygame.image.load('img/bg.png').convert()

# COLLISION DETECTER
def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx

    return dx, dy

# GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    game.blit(img, (0, 0))

    # DRAWING
    [pygame.draw.rect(game, color_list[color], block) for color, block in enumerate(block_list)]
    pygame.draw.rect(game, pygame.Color('darkviolet'), platform)
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
        dx, dy = detect_collision(dx, dy, ball, platform)

    # BALL BLOCKS COLLISION
    hit_index = ball.collidelist(block_list)
    if hit_index != -1:
        hit_rect = block_list.pop(hit_index)
        hit_color = color_list.pop(hit_index)
        dx, dy = detect_collision(dx, dy, ball, hit_rect)
        
        # SPECIAL EFFECTS
        hit_rect.inflate_ip(ball.width * 3, ball.height * 3)
        pygame.draw.rect(game, hit_color, hit_rect)
        fps += 2
    
    # WIN, GAME OVER
    if ball.bottom > HEIGHT:
        print("GAME OVER!")
        exit()
    elif not len(block_list):
        print("WIN!")
        exit()

    # CONTROL
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and platform.left > 0:
        platform.left -= platform_speed

    if key[pygame.K_RIGHT] and platform.right < WIDTH:
        platform.right += platform_speed

    # SCREEN UPDATING
    pygame.display.flip()
    clock.tick(fps)