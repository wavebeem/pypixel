#!/usr/bin/python

from pypixel import *
show()

while True:
    for i in xrange(100):
        x = random(0, WIDTH)
        y = random(0, HEIGHT)
        pixel((x, y), WHITE)
        update()
    clear()
