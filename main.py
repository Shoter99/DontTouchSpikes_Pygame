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
from pygame.math import Vector2
pygame.init()

#COLORS

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

WIDTH, HEIGHT = 400, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
class Player:
    def __init__(self) -> None:
        self.position = Vector2.xy

def draw_window():
    WIN.fill(WHITE)
    
    pygame.display.update()

#Game Loop
def main():
    clock = pygame.time.Clock()
    pygame.display.set_caption("Dont touch spikes!")
    FPS = 60
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        

        draw_window()

    pygame.quit()

if __name__ == '__main__':
    main()