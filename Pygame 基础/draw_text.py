import sys
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('draw text')

myfont = pygame.font.Font(None, 60)

white = 255, 255, 255
blue = 0, 0, 255
textImage = myfont.render("Hello pygame", True, white)

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill(blue)
    screen.blit(textImage, (100, 100))
    pygame.display.update()