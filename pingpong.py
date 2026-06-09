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

ball_x = WIDTH // 2 - 15
ball_y = HEIGHT // 2 - 15

p1_score = 0
p2_score = 0

p1_x = 20
p1_y = HEIGHT // 2 - 60

p2_x = WIDTH - 40
p2_y = HEIGHT // 2 - 60

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLUE)

    score_text = font.render(f"{p1_score}   {p2_score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 30, 20))

    screen.blit(ball, (ball_x, ball_y))

    screen.blit(paddle, (p1_x, p1_y))
    screen.blit(paddle, (p2_x, p2_y))

    pygame.display.update()

pygame.quit()
sys.exit()
