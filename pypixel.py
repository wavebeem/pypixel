### pypixel - Python educational graphics library
### Copyright 2009-2011 Brian Mock <mock.brian@gmail.com>
###
### This library is free software; you can redistribute it and/or
### modify it under the terms of the GNU Library General Public
### License as published by the Free Software Foundation; either
### version 2 of the License, or (at your option) any later version.
###
### This library is distributed in the hope that it will be useful,
### but WITHOUT ANY WARRANTY; without even the implied warranty of
### MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
### Library General Public License for more details.
###
### You should have received a copy of the GNU Library General Public
### License along with this library; if not, write to the Free
### Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

'''
pypixel is a simple graphics library intended for educational use.
It is a collection of verbosely named functions that achieve basic geometric shape drawing.
'''

__author__  = "Brian Mock <mock.brian@gmail.com>"
__version__ = "0.1"

from math import log, sqrt, radians, degrees, pi, e

import sys
import pygame
import pygame.locals

# Screen size
SIZE = WIDTH, HEIGHT = 640, 480
CENTER = (WIDTH/2, HEIGHT/2)

### BEGIN PRIVATES
_clock         = None
_paused        = False
_show_fps      = False
_video_is_on   = False

_TITLE = "pypixel " + __version__
_program = None

_FPS = 60

_WINDOW_OPTS = (
    pygame.DOUBLEBUF |
    pygame.HWSURFACE
)

_FULLSCREEN_OPTS = (
    pygame.DOUBLEBUF  |
    pygame.HWSURFACE  |
    pygame.FULLSCREEN
)

_full_screen = False

def _debug(*xs):
    if __debug__:
        print " ".join(map(str, xs))

def _debug_noln(*xs):
    if __debug__:
        print " ".join(map(str, xs)),
        sys.stdout.flush()

# This should really be expressable with a lambda, python...
def _toggle_show_fps():
    global _show_fps
    _show_fps = not _show_fps

# This should really be expressable with a lambda, python...
def _toggle_paused():
    global _paused
    _paused = not _paused


def _toggle_full_screen():
    global _full_screen
    buf = _screen().copy()
    if not _full_screen:
        pygame.display.set_mode(SIZE, _FULLSCREEN_OPTS)
    else:
        pygame.display.set_mode(SIZE, _WINDOW_OPTS)
    _screen().blit(buf, (0, 0))
    _full_screen = not _full_screen

# Mapping of keys to functions
_keybinds = {
    pygame.locals.K_q: exit,
    pygame.locals.K_f: _toggle_full_screen,
    pygame.locals.K_v: _toggle_show_fps,
    pygame.locals.K_p: _toggle_paused,

    pygame.locals.K_SPACE:  _toggle_paused,
    pygame.locals.K_ESCAPE: exit,
}

def bind(key, func):
    '''\
    Binds the key to the function. The key is simply the character
    string of its representation, like 'k' for the K key, 'q' for the Q key
    and so on.
    '''

    global _keybinds
    _keybinds[ord(key)] = func

# This should really be expressable with a lambda, python...
def _noop():
    pass

def _handle_events():
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            exit()
        elif event.type == pygame.locals.KEYDOWN:
            # Execute the keybinding function, defaulting to a noop method
            _keybinds.get(event.key, _noop)()
    _try_to_flip()
    _clock.tick(_FPS)

def _try_to_flip():
    if _video_is_on:
        pygame.display.flip()

def pause():
    '''\
    Pauses the currently running program. Useful to examine the current state
    of the screen.
    '''
    global _paused
    _debug("::: Pausing game")
    _paused = True
    pygame.display.flip()
    while _paused:
        _handle_events()

def _play_pause():
    '''Toggle between paused and unpaused states.'''
    global _paused
    _paused = not _paused


def _check():
    '''\
    Check to see if the user wants to quit.
    That is, if they pressed Q, Esc, or tried to close the window.
    Also checks to see if the user pressed F for fullscreen.
    '''
    _handle_events()
    if _paused:
        pause()

def _screen():
    return pygame.display.get_surface()

### END PRIVATES

def show():
    '''Set up the basic pypixel environment, like the main window.'''
    global _clock
    global _video_is_on
    pygame.init()
    title(None)
    pygame.display.set_mode(SIZE, _WINDOW_OPTS)
    pygame.mouse.set_visible(False)
    _clock = pygame.time.Clock()
    _video_is_on = True

def update():
    '''Update the display and check if the user wants to quit.'''
    pygame.display.flip()
    _check()
    _clock.tick(_FPS)
    if _show_fps:
        _debug_noln("> %.2f FPS\r" % _clock.get_fps())

def line(color, start, end, width=1):
    '''\
    Draw a line on the screen.
    If width is not given, make it 1px wide.
    '''
    pygame.draw.line(_screen(), color, start, end, width)

def circle(color, center, radius, width=0):
    '''\
    Draw a circle on the screen.
    if width is 0 or not given, fill in the circle.
    '''
    pygame.draw.circle(_screen(), color, center, radius, width)

def rectangle(color, rect, width=0, **kwargs):
    '''\
    Draws a rectangle.
    The optional width specifies the outline width. The rectangle is filled
    if this is 0. The keyword args may contain "center", which is a boolean
    that instructs pypixel to use the coordinate specified for the rectangle
    to be the center instead of the top left corner. The rect itself is a pair
    of pairs, specifiying a location and dimensions.
    '''
    rect2 = pygame.Rect(*rect)
    if kwargs.get("center", False):
        rect2.center = rect[0]
    pygame.draw.rect(_screen(), color, rect2, width)

def ellipse(color, rect, width=0, **kwargs):
    '''\
    Draws an ellipse.
    The optional width specifies the outline width. The rectangle is filled
    if this is 0. The keyword args may contain "center", which is a boolean
    that instructs pypixel to use the coordinate specified for the rectangle
    to be the center instead of the top left corner. The rect itself is a pair
    of pairs, specifiying a location and dimensions.
    '''
    rect2 = pygame.Rect(*rect)
    if kwargs.get("center", False):
        rect2.center = rect[0]
    pygame.draw.ellipse(_screen(), color, rect2, width)

def polygon(color, points, width=0):
    '''\
    Draws a polygon with the given list of points, and the specified line
    width (by default, with 0, it is filled in).
    '''
    pygame.draw.polygon(_screen(), color, points, width)

def equilateral(color, center, length, width=0):
    '''Draws an equilateral triangle with side length length.'''
    x, y = center
    bottom_left  = x - length/2, y + length/2
    bottom_right = x + length/2, y + length/2
    top = x, y - length/2
    polygon(color, [bottom_left, top, bottom_right], width)

def arc(color, circ, start_angle, stop_angle, width=1, **kwargs):
    '''\
    Draws an arc on the circle circ from start_angle to stop_angle of width
    width. circ is of the form ((x, y), radius) or (center, radius).
    Note that setting width to 0 will NOT fill in the arc.
    '''
    point, radius = circ
    rect = pygame.Rect((0, 0), (radius, radius))
    rect.center = point
    start_angle = radians(start_angle)
    stop_angle  = radians(stop_angle)
    pygame.draw.arc(_screen(), color, rect, start_angle, stop_angle, width)

def pixel(color, point):
    '''Sets the pixel at the given point to the given color.'''
    _screen().set_at(point, color)

def clear():
    '''Clears the screen by making it entirely black.'''
    rectangle(BLACK, ((0, 0), SIZE))

def random(x=None, y=None, **kwargs):
    '''\
    When given no arguments, return a random real number in the range [0, 1).
    When given one argument, return a random integer in the range [0, x).
    When given two arguments, return a random integer in the range [x, y).
    If the argument 'end=False' is included, the random does not include the endpoint.
    '''
    import random
    rand_func = None
    if kwargs.get("end", True):
        rand_func = random.randint
    else:
        rand_func = random.randrange

    if x is None and y is None:
        return random.random()
    elif y is None:
        return rand_func(0, x)
    else:
        return rand_func(x, y)

def hsv2rgb(hsv):
    '''Create a new color from an HSV triplet. Hues range from 0 to 359,
    saturation ranges from 0 to 100, and value ranges from 0 to 100.'''
    c = pygame.Color(0)
    c.hsva = hsv + (1,) 
    return c[0:-1]

def hsl2rgb(hsl):
    '''Create a new color from an HSL triplet. Hues range from 0 to 359,
    saturation ranges from 0 to 100, and lightness ranges from 0 to 100.'''
    c = pygame.Color(0)
    c.hsla = hsl + (1,) 
    return c[0:-1]

def hex2rgb(hexcode):
    '''\
    Create a new color from a six digit hexadecimal number, as in HTML (but
    but without the the # sign). The format is a string of the form "RRGGBB"
    where RR, GG, and BB are two digit hexadecimal digits specifying the color
    values for red, green and blue respectively.
    '''
    r = int(hexcode[0:2], 16)
    g = int(hexcode[2:4], 16)
    b = int(hexcode[4:6], 16)
    c = pygame.Color(r, g, b)
    return c[0:-1]

# {{{ Basic color palette for simple drawing
RED     = hex2rgb("FF0000")
ORANGE  = hex2rgb("FFA500")
YELLOW  = hex2rgb("FFFF00")
GREEN   = hex2rgb("00FF00")
BLUE    = hex2rgb("0000FF")
INDIGO  = hex2rgb("A020F0")
VIOLET  = hex2rgb("EE82EE")
#######################
PINK    = hex2rgb("FFC0CB")
#######################
BLACK   = hex2rgb("000000")
GREY    = hex2rgb("888888")
GRAY    = hex2rgb("888888")
WHITE   = hex2rgb("FFFFFF")
# }}}

# Possibly better not to have to teach modulo immediately
def odd(x):
    '''Returns true if x is odd, false otherwise.'''
    return (x % 2) == 1

def even(x):
    '''Returns true if x is even, false otherwise.'''
    return (x % 2) == 0

# Most people can think easier in degrees than radians. These functions allow
# them to do so.
def sin(x):
    '''Return the sine of x (x is in degrees).'''
    from math import sin, cos, tan
    return sin(radians(x))

def cos(x):
    '''Return the cosine of x (x is in degrees).'''
    from math import sin, cos, tan
    return cos(radians(x))

def tan(x):
    '''Return the tangent of x (x is in degrees).'''
    from math import sin, cos, tan
    return tan(radians(x))

def abs(x):
    '''Return the absolute value of the argument.'''
    from math import fabs
    if isinstance(x, int):
        return int(fabs(x))
    else:
        return fabs(x)

def cartesian(polar):
    '''This function converts a polar point (r, theta) to a cartesian point (x, y)'''
    r, theta = polar

    def adjust(point):
        x, y = point
        return (x + WIDTH/2, y + HEIGHT/2)

    def int_pair(point):
        x, y = point
        return (int(x), int(y))

    return int_pair(adjust((r * cos(theta), r * sin(theta))))

def midpoint(p1, p2):
    '''Returns the midpoint of p1 and p2.'''
    x1, y1 = p1
    x2, y2 = p2

    xm, ym = (x1 + x2)/2, (y1 + y2)/2

    return (xm, ym)

def title(t):
    '''Sets the title of the currently running program.
    Using None, this resets to a default title.'''
    global _program
    if t is not None:
        _program = t
    if _program is None:
        pygame.display.set_caption(_TITLE)
    else:
        pygame.display.set_caption(_program + ': ' + _TITLE)
