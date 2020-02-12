import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
blue = 0, 0, 255
pygame.display.set_caption('draw line')

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill(blue)

    # draw a line
    color = 100, 255, 200
    start_pos = 100, 100
    end_pos = 500, 400
    width = 8
    pygame.draw.line(screen, color, start_pos, end_pos, width)
    pygame.display.update()