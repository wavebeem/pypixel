#!/usr/bin/python

from pypixel import *

show()

hue  = 0
while True:
    rectangle(hsv((hue, 100, 100)), ((0, 0), SIZE))
    update()
    hue += 1
    hue %= 360
