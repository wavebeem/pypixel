#!/usr/bin/python
#
# TODO
# Thread pypixel so that the end user doesn't have to insert check()
# everywhere...
#
# TODO
# Write color wrapper for HSVA, HSLA, RGBA
#

import  random  as randy
import  pygame
from    pygame.locals   import *

# Screen size
WIDTH  = 640
HEIGHT = 480

def hsv(hsv):
    '''Create a new color from an HSV triplet'''
    c = pygame.Color(0)
    c.hsva = hsv + (100,) 
    return c

def hsva(hsv):
    '''Create a new color from an HSVA quadruplet'''
    c = pygame.Color(0)
    c.hsva = hsva
    return c

def hsl(hsl):
    '''Create a new color from an HSL triplet'''
    c = pygame.Color(0)
    c.hsla = hsl + (100,) 
    return c

def hsla(hsl):
    '''Create a new color from an HSLA quadruplet'''
    c = pygame.Color(0)
    c.hsla = hsla
    return c

def rgb(rgb):
    '''Create a new color from an RGB triplet'''
    c = pygame.Color(*rgb)
    return c

def rgba(rgba):
    '''Create a new color from an RGBA quadruplet'''
    c = pygame.Color(*rgba)
    return c

def check():
    '''Check to see if the user wants to quit.
       That is, if they pressed Q, Esc, or tried to close the window.'''
    for event in pygame.event.get():
        if event.type == QUIT:
            print "Got signal to quit"
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                print "Got signal to quit"
                exit()
            elif event.key == K_q:
                print "Got signal to quit"
                exit()

def run(main):
    '''Set up the basic pypixel environment and run the main function'''
    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.mouse.set_visible(False)

    main()

def screen():
    return pygame.display.get_surface()

def update():
    '''Update the display and check if the user wants to quit'''
    pygame.display.update()
    check()

def line(color, start, end, width=1):
    '''Draw a line on the screen.
       color, start, end, [width]
       If width is not given, make it 1px wide.'''
    pygame.draw.line(screen(), color, start, end, width)

def circle(color, center, radius, width=0):
    '''Draw a circle on the screen.
       color, center, radius, [width]
       if width is 0 or not given, fill in the circle.'''
    pygame.draw.circle(screen(), color, center, radius, width)

def random(x=None, y=None):
    if x is None and y is None:
        return randy.random()
    elif y is None:
        return randy.randrange(0, x)
    else:
        return randy.randrange(x, y)
