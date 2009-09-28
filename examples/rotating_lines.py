#!/usr/bin/python

from pypixel import *

show()

angle   = 0
x1      = WIDTH  / 2
y1      = HEIGHT / 2
radius  = HEIGHT
while True:
    x2 = radius * cos(angle) + x1
    y2 = radius * sin(angle) + y1
    line(RED, (x1, y1), (x2, y2))
    update()
    line(BLACK, (x1, y1), (x2, y2))

    x2 = radius * cos(-angle) + x1
    y2 = radius * sin(-angle) + y1
    line(GREEN, (x1, y1), (x2, y2))
    update()
    line(BLACK, (x1, y1), (x2, y2))

    angle += 1
