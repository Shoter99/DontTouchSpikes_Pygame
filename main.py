import pygame, sys, random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
pygame.init()

#COLORS

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

WIDTH, HEIGHT = 400, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
FPS = 60
#Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    
    screen.fill(WHITE)

    pygame.draw.circle(screen, BLUE, (200,300), 75)

    pygame.display.flip()

pygame.quit()
    