import pygame
import sys

pygame.init()

WIDTH = 500
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

BLUE = (135, 206, 235)
WHITE = (255, 255, 255)

font = pygame.font.SysFont("Arial", 30)

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

    ball_x += ball_dx
    ball_y += ball_dy

    if ball_y <= 0 or ball_y + 30 >= HEIGHT:
        ball_dy *= -1

    if ball_x <= 0 or ball_x + 30 >= WIDTH:
        ball_dx *= -1

    screen.fill(BLUE)

    screen.blit(ball, (ball_x, ball_y))
    screen.blit(paddle, (p1_x, p1_y))
    screen.blit(paddle, (p2_x, p2_y))

    pygame.display.update()

pygame.quit()
sys.exit()
