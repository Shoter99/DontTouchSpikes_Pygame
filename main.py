from email.mime import image
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
    pygame.transform.scale2x(pygame.image.load(os.path.join('Assets', 'player1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('Assets', 'player2.png')))
    ]
SPIKE_SURFACE = pygame.image.load(os.path.join('Assets', 'spike.png'))
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
        self.vel = -6
        self.tick_count = 0
        self.height = self.y
    def move(self):
        self.tick_count +=.25
        
        #calculating x vel
        if self.x > WIDTH - 40:
            self.dir = 1
        elif self.x < 0 :
            self.dir = -1
        
        velx = self.vel/1.5 * self.dir
        
        self.x += velx


        d = self.vel*self.tick_count + 1.5*self.tick_count**2
        if d >= 5:
            d = 5
        elif d < 0:
            d -= 2
        
        self.y = self.y + d

        if self.y > self.height:
            self.tilt = 1
        else:
            self.tilt = -1

        if self.y > HEIGHT - 20:
            self.y = HEIGHT - 20
        if self.y < 0:
            self.y = 0
    def draw(self, win):
        self.img_count += 1
        
        if self.tilt <= 0:
            self.img = self.IMGS[1]
        else:
            self.img = self.IMGS[0]
        
        if self.dir == 1:
            self.img = pygame.transform.flip(self.img, True, False)
        

        # rotated_img = pygame.transform.rotate(self.img, self.tilt)
        # new_rect = rotated_img.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)
        
        win.blit(self.img, (self.x, self.y))
    
    def get_mask(self):
        return pygame.mask.from_surface(self.img)
    def get_dir(self):
        return self.dir
    def get_rect(self):
        return pygame.Rect(self.x,self.y, 15,15)
class Spike:
    def __init__(self, x,y, rot=1):
        self.x = x
        self.y = y
        self.rotation = rot
        self.img = SPIKE_SURFACE
        self.rotate()
    def rotate(self):
        if self.rotation:
            self.img = pygame.transform.rotate(self.img, -90)
        else:
            self.img = pygame.transform.rotate(self.img, 90)
    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
    def get_rect(self):
        return pygame.Rect(self.x, self.y, 10,25)


def draw_window(win, bird,spikes):
    win.fill(WHITE)
    win.blit(SKY_SURFACE, (0,0))
    bird.draw(win)
    for spike in spikes:
        spike.draw(win)
    pygame.display.update()


def generate_left_side_spikes():
    spike_free_area = random.randint(0, HEIGHT-192)
    spikes = []
    for i in range(0,spike_free_area, 32):
        spikes.append(Spike(0,i))
    for i in range(spike_free_area+160,HEIGHT,32):
        spikes.append(Spike(0,i))
    return spikes
def generate_right_side_spikes():
    spike_free_area = random.randint(0, HEIGHT-192)
    spikes = []
    for i in range(0,spike_free_area, 32):
        spikes.append(Spike(WIDTH-32,i,0))
    for i in range(spike_free_area+160,HEIGHT,32):
        spikes.append(Spike(WIDTH-32,i,0))
    return spikes
#Game Loop
def main():
    clock = pygame.time.Clock()
    pygame.display.set_caption("Dont touch spikes!")
    FPS = 60
    running = True
    round_start = False
    bird = Bird(160,250)
    spikes = generate_left_side_spikes()
    dir = bird.get_dir()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    if round_start:
                        bird.jump()
                    if not round_start:
                        round_start = True
        if round_start:
            bird.move()
        if dir != bird.get_dir():
            if bird.get_dir() == -1:
                spikes = generate_right_side_spikes()
            else:
                spikes = generate_left_side_spikes()
            dir = bird.get_dir()
        draw_window(screen, bird, spikes)
        for spike in spikes:
            rect1 = spike.get_rect()
            rect2 = bird.get_rect()
            pygame.draw.rect(screen, (255,255,255), rect1)
            pygame.draw.rect(screen, (255,255,255), rect2)
            if rect1.colliderect(rect2):
                round_start = False
                bird.x = 160
                bird.y = 250
                bird.dir = 1
                spikes = generate_left_side_spikes()
        

    pygame.quit()

if __name__ == '__main__':
    main()