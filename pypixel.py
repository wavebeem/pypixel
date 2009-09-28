#!/usr/bin/python

import random  as randy
import pygame
import pygame.locals
import math

# TODO
#
# * Add the following drawing mechanisms
#   * Ellipses
#   * Arcs
#   * Polygons
#   * Pixels
# * Add support for toggling full_screen
# * Rename main window to "pypixel application" or something
# * Add some kind of pause when the program is done

# Screen size
SIZE = WIDTH, HEIGHT = 640, 480

_WINDOW_OPTS =        \
    pygame.DOUBLEBUF | \
    pygame.HWSURFACE    \
#   pygame.OPENGL

_FULLSCREEN_OPTS =     \
    pygame.DOUBLEBUF  | \
    pygame.HWSURFACE  |  \
    pygame.FULLSCREEN     \
#   pygame.OPENGL

_full_screen = False

def _debug(*xs):
    if __debug__:
        print " ".join([str(x) for x in xs])

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
    '''\
    Check to see if the user wants to quit.
    That is, if they pressed Q, Esc, or tried to close the window.
    '''
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            exit()
        if event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_ESCAPE:
                exit()
            elif event.key == pygame.locals.K_q:
                exit()
            elif event.key == pygame.locals.K_f:
                _toggle_full_screen()
            elif event.key == pygame.locals.K_v:
                _debug(pygame.display.Info())

def show():
    '''Set up the basic pypixel environment and run the main function'''
    pygame.init()
    pygame.display.set_mode(SIZE, _WINDOW_OPTS)
    pygame.mouse.set_visible(False)
    pygame.display.set_caption("PyPixel")

def _screen():
    return pygame.display.get_surface()

def _toggle_full_screen():
    global _full_screen
    if not _full_screen:
        pygame.display.set_mode(SIZE, _FULLSCREEN_OPTS)
    else:
        pygame.display.set_mode(SIZE, _WINDOW_OPTS)
    _full_screen = not _full_screen

def update():
    '''Update the display and check if the user wants to quit'''
    pygame.display.flip()
    check()

def line(color, start, end, width=1):
    '''\
    Draw a line on the _screen.
    color, start, end, [width]
    If width is not given, make it 1px wide.
    '''
    pygame.draw.line(_screen(), color, start, end, width)

def circle(color, center, radius, width=0):
    '''\
    Draw a circle on the _screen.
    color, center, radius, [width]
    if width is 0 or not given, fill in the circle.
    '''
    pygame.draw.circle(_screen(), color, center, radius, width)

def rectangle(color, rect, width=0, **kwargs):
    '''\
    Draws a rectangle.
    color, rect, [width], [center=False]
    The optional width specifies the outline width. The rectangle is filled
    if this is 0. The keyword args may contain "center", which instructs
    pypixel to use the coordinate specified for the rectangle to be the
    center instead of the top left corner. The rect itself is a pair of
    pairs, specifiying a location and dimensions.
    '''
    if "center" in kwargs and kwargs["center"]:
        rect2        = pygame.Rect(*rect)
        rect2.center = rect[0]
        pygame.draw.rect(_screen(), color, rect2, width)
    else:
        pygame.draw.rect(_screen(), color, pygame.Rect(*rect), width)

def ellipse(color, rect, width=0, **kwargs):
    '''\
    Draws an ellipse.
    color, rect, [width], [center=False]
    The optional width specifies the outline width. The rectangle is filled
    if this is 0. The keyword args may contain "center", which instructs
    pypixel to use the coordinate specified for the rectangle to be the
    center instead of the top left corner. The rect itself is a pair of
    pairs, specifiying a location and dimensions.
    '''
    if "center" in kwargs and kwargs["center"]:
        rect2        = pygame.Rect(*rect)
        rect2.center = rect[0]
        pygame.draw.ellipse(_screen(), color, rect2, width)
    else:
        pygame.draw.ellipse(_screen(), color, pygame.Rect(*rect), width)

def random(x=None, y=None):
    '''\
    When given no arguments, return a random number in the range [0, 1).
    When given one argument, return a random number in the range [0, x).
    When given two arguments, return a random number in the range [x, y).
    '''
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
