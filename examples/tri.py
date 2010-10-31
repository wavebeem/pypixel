#!/usr/bin/python2

from pypixel import *

show()

color = GREY
center = (WIDTH/2, HEIGHT/2)
for width in reversed(xrange(1, HEIGHT/2)):
    if width % 50 < 25:
        color = WHITE
    else:
        color = GREY
    equilateral(color, center, width)
    update()
    clear()
