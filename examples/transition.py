#!/usr/bin/python

from pypixel import *

def transition():
    hue = 0
    size = WIDTH
    while True:
        for x in xrange(0, WIDTH + 1, size):
            for y in xrange(0, HEIGHT + 1, size):
                circle(hsv((hue, 100, 100)), (x, y), size)
                update()
                hue += 1
                hue %= 360

run(transition)
