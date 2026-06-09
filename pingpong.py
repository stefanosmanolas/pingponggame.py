
import pygame
import sys
import random

pygame.init()

WIDTH = 600
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

BLUE = (0, 150, 255)
RED = (255, 80, 80)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font_big = pygame.font.SysFont("Arial", 90)
font_small = pygame.font.SysFont("Arial", 25)

paddle_img = pygame.image.load("paddle.png")
paddle_img = pygame.transform.scale(paddle_img, (20, 130))

ball_img = pygame.image.load("ball.png")
ball_img = pygame.transform.scale(ball_img, (30, 30))

clock = pygame.time.Clock()

state = "menu"
countdown = 3
countdown_started = False
freeze_timer = 0
game_started = False

p1_x = 20
p2_x = WIDTH - 40

p1_y = HEIGHT // 2 - 60
p2_y = HEIGHT // 2 - 60

ball_x = WIDTH // 2
ball_y = HEIGHT // 2

ball_dx = 0
ball_dy = 0

speed = 7

p1_score = 0
p2_score = 0


def reset_ball():
    global ball_x, ball_y, ball_dx, ball_dy
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_dx = random.choice([-3, 3])
    ball_dy = random.choice([-3, 3])


running = True

while running:
    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                state = "menu"

    keys = pygame.key.get_pressed()

    # ================= MENU =================
    if state == "menu":
        screen.fill(BLUE)

        title = font_big.render("PING PONG", True, WHITE)
        screen.blit(title, (80, 200))

        play_btn = pygame.Rect(200, 400, 200, 80)
        pygame.draw.rect(screen, WHITE, play_btn)

        play_text = font_small.render("PLAY", True, BLACK)
        screen.blit(play_text, (275, 425))

        mx, my = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if play_btn.collidepoint(mx, my) and click[0]:
            state = "game"
            countdown = 3
            countdown_started = True
            game_started = False

    # ================= GAME =================
    elif state == "game":

        # background half red / half blue
        pygame.draw.rect(screen, BLUE, (0, 0, WIDTH // 2, HEIGHT))
        pygame.draw.rect(screen, RED, (WIDTH // 2, 0, WIDTH // 2, HEIGHT))

        hint = font_small.render("BACKSPACE = MENU", True, WHITE)
        screen.blit(hint, (10, 10))

        # movement
        if keys[pygame.K_w]:
            p1_y -= speed
        if keys[pygame.K_s]:
            p1_y += speed

        if keys[pygame.K_UP]:
            p2_y -= speed
        if keys[pygame.K_DOWN]:
            p2_y += speed

        p1_y = max(0, min(HEIGHT - 130, p1_y))
        p2_y = max(0, min(HEIGHT - 130, p2_y))

        # ================= COUNTDOWN ONCE =================
        if countdown_started:
            text = font_big.render(str(countdown), True, WHITE)
            screen.blit(text, (WIDTH//2 - 30, HEIGHT//2 - 60))

            pygame.display.update()
            pygame.time.delay(1000)

            countdown -= 1

            if countdown <= 0:
                countdown_started = False
                freeze_timer = pygame.time.get_ticks()

        # ================= FREEZE 1 SECOND =================
        elif not game_started:
            if pygame.time.get_ticks() - freeze_timer < 1000:
                pass
            else:
                reset_ball()
                game_started = True

        # ================= GAME LOGIC =================
        else:
            ball_x += ball_dx
            ball_y += ball_dy

            if ball_y <= 0 or ball_y + 30 >= HEIGHT:
                ball_dy *= -1

            ball_rect = pygame.Rect(ball_x, ball_y, 30, 30)
            p1_rect = pygame.Rect(p1_x, p1_y, 20, 130)
            p2_rect = pygame.Rect(p2_x, p2_y, 20, 130)

            if ball_rect.colliderect(p1_rect):
                ball_dx = abs(ball_dx)

            if ball_rect.colliderect(p2_rect):
                ball_dx = -abs(ball_dx)

            if ball_x <= 0:
                p2_score += 1
                reset_ball()

            if ball_x + 30 >= WIDTH:
                p1_score += 1
                reset_ball()

            screen.blit(ball_img, (ball_x, ball_y))

        # draw paddles ALWAYS
        screen.blit(paddle_img, (p1_x, p1_y))
        screen.blit(paddle_img, (p2_x, p2_y))

        score = font_small.render(f"{p1_score}   {p2_score}", True, WHITE)
        screen.blit(score, (WIDTH//2 - 30, 20))

    pygame.display.update()

pygame.quit()
sys.exit()
