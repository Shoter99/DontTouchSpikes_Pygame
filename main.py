from email.mime import image
from platform import win32_edition
import pygame, sys, random, os
from Bird import Bird
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
screen = pygame.display.set_mode((WIDTH, HEIGHT))

SKY_SURFACE = pygame.image.load(os.path.join('Assets', 'bg.png'))
SKY_SURFACE = pygame.transform.scale(SKY_SURFACE, (WIDTH, HEIGHT))





def draw_window(win, bird):
    win.fill(WHITE)
    win.blit(SKY_SURFACE, (0,0))
    bird.draw(win)
    pygame.display.update()




#Game Loop
def main():
    clock = pygame.time.Clock()
    pygame.display.set_caption("Dont touch spikes!")
    FPS = 60
    running = True
    bird = Bird(200,200)
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    bird.jump()
        
        bird.move()
        draw_window(screen, bird)

    pygame.quit()

if __name__ == '__main__':
    main()
