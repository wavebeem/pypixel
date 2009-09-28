#!/usr/bin/python

from pypixel import *

show()

hue = 0
while True:
    x  = WIDTH  / 2
    y  = HEIGHT / 2
    w  = random(WIDTH)  / 2
    h  = random(HEIGHT) / 2
    hue += 1
    hue %= 360
    sat  = 100
    val  = 100
    col  = hsv((hue, sat, val))
    rect = ((x, y), (w, h))
    rectangle(col, rect, center=True)
    update()
