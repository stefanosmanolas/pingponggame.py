import pygame
import sys

pygame.init()

WIDTH = 500
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

BLUE = (135, 206, 235)

ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, (30, 30))

paddle = pygame.image.load("padle.png")
paddle = pygame.transform.scale(paddle, (20, 120))

ball_x = WIDTH // 2
ball_y = HEIGHT // 2

ball_dx = 4
ball_dy = 4

p1_x = 20
p1_y = HEIGHT // 2 - 60

p2_x = WIDTH - 40
p2_y = HEIGHT // 2 - 60

speed = 6

clock = pygame.time.Clock()

running = True

while running:
    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        p1_y -= speed
    if keys[pygame.K_s]:
        p1_y += speed

    if keys[pygame.K_UP]:
        p2_y -= speed
    if keys[pygame.K_DOWN]:
        p2_y += speed

    if p1_y < 0:
        p1_y = 0
    if p1_y + 120 > HEIGHT:
        p1_y = HEIGHT - 120

    if p2_y < 0:
        p2_y = 0
    if p2_y + 120 > HEIGHT:
        p2_y = HEIGHT - 120

    ball_x += ball_dx
    ball_y += ball_dy

    if ball_y <= 0 or ball_y + 30 >= HEIGHT:
        ball_dy *= -1

    ball_rect = pygame.Rect(ball_x, ball_y, 30, 30)
    p1_rect = pygame.Rect(p1_x, p1_y, 20, 120)
    p2_rect = pygame.Rect(p2_x, p2_y, 20, 120)

    if ball_rect.colliderect(p1_rect):
        ball_dx *= -1
        ball_x = p1_x + 20

    if ball_rect.colliderect(p2_rect):
        ball_dx *= -1
        ball_x = p2_x - 30

    if ball_x <= 0 or ball_x >= WIDTH:
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2

    screen.fill(BLUE)

    screen.blit(ball, (ball_x, ball_y))
    screen.blit(paddle, (p1_x, p1_y))
    screen.blit(paddle, (p2_x, p2_y))

    pygame.display.update()

pygame.quit()
sys.exit()
