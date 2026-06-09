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

ball_x = WIDTH // 2 - 15
ball_y = HEIGHT // 2 - 15

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLUE)
    screen.blit(ball, (ball_x, ball_y))

    pygame.display.update()

pygame.quit()
sys.exit()
