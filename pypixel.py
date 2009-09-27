#!/usr/bin/python

import  random  as randy
import  pygame
import  math
from    pygame.locals   import *

# Screen size
WIDTH  = 640
HEIGHT = 480

def hsv(hsv):
    '''Create a new color from an HSV triplet'''
    c = pygame.Color(0)
    c.hsva = hsv + (100,) 
    return c

def hsl(hsl):
    '''Create a new color from an HSL triplet'''
    c = pygame.Color(0)
    c.hsla = hsl + (100,) 
    return c

def rgb(rgb):
    '''Create a new color from an RGB triplet'''
    c = pygame.Color(*rgb)
    return c

def hex(hexcode):
    r = int(hexcode[0:2], 16)
    g = int(hexcode[2:4], 16)
    b = int(hexcode[4:6], 16)
    c = pygame.Color(r, g, b)
    return c

# Basic color palette for simple drawing
RED     = hex("FF0000")
ORANGE  = hex("FFA500")
YELLOW  = hex("FFFF00")
GREEN   = hex("00FF00")
BLUE    = hex("0000FF")
INDIGO  = hex("A020F0")
VIOLET  = hex("EE82EE")

PINK    = hex("FFC0CB")

BLACK   = hex("000000")
GREY    = hex("888888")
GRAY    = hex("888888")
WHITE   = hex("FFFFFF")

def check():
    '''Check to see if the user wants to quit.
       That is, if they pressed Q, Esc, or tried to close the window.'''
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
            elif event.key == K_q:
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

# Most people can think easier in degrees than radians. These functions allow
# them to do so.
sin = lambda x: math.sin(math.radians(x))
cos = lambda x: math.cos(math.radians(x))
tan = lambda x: math.tan(math.radians(x))
