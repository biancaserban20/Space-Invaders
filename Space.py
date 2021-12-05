import pygame
import sys


BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

WIDTH = 800
HEIGHT = 600
 
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

running=True
while running:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
          running = False 

screen.fill((128, 0, 128))          
pygame.display.update()
