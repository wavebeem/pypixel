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
    line(RED, (x1, y1), (x2, y2), 10)
    circle(YELLOW, (x1, y1), 10)

    x3 = radius * cos(-angle) + x1
    y3 = radius * sin(-angle) + y1
    line(GREEN, (x1, y1), (x3, y3), 10)
    circle(YELLOW, (x1, y1), 10)
    update()
    line(BLACK, (x1, y1), (x2, y2), 10)
    line(BLACK, (x1, y1), (x3, y3), 10)

    angle += 1
