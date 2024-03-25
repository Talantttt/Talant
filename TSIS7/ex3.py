import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

BALL_RADIUS = 25
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_speed = 20

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(ball_y - ball_speed, BALL_RADIUS)
            elif event.key == pygame.K_DOWN:
                ball_y = min(ball_y + ball_speed, SCREEN_HEIGHT - BALL_RADIUS)
            elif event.key == pygame.K_LEFT:
                ball_x = max(ball_x - ball_speed, BALL_RADIUS)
            elif event.key == pygame.K_RIGHT:
                ball_x = min(ball_x + ball_speed, SCREEN_WIDTH - BALL_RADIUS)

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

    pygame.display.flip()

pygame.quit()
