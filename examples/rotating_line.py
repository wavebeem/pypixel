#!/usr/bin/python

from pypixel import *

show()

angle   = 0
x1      = WIDTH  / 2
y1      = HEIGHT / 2
radius  = HEIGHT
red     = rgb((255, 0, 0))
black   = rgb((0,   0, 0))
while True:
    x2 = radius * cos(angle) + x1
    y2 = radius * sin(angle) + y1
    line(red, (x1, y1), (x2, y2))
    update()
    line(black, (x1, y1), (x2, y2))

    angle += 1
