from platform import win32_edition
import pygame, sys, random, os
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

BIRD_SURFACES = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('Assets', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('Assets', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('Assets', 'bird3.png')))
    ]
def draw_window():
    screen.fill(WHITE)
    screen.blit(SKY_SURFACE, (0,0))
    screen.blit(BIRD_SURFACES[0], (WIDTH/2, HEIGHT/2))
    pygame.display.update()

class Bird:
    IMGS = BIRD_SURFACES
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]
    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y
    def move(self):
        self.tick_count +=1 
    def draw_bird(self):
        screen.blit(self.IMGS[self.img_count], (self.x, self.y))





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