import pygame
import sys
import random

pygame.init()

WIDTH = 600
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

WHITE = (255,255,255)
BLACK = (0,0,0)

font_big = pygame.font.SysFont("Arial", 70)
font_small = pygame.font.SysFont("Arial", 24)

colors = [
    (255,255,255),
    (0,255,0),
    (255,0,255),
    (255,255,0),
    (0,150,255),
    (255,80,80),
    (255,140,0),
    (0,255,255),
    (0,0,0)
]

state = "menu"

p1_x = 20
p2_x = WIDTH - 40

p1_y = HEIGHT//2 - 60
p2_y = HEIGHT//2 - 60

ball_x = WIDTH//2
ball_y = HEIGHT//2

ball_dx = 3
ball_dy = 3

p1_score = 0
p2_score = 0

speed = 7

clock = pygame.time.Clock()

paddle_img = pygame.image.load("padle.png")
ball_img = pygame.image.load("ball.png")
bg_img = pygame.image.load("back.png")
shop_img = pygame.image.load("shop.png")

paddle_img = pygame.transform.scale(paddle_img,(20,130))
ball_img = pygame.transform.scale(ball_img,(30,30))
bg_img = pygame.transform.scale(bg_img,(WIDTH,HEIGHT))
shop_img = pygame.transform.scale(shop_img,(WIDTH,HEIGHT))

use_img = {"p1":True,"p2":True,"ball":True,"bg":True}

p1_color = WHITE
p2_color = WHITE
ball_color = WHITE
bg_color = (0,150,255)

equipped = {
    "p1":"classic",
    "p2":"classic",
    "ball":"classic",
    "bg":"classic"
}

waiting = False
last_goal = 0


def reset_ball():
    global ball_x, ball_y, ball_dx, ball_dy, waiting
    ball_x = WIDTH//2
    ball_y = HEIGHT//2
    ball_dx = random.choice([-3,3])
    ball_dy = random.choice([-3,3])
    waiting = False


running = True

while running:
    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                state = "menu"

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my = pygame.mouse.get_pos()

            if state == "menu":
                if pygame.Rect(200,380,200,80).collidepoint(mx,my):
                    state = "game"
                    reset_ball()

                if pygame.Rect(200,480,200,80).collidepoint(mx,my):
                    state = "shop"

            elif state == "shop":

                if pygame.Rect(40,120,90,30).collidepoint(mx,my):
                    use_img["p1"] = True
                    equipped["p1"] = "classic"
                    p1_color = WHITE

                if pygame.Rect(40,280,90,30).collidepoint(mx,my):
                    use_img["p2"] = True
                    equipped["p2"] = "classic"
                    p2_color = WHITE

                if pygame.Rect(40,440,90,30).collidepoint(mx,my):
                    use_img["ball"] = True
                    equipped["ball"] = "classic"
                    ball_color = WHITE

                if pygame.Rect(40,600,90,30).collidepoint(mx,my):
                    use_img["bg"] = True
                    equipped["bg"] = "classic"
                    bg_color = (0,150,255)

                for i,c in enumerate(colors):

                    if pygame.Rect(200+i*35,120,28,28).collidepoint(mx,my):
                        use_img["p1"] = False
                        p1_color = c
                        equipped["p1"] = "color"

                    if pygame.Rect(200+i*35,280,28,28).collidepoint(mx,my):
                        use_img["p2"] = False
                        p2_color = c
                        equipped["p2"] = "color"

                    if pygame.Rect(200+i*35,440,28,28).collidepoint(mx,my):
                        use_img["ball"] = False
                        ball_color = c
                        equipped["ball"] = "color"

                    if pygame.Rect(200+i*35,600,28,28).collidepoint(mx,my):
                        use_img["bg"] = False
                        bg_color = c
                        equipped["bg"] = "color"

    keys = pygame.key.get_pressed()

    if state == "menu":
        screen.fill((0,150,255))

        screen.blit(font_big.render("PING PONG",True,WHITE),(80,200))

        pygame.draw.rect(screen,WHITE,(200,380,200,80))
        pygame.draw.rect(screen,WHITE,(200,480,200,80))

        screen.blit(font_small.render("PLAY",True,BLACK),(270,405))
        screen.blit(font_small.render("SHOP",True,BLACK),(270,505))

    elif state == "shop":

        screen.blit(shop_img,(0,0))

        screen.blit(font_big.render("SHOP",True,BLACK),(230,20))
        screen.blit(font_small.render("BACKSPACE = MENU",True,BLACK),(10,5))

        screen.blit(font_small.render("P1",True,BLACK),(20,125))
        screen.blit(font_small.render("P2",True,BLACK),(20,285))
        screen.blit(font_small.render("BALL",True,BLACK),(20,445))
        screen.blit(font_small.render("BG",True,BLACK),(20,605))

        boxes = [
            pygame.Rect(40,120,90,30),
            pygame.Rect(40,280,90,30),
            pygame.Rect(40,440,90,30),
            pygame.Rect(40,600,90,30)
        ]

        for b in boxes:
            pygame.draw.rect(screen,BLACK,b,2)

        screen.blit(font_small.render("classic",True,BLACK),(52,127))
        screen.blit(font_small.render("classic",True,BLACK),(52,287))
        screen.blit(font_small.render("classic",True,BLACK),(52,447))
        screen.blit(font_small.render("classic",True,BLACK),(52,607))

        for i,c in enumerate(colors):

            r1 = pygame.Rect(200+i*35,120,28,28)
            r2 = pygame.Rect(200+i*35,280,28,28)
            r3 = pygame.Rect(200+i*35,440,28,28)
            r4 = pygame.Rect(200+i*35,600,28,28)

            pygame.draw.rect(screen,c,r1)
            pygame.draw.rect(screen,c,r2)
            pygame.draw.rect(screen,c,r3)
            pygame.draw.rect(screen,c,r4)

            if not use_img["p1"] and p1_color == c:
                pygame.draw.rect(screen,WHITE,r1,2)
            if not use_img["p2"] and p2_color == c:
                pygame.draw.rect(screen,WHITE,r2,2)
            if not use_img["ball"] and ball_color == c:
                pygame.draw.rect(screen,WHITE,r3,2)
            if not use_img["bg"] and bg_color == c:
                pygame.draw.rect(screen,WHITE,r4,2)

    elif state == "game":

        if use_img["bg"]:
            screen.blit(bg_img,(0,0))
        else:
            screen.fill(bg_color)

        if keys[pygame.K_w]:
            p1_y -= speed
        if keys[pygame.K_s]:
            p1_y += speed
        if keys[pygame.K_UP]:
            p2_y -= speed
        if keys[pygame.K_DOWN]:
            p2_y += speed

        p1_y = max(0,min(HEIGHT-130,p1_y))
        p2_y = max(0,min(HEIGHT-130,p2_y))

        if waiting:
            if pygame.time.get_ticks() - last_goal > 1000:
                reset_ball()
        else:
            ball_x += ball_dx
            ball_y += ball_dy

            if ball_y <= 0 or ball_y+30 >= HEIGHT:
                ball_dy *= -1

            p1_rect = pygame.Rect(p1_x,p1_y,20,130)
            p2_rect = pygame.Rect(p2_x,p2_y,20,130)
            ball_rect = pygame.Rect(ball_x,ball_y,30,30)

            if ball_rect.colliderect(p1_rect):
                ball_dx = abs(ball_dx)

            if ball_rect.colliderect(p2_rect):
                ball_dx = -abs(ball_dx)

            if ball_x <= 0:
                p2_score += 1
                waiting = True
                last_goal = pygame.time.get_ticks()

            if ball_x + 30 >= WIDTH:
                p1_score += 1
                waiting = True
                last_goal = pygame.time.get_ticks()

        if use_img["p1"]:
            screen.blit(paddle_img,(p1_x,p1_y))
        else:
            pygame.draw.rect(screen,p1_color,(p1_x,p1_y,20,130))

        if use_img["p2"]:
            screen.blit(paddle_img,(p2_x,p2_y))
        else:
            pygame.draw.rect(screen,p2_color,(p2_x,p2_y,20,130))

        if use_img["ball"]:
            screen.blit(ball_img,(ball_x,ball_y))
        else:
            pygame.draw.ellipse(screen,ball_color,(ball_x,ball_y,30,30))

        screen.blit(font_small.render(f"{p1_score} {p2_score}",True,WHITE),(WIDTH//2-20,20))

    pygame.display.update()

pygame.quit()
sys.exit()
