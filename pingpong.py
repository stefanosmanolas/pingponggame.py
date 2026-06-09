import pygame
import sys
import random

pygame.init()

WIDTH = 500
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

BLUE = (0, 150, 255)
RED = (255, 80, 80)
WHITE = (255, 255, 255)

font = pygame.font.SysFont("Arial", 40)

paddle_img = pygame.image.load("padle.png")
paddle_img = pygame.transform.scale(paddle_img, (20, 120))

ball_img = pygame.image.load("ball.png")
ball_img = pygame.transform.scale(ball_img, (30, 30))

p1_x = 20
p2_x = WIDTH - 40

p1_y = HEIGHT // 2 - 60
p2_y = HEIGHT // 2 - 60

ball_x = WIDTH // 2
ball_y = HEIGHT // 2

ball_dx = 3
ball_dy = 3

p1_score = 0
p2_score = 0

speed = 6

clock = pygame.time.Clock()

serve_owner = random.choice(["p1", "p2"])

def spawn_ball():
    global ball_x, ball_y, ball_dx, ball_dy, serve_owner

    ball_y = random.randint(100, HEIGHT - 100)

    if serve_owner == "p1":
        ball_x = p1_x + 40
        ball_dx = 3
    else:
        ball_x = p2_x - 40
        ball_dx = -3

    ball_dy = random.choice([-3, -2, 2, 3])

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

    p1_y = max(0, min(HEIGHT - 120, p1_y))
    p2_y = max(0, min(HEIGHT - 120, p2_y))

    ball_x += ball_dx
    ball_y += ball_dy

    if ball_y <= 0 or ball_y + 30 >= HEIGHT:
        ball_dy *= -1

    ball_rect = pygame.Rect(ball_x, ball_y, 30, 30)
    p1_rect = pygame.Rect(p1_x, p1_y, 20, 120)
    p2_rect = pygame.Rect(p2_x, p2_y, 20, 120)

    if ball_rect.colliderect(p1_rect):
        ball_dx = abs(ball_dx)

    if ball_rect.colliderect(p2_rect):
        ball_dx = -abs(ball_dx)

    if ball_x <= 0:
        p2_score += 1
        serve_owner = "p2"
        pygame.time.delay(1000)
        spawn_ball()

    if ball_x + 30 >= WIDTH:
        p1_score += 1
        serve_owner = "p1"
        pygame.time.delay(1000)
        spawn_ball()

    screen.fill(BLUE)

    pygame.draw.rect(screen, BLUE, (0, 0, WIDTH // 2, HEIGHT))
    pygame.draw.rect(screen, RED, (WIDTH // 2, 0, WIDTH // 2, HEIGHT))

    screen.blit(paddle_img, (p1_x, p1_y))
    screen.blit(paddle_img, (p2_x, p2_y))
    screen.blit(ball_img, (ball_x, ball_y))

    score_text = font.render(f"{p1_score}   {p2_score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 40, 20))

    pygame.display.update()

pygame.quit()
sys.exit()
