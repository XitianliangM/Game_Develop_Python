import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
blue = 0, 0, 255
pygame.display.set_caption('draw rectangle')

pos_x = 300
pos_y = 250

vel_x = 0.2
vel_y = 0.1
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill(blue)

    # move
    pos_x += vel_x
    pos_y += vel_y

    # keep rectangle on the screen
    if pos_x > 500 or pos_x < 0:
        vel_x = -vel_x
    if pos_y > 400 or pos_y < 0:
        vel_y = -vel_y

    # draw a rectangle
    color = 255, 255, 0
    position = pos_x, pos_y, 100, 100
    width = 0
    pygame.draw.rect(screen, color, position, width)
    pygame.display.update()