#!/usr/bin/python

from pypixel import *

show()

angle   = 0
x1      = WIDTH  / 2
y1      = HEIGHT / 2
radius  = HEIGHT
hue     = 0
size    = 100
while True:
    x2 = radius * cos(angle) + x1
    y2 = radius * sin(angle) + y1
    line(hsv((hue, 100, 100)), (x1, y1), (x2, y2), size)
    circle(BLACK, (WIDTH/2, HEIGHT/2), size)
    update()

    hue   += 1
    hue   %= 360
    angle += 1
    if angle/360.0 >= 1.0:
        hue    = random(360)
        angle %= 360
