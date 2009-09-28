#!/usr/bin/python

from pypixel import *

show()

hue  = 0
size = (WIDTH, HEIGHT)
while True:
    rectangle(hsv((hue, 100, 100)), ((0, 0), size))
    update()
    hue += 1
    hue %= 360
