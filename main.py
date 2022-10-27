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
    pygame.image.load(os.path.join('Assets', 'bird2.png')),
    pygame.image.load(os.path.join('Assets', 'bird1.png')),
    pygame.image.load(os.path.join('Assets', 'bird3.png'))
    ]

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
        self.dir = 1
    def jump(self):
        self.vel = -12
        self.tick_count = 0
        self.height = self.y
    def move(self):
        self.tick_count +=1 
        
        #calculating x vel
        if self.x > WIDTH - 20:
            self.dir = 1
        elif self.x < 0 :
            self.dir = -1
        
        velx = self.vel/2 * self.dir
        
        self.x += velx
        d = self.vel*self.tick_count + 1.5*self.tick_count**2
        if d >= 7:
            d = 7
        elif d < 0:
            d -= 2
        
        self.y = self.y + d

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        # else:
        #     if self.tilt > -30:
        #         self.tilt -= self.ROT_VEL
        if self.y > HEIGHT - 20:
            self.y = HEIGHT - 20
        if self.y < 0:
            self.y = 0
    def draw(self, win):
        self.img_count += 1
        
        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME*4+1:
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2
        
        if self.dir == 1:
            self.img = pygame.transform.flip(self.img, True, False)
        

        rotated_img = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_img.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)
        
        win.blit(rotated_img, new_rect.topleft)
    
    def get_mask(self):
        return pygame.mask.from_surface(self.img)

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
