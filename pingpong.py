import pygame
import sys

pygame.init()

WIDTH = 500
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Το Παιχνίδι Μου")

BLUE = (135, 206, 235)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLUE)
    pygame.display.flip()

pygame.quit()
sys.exit()