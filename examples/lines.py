#!/usr/bin/python

from pypixel import *

show()

hue = 0
width = 4
for x in xrange(0, WIDTH + 1, width):
    line(hsv2rgb((hue, 100, 100)), (x, 0), (x, HEIGHT), width)
    update()
    hue += 1
    hue %= 360
for x in reversed(xrange(0, WIDTH + 1, width)):
    line(hsv2rgb((hue, 100, 100)), (x, 0), (x, HEIGHT), width)
    update()
    hue += 1
    hue %= 360
