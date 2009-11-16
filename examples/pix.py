#!/usr/bin/python

from pypixel import *
show()

for i in xrange(100):
    x = random(0, WIDTH)
    y = random(0, HEIGHT)
    pixel((x, y), WHITE)
    update()
