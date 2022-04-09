from multiprocessing import Event
import pygame, sys, random

WIDTH, HEIGHT = 640, 240

screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    