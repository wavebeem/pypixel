#!/usr/bin/python2

from pypixel import *

show()

hue  = 0
size = 10
for x in xrange(0, WIDTH + 1, size):
    for y in xrange(0, HEIGHT + 1, size):
        hsv = (hue, 100, 100)
        color = hsv2rgb(hsv)
        position = (x, y)
        circle(color, position, size)
        hue += 1
        hue %= 360
    update()

pause()
