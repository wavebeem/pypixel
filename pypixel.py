#!/usr/bin/python
#
# TODO
# Thread pypixel so that the end user doesn't have to insert check()
# everywhere...
#

import  pygame
from    pygame.locals   import *

WIDTH  = 640
HEIGHT = 480

# Copy over the pygame color class
Color = pygame.Color

def run(main):
    '''Set up the basic pypixel environment'''
    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.mouse.set_visible(False)

    main()
    while True:
        check()

def check():
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
            elif event.key == K_q:
                exit()


def screen():
    return pygame.display.get_surface()

def line(color, start, end, width=1):
    pygame.draw.line(screen(), color, start, end, width)
    pygame.display.update()

def circle(color, center, radius):
    pygame.draw.circle(screen(), color, center, radius, 0)
    pygame.display.update()
